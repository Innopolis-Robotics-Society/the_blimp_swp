# Customer Review Transcript

**Date:** 28.06.2026
**Participants:** Daniyar (PO), Arina (SM), Iuliana, Svetlana, Eugene (Customer)
**Recording:** https://disk.yandex.ru/i/SlLfdo8aPhLM9A (instructors only)

---

**Daniyar**
So, we can start. We can start with the first test.

**Eugene**
Okay, I'll get familiar with it and turn it on. I'll download it on Linux anyway. VSL is not critical for me, but okay. The instructions are quite detailed, pretty cool. So, I've already launched the QGroundControl, so everything works there. That's great.

**Daniyar**
Yeah, great. So, we're done with the first one. Let's do the second one, then. We don't need to close anything. Let's continue from that state. You can just use QGroundControl to check that everything is working.

**Eugene**
I've actually launched it before, and now I can see that everything is fine. I don't see any problems with test 2.

**Daniyar**
Let's check the third one, too. Let's try to change the settings. For example, you can change the arming settings. When the simulator is running, it loads the GPS for about 15 seconds. It's a virtual GPS, but it still loads. So, you can try to disable the GPS check and try to arm it.

**Eugene**
Let's try it. Let me finish reading the instructions. It seems to be working, so I think everything is fine.

**Daniyar**
Great. So, the UATs are successful. There are a few more questions about the project. Let me find them. So, we're starting to implement the CI/CD. So far, we've done the CI for the backend. Should we add more tests via GitHub? Maybe in the simulator?

**Eugene**
In theory, you can have three systems in the CI/CD. The first one is to check your code with linters. The second one is to build a Docker file and publish it in Harbour. You can set it up, too. And the third one is the documentation. Automatic assembly. I won't have to describe the documentation in great detail. It's probably just a list of things. But if you have time, it would be great if you could use Sphinx to describe your repository, make a full-fledged Docs folder, and when you push it to GitHub, your CI/CD will automatically build the documentation after all the checks and publish it via GitHub Pages. I can send you one of our repositories that does just that, so that you have an example.

**Daniyar**
That would be great.

**Eugene**
I think that's more than enough for you. The rest will be unnecessary work.

**Daniyar**
We already have a linter that checks the documentation using links. We did that during the first week, as far as I remember. We'll probably look at what you said. We've already done the assembly in Docker via Docker Hub. We'll just repeat it with the new CI/CD implementation. So, that's clear. The question is about next week. What do you expect from us next week?

**Eugene**
Look, our Capstone team has now received all the equipment. The only thing we have now is the remote for your team, and we already have everything else. So, we need to figure out how to specify the frames of the motors as soon as possible. That's what you were doing, right? Yes, yes. There are some successes already. So that you can contact the Capstone team and start preparing the flight controller infrastructure for the system to start working. Because, in theory, the guys will assemble everything in the next week, and we'll start with the first test.

**Daniyar**
Okay.

**Eugene**
If I'm not mistaken, this is what Egor is doing in that team. You can contact him. Or you can just write to him in the general chat that we already have and discuss it. Tell him about your experience, so that we can work together.

**Daniyar**
Okay. At the moment, we have a ready-to-use simulator for these requirements. It's ready. It's in the connect-to-SITL stage, just so it can work. Literally SITL. The rest of it is working. And now we are studying the script and parameters for configuring the SITL for the hold. Well, for configuring the hold of the copter for the hold. And in the next tests, it's all about SITL.

**Eugene**
Okay, great. Just hurry up, please. Tomorrow, the day after tomorrow, to RISE with the guys. Because otherwise they might start running now and we might lose synchronization. Because they might start doing something on their own. Okay. So that your experience and what you've been doing can be combined.

**Daniyar**
So, to put it bluntly, we are working on the software part of the flight controller.

**Eugene**
Well, at least the frames, yes.

**Daniyar**
Yes, yes.

**Eugene**
So, they are navigating the other blocks and we are synchronizing it. And writing it in one place.

**Daniyar**
Okay.

**Eugene**
I have no other questions. I'm waiting for some interesting and beautiful videos with the simulator. How are you going to do it? When are you going to do it? When will you be able to run it?

**Daniyar**
In general, I think, we can try to do it in 4 days. So, on Thursday, we'll write it down and see what we've managed to do during that time.

**Eugene**
Okay, then we'll write it down on Thursday and discuss it in the chat.

**Daniyar**
Okay. Okay.

**Eugene**
Then we'll put a deadline for you to write to the guys on the second level of Krysis and discuss the question of frames and how to flash the flight controller. And on Thursday, we'll write it down and discuss it in the simulator so that it can run as soon as possible. Okay, then? Okay. And gradually. And most importantly, don't forget to write the documentation so that all the blocks of your system are documented. Ideally, I'll send it to you. It was done in our repository. Okay. With the automatic build. It will be convenient and beautiful.

**Daniyar**
Okay, we'll see.

**Eugene**
Do you have any more questions for me? Because I don't have anything else.

**Daniyar**
We're done, too.

**Eugene**
Okay, then. Thank you all for the meeting. Have a good week. And bye. Bye.

**Daniyar**
Goodbye.
