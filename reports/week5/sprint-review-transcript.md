[Daniyar]
So, recording is on. Today we're going to test two more UATs. These tests will also be a demo of what we're going to do.

I can show you a separate demo as well, while you're recording.

[Eugene]
I've already done that for myself. You'll show your demo as well.

[Daniyar]
Okay, let's do it. Let's just run the Docker containers. One for SITL.

[Eugene]
Are you talking about Windows in your documentation? Is Docker Compose ready to work with Windows?

[Daniyar]
In Windows documentation?

[Eugene]
You're talking about the UI.

[Daniyar]
Oh, you mean with WSL?

[Eugene]
I know how it works, but Docker Compose will require different Windows settings. You'll probably need to specify the full IP of the port. I'd cut out the whole thing about Windows, because it's too much effort for you, and too many instructions for the user, the team, the course, and other people.

I'd cut out the whole thing about Windows, and say, install on Linux, and that's it. And we only have Linux ready.

[Daniyar]
By the way, everything works on Windows. And to be honest, I ignored a couple of things about the installation, and it still worked. Maybe they're automatically installed together with the WSL installation, I suspect.

But it's a fact.

[Eugene]
Well, if they're installed, they're installed. Okay, fine.

[Daniyar]
In general, everything works. We just copied the official QGroundControl, we didn't write our own code there. It's just that through Docker, it creates a new bundle and pulls the official repository.

By the way, what's happening with the vehicle? We decided not to make another repository that copies ArduPilot. We're writing our own vehicle directory.

So, along with ArduPilot and the stock Blimp, we're writing our own ArduMotorBlimp, which will meet our requirements.

[Eugene]
So there will be all the configs for the motor frame and everything else?

[Daniyar]
Yes, yes, yes. I looked at it. In general, this is the same code that we would have modified.

There are some problems at the build stage, because ArduPilot needs to understand that we have another vehicle that needs to be built the same way. And this is a bit of a problem. But in general, everything is solvable.

[Eugene]
And if there are any difficulties, write to Egor and make sure you're doing everything right. When do you expect to finish this? Because in the next few days we'll be assembling the vehicle itself, we'll run tests on Betaflight, and then we'll have to start working with ArduPilot.

[Daniyar]
Well, I was planning to look at the build stage today and tomorrow. So that next week we can start with the ready-made base, so that we can start changing the code. If it doesn't work out, then on Monday or Tuesday we'll have deadlines for the finished part, so that we can actually run our code.

And then we'll write in all the logic that we need. By the way, I looked at why we ended up writing our own code. Because ArduPilot's logic is completely different — it fights gravity, and I couldn't find a place where I could simply turn it off.

The plane doesn't work for us for obvious reasons, because there are height controls and all that. And ArduPilot is built around a control logic that is incompatible with our design. That is, it can control movement along the three axes and rotate around yaw.

And our custom ArduPilot vehicle will work so that it can rotate along all three axes and fly back and forth. In this regard, it looks more like a quadcopter, but it doesn't work for a quadcopter either. So we decided to copy the Blimp vehicle and rewrite it with different control logic.

So we'll rewrite the motor logic, it's not difficult at all. We'll rewrite Loiter. In general, it should also be quite simple.

The main thing is to implement the control logic so that it first turns and then flies, or to implement it smoothly. And then just rewrite the control mode.

We don't even need all the control modes. We won't have RTL, in fact. Because we will operate indoors and fly around obstacles, we won't be able to configure the standard RTL. In any emergency, Stop mode will most likely be used instead.

[Eugene]
Well, yes, we'll just have to turn everything off and watch it slowly fall.

[Daniyar]
What will we need? We'll need to configure the manual control mode. And the other control mode...

I don't remember what it's called. Guided, I think, or Auto.

[Eugene]
Well, yes, PX4 and ArduPilot call them differently.

[Daniyar]
And Blimp and Stop. Accordingly, for emergencies. Yes, great.

In general, the plan is quite clear. There are only some problems with the ArduPilot build dependencies. But I think we'll solve them somehow.

We'll discuss it with Egor.

[Eugene]
Agreed. In fact, I have no other questions. Now we'll finish the hardware, and after that we'll proceed to full-scale testing of your part.

Both on the real system and in the simulator. If you have no questions for me...

[Daniyar]
Yes, yes, we have everything.

[Eugene]
Have a good evening. Everything works, everything is fine.

[Daniyar]
Okay.

[Eugene]
Have a good evening, bye.

[Daniyar]
Goodbye.
