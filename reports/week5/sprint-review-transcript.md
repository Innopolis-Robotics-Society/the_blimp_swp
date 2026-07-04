
[Daniyar]
So, recording is on. Today we're going to test two more UI tests. These tests will also be a demo of what we're going to do.

I can show you a separate demo as well, while you're recording.

[Eugene]
I've already done that for myself. You'll show your demo as well.

[Daniyar]
Okay, let's do it. Let's just run Docker packages. One for Settler.

[Eugene]
Are you talking about Windows in your documentation? Is Docker Compose ready to work with Windows?

[Daniyar]
In Windows documentation?

[Eugene]
You're talking about the UI.

[Daniyar]
Oh, you mean with VSL?

[Eugene]
I know how it works, but Docker Compose will require different window settings. You'll probably need to specify the full IP of the port. I'd cut out the whole thing about Windows, because it's too much hammer for you, and too many instructions for the user, the team, the course, and other people.

I'd cut out the whole thing about Windows, and say, install on Linux, and that's it. And we only have Linux ready.

[Daniyar]
By the way, everything works on Windows. And to be honest, I ignored a couple of things about the installation, and it still worked. Maybe they're automatically pulled together with the VSL installation, I suspect.

But it's a fact.

[Eugene]
Well, if they're pulled, they're pulled. Okay, fine.

[Daniyar]
In general, everything works. We just copied the official QGram control, we didn't write our own code there. It's just that through Docker, it creates a new bundle and pulls the official repository.

By the way, what's happening with the title? We decided not to make another repository that copies RDP. We're writing our own vehicle directory.

So, along with RDP and stock blimp, we're writing our own RduMotorBlimp, which will meet our requirements.

[Eugene]
So there will be all the configs for the frame of the motors and everything else?

[Daniyar]
Yes, yes, yes. I looked at it. In general, this is the same code that we would have corrected.

There are some problems at the build stage, because RDP needs to understand that we have another vehicle that needs to be built the same way. And this is a bit of a problem. But in general, everything is solvable.

[Eugene]
And if there are any difficulties, write to Egor and make sure you're doing everything right. When do you expect to finish this? Because in the next few days we'll be assembling the vehicle itself, we'll run tests on Betaflight, and then we'll have to start RDP.

[Daniyar]
Well, I was planning to look at the build stage today and tomorrow. So that next week we can start with the ready-made base, so that we can start changing the code. If it doesn't work out, then on Monday, Tuesday, we'll have deadlines for the finished part, so that we can actually run our code.

And then we'll write in all the logic that we need. By the way, I looked at why we ended up with our code. Because RDP's logic is completely different, it fights gravity, and I couldn't find a place where I could just turn it off.

The plane doesn't work for us for obvious reasons, because there are height controls and all that. And RDP is built on incompatible with our schematic logic. That is, there is control, it can control movement along the three axes and rotate along the yaw.

And our RDP will work so that it can rotate along all three axes and fly back and forth. In this regard, it looks more like a quadcopter, but it doesn't work for a quadcopter either. So we decided to copy Blink and just rewrite it for another logic.

So we'll rewrite the logic for the engine, it's not difficult at all. We'll rewrite the loiter. There, in general, it will also be quite simple.

The main thing there is to enter the control logic, that we first turn, and then fly. Or somehow smoothly implement it. And then just rewrite the control mode.

We don't even need all the control modes, we won't have RTL, in fact. Due to the fact that we will have a room and we will fly around the obstacles, we will not be able to configure standard RTL. And in any emergency, the stop will most likely turn on.

[Eugene]
Well, yes, we'll just have to turn everything off and just watch it slowly fall.

[Daniyar]
And what will we need there? We'll need to configure the manual control mode. And the control mode...

I don't remember what it's called. Guided, I think, or auto.

[Eugene]
Well, yes, P4 and R2 are called differently.

[Daniyar]
And blend and stop. Accordingly, for an emergency. Yes, great.

In general, the plan is quite clear. There are only problems in the dependencies of the pilot. But I think we'll fight them somehow.

We'll discuss it with Egor.

[Eugene]
Agreed. In fact, I have no other questions. Now we will finish the hardware, and after that we will proceed to the full-fledged tests of your part.

Already on the system and in the simulators. If you have no questions for me...

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

