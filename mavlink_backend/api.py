import logging
from fastapi import FastAPI, WebSocket, WebSocketDisconnect, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import uvicorn
import asyncio
from contextlib import asynccontextmanager
from mavlink_backend.backend import MAVLinkBackend

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='airship_backend.log',
    filemode='a'
)

logger = logging.getLogger(__name__)

backend: Optional[MAVLinkBackend] = None


class SetpointRequest(BaseModel):
    x: float
    y: float
    z: float
    yaw: Optional[float] = 0.0


class Waypoint(BaseModel):
    lat: float
    lon: float
    alt: float


class MissionRequest(BaseModel):
    waypoints: List[Waypoint]


@asynccontextmanager
async def lifespan(app: FastAPI):
    global backend
    try:
        backend = MAVLinkBackend('udp:127.0.0.1:14550')
        logger.info("MAVLink Backend started!")
    except Exception as e:
        logger.error(f"Failed to connect to SITL: {e}")

    yield

    if backend:
        backend.stop()


app = FastAPI(title="Airship MAVLink Backend", version="1.0", lifespan=lifespan)


@app.get("/")
async def root():
    return {"status": "ok", "message": "Airship MAVLink Backend API"}


@app.get("/telemetry")
async def get_telemetry():
    if not backend:
        raise HTTPException(status_code=503, detail="Backend not connected")
    return backend.get_telemetry()


@app.post("/setpoint")
async def send_setpoint(req: SetpointRequest):
    if not backend:
        raise HTTPException(status_code=503, detail="Backend not connected")
    backend.send_setpoint(req.x, req.y, req.z, req.yaw)
    return {"status": "ok", "message": "Setpoint sent"}


@app.post("/mission")
async def upload_mission(req: MissionRequest):
    if not backend:
        raise HTTPException(status_code=503, detail="Backend not connected")

    waypoints = [(wp.lat, wp.lon, wp.alt) for wp in req.waypoints]

    success = backend.upload_mission(waypoints)
    if success:
        return {"status": "ok", "message": "Mission uploaded successfully"}
    else:
        raise HTTPException(status_code=500, detail="Failed to upload mission")


@app.websocket("/ws/telemetry")
async def websocket_telemetry(websocket: WebSocket):
    await websocket.accept()
    logger.info("WebSocket client connected")

    try:
        while True:
            if backend:
                telemetry = backend.get_telemetry()
                await websocket.send_json(telemetry)
            await asyncio.sleep(0.1)
    except WebSocketDisconnect:
        logger.info("WebSocket client disconnected")
