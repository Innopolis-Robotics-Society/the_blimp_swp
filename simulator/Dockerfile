FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY blimp_sim.py .
COPY blimp_config.yaml .

ENV PYTHONUNBUFFERED=1

EXPOSE 9002/udp

CMD ["python3", "-u", "blimp_sim.py", "--config", "blimp_config.yaml"]
