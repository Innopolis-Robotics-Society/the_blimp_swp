# Customer Review Transcript – Sprint 1

**Date:** 20.06.2026  
**Participants:** Daniyar (Product Owner), Arina (Scrum Master), Iuliana (Developer), Svetlana (Developer), Eugene (Customer)  
**Recording:** Available for instructors – [Yandex Disk link](https://disk.yandex.ru/i/8LWrxJYlks_fsg)

---

[00:03] — Daniyar
So, today we are showing you our MVP v1 and what we have done during the first two weeks. Now I will start the demo. At the moment, we have a working SITL that can run anywhere using Docker. We also started working on our own simulator for the airship, and it is currently under review.

At the same time, we are working on setting up the connection from the Raspberry Pi through MAVLink and the ELRS Backpack to the flight controller. The simulator runs inside a Docker container. It runs on the device and sends data to QGroundControl through a port. It needs some time for the pre-arm process.

Overall, the simulator works as expected through Docker. Right now, we are working on connecting our airship physics simulator to SITL and adding neutral buoyancy. Since we will fly indoors, we do not simulate wind. We are trying to make the physics as close as possible to a real airship.

So far, we have added aerodynamic simulation in all three directions with separate parameters, so we can match the behavior of a real airship. We also simulate rotational inertia, movement inertia, and the effects of all motors, including their thrust and torque. We plan to include all of this in the simulator.

[03:42] — Eugene
Which option did you finally choose? Are you writing all the dynamics in Python with your own formulas?

[03:49] — Daniyar
Yes. Right now, we write everything in Python, and we are thinking about whether we should switch to Unity or some other external simulator later.

[04:10] — Eugene
But if you write everything in Python, there may not be much reason to switch. Especially if you make a simple 3D visualization with Matplotlib, it should be more than enough. We do not really need a full simulator here. The main goal is to test and improve the motor frame layout. By the way, how is that going now?

[04:32] — Daniyar
At the moment, in Docker we mounted two folders that let us configure scripts and vehicle parameters. This means we can test scripts and parameters for our airship in simulation. We can set custom control logic and create parameters that are important for us.

Right now, our goal is to build the airship simulation without changing the original source code. However, we are not sure that this will be completely possible. We may have to modify some parts of the ArduPilot source code.

[05:27] — Eugene
I understand. That is possible, but if you decide to do that, we should arrange a separate meeting, preferably in person, and discuss it first. It is a difficult task, and maybe there will be other options. If there is no other way, then we will modify their code.

What about QGroundControl? Do you have any ideas about customizing it, or have you not worked on that yet?

[05:58] — Daniyar
We have not worked on that yet. It has good customization potential because it is open source. There are already custom versions, and we could create our own one. But we have not explored it in detail yet.

[06:22] — Eugene
Alright, then we still have time. Overall, I am happy with the progress. One more thing: could you send me the link to your simulator after the meeting? I would like to take a look at it.

[06:30] — Daniyar
Okay.

[06:36] — Eugene
Otherwise, I think everything is going well. Let us keep working. I think the RC transmitter will arrive within the next four days, and then we can start testing the full connection between the Raspberry Pi, the LRS system, and the flight controller.

[06:52] — Daniyar
Great.

[06:53] — Eugene
It has already cleared customs. Now we are waiting for it to be handed over to the delivery service. So I think everything is fine.

Anyway, you are doing a good job. Do you have any questions right now, and do you already have a plan for the next steps?

[07:11] — Daniyar
Our plan is to finish the simulator and connect it to SITL so that we can start tuning the airship itself. After that, we will test what can be done using scripts and parameters and see if they allow us to achieve the behavior we need.

Then there are two possible options. Either we configure the airship using scripts and parameters, or we start modifying the source code. The second option will take more time.

[08:06] — Eugene
Okay. Sounds good.

[08:08] — Daniyar
As for the connection between the computer and the flight controller, when the RC transmitter arrives, we will start setting up the whole system.

[08:23] — Eugene
Alright. One more thing. QGroundControl is not included in the Docker container yet, right? Okay. Just keep in mind that it should also be added there.

[08:35] — Daniyar
We will make a note to include QGroundControl in the Docker package.

[08:44] — Eugene
Good. If you have no more questions, then I have none either.

[08:51] — Daniyar
I will check the script. That is all.

[09:11] — Eugene
Thanks, everyone, for the meeting, and good luck with your work. Have a great week. Bye.
