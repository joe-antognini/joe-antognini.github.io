---
layout: post
title: My experience with the Librem 13 laptop
date: 2020-12-6
categories: misc
image:
  feature: constellations3.jpg
---

I've been using Purism's Librem 13 laptop as my primary personal laptop for
just over a year now.  Given that Purism laptops are not widely used I thought
I would write up my experience with it for anyone who is considering a Librem
laptop.  (The Librem 13 is no longer available, but Purism recently released
the [Librem 14][4] instead.)

**tl;dr**: As much as I wanted to like it, the build quality issues are too
serious for me to recommend buying it.  I've learned some workarounds for the
quirks of this laptop so I'll probably continue to use it for a little while,
but I will have to go with another company when I buy my next laptop.

I'll start with the things I liked, move on to some of the annoyances I've run
into, and end with the dealbreakers.  One caveat to all this is that I switched
from their custom operating system, [PureOS][1], to Ubuntu not long after I
started using the laptop.  (I didn't feel super comfortable relying on a
smallish company for my OS and preferred using a more common Linux distro.)  It
is possible that some of the issues I ran into wouldn't have existed had I
stuck with PureOS.

## The Good

There are a lot of things going for this laptop!  Modern laptops have almost
become commodified so there's generally not a lot to differentiate one brand
from the next.  But Purism has done a good job standing out from the crowd with
their focus on privacy and open source software.  The bootloader is [open
source][2], the firmware has [tamper evidence][3], and of course, the Librem
boasts those famous hardware kill switches for the WiFi, camera, and
microphone.  So in case you don't *really* trust that your OS is secretly
recording you and streaming your chats with Edward Snowden directly to the NSA,
you can physically disable the microphone, the WiFi, or both.  To be honest it
feels like a bit of a gimmick to me, but I appreciate the attitude.  It is a
great signal that when they say they support privacy they *mean* it.

On a more superficial level, the laptop looks really nice.  In particular there
is no logo on the back --- it is discretely printed on the bottom side of the
laptop.  The keyboard feels good, the battery life is decent, and it is
sufficiently powerful for the work I do on it (mostly programming and training
some small ML models, but also keeping open an ungodly number of Firefox tabs).

{% 
    include image name="librem-13-back.jpg"
    caption="The back of the Librem 13 has no logo."
%}

## The Bad

As neat as the hardware kill switches are, they are a little bit finicky.  The
switches themselves feel sturdy, but it's often the case that when the laptop
wakes up it thinks that the WiFi has been hardware disabled when it hasn't.
Flicking the WiFi switch off and on again fixes this, but it is an annoyance.

The WiFi antenna is not great.  Sitting about 12 feet from my WiFi router put
the laptop out of range, whereas I get a very strong signal with the Macbook
Pro I use for work even at longer distances.

There have been a few other things about the Librem that have bugged me.  There
are three LEDs just above the right side of the keyboard that display the power
status, the WiFi status, and the charging status.  In the dark these LEDs are
*very* bright and cannot be dimmed.  Furthermore, because the charging LED is
right above the keyboard, you cannot see it when you close the laptop.  So it
is hard to discreetly charge the laptop somewhere and be sure that it is really
charging.

{% 
    include image name="librem-keyboard.jpg"
    caption="The Librem 13 keyboard."
%}

Another minor thing is that the Librem 13 uses a barrel charger rather than
USB-C like many modern laptops do.  Unfortunately this means that you have to
take one more charger with you when travelling.

Finally, when I switched to Ubuntu I noticed that the pipe key ("`|`") was not
working.  I had to spend a few hours figuring out how to get the OS to
recognize that key and map it properly.  It is hard to blame Purism *too* much
for that since I was using a custom OS, but Ubuntu isn't so uncommon.  At any
rate I thought I would point this out to anyone who was thinking of using
Ubuntu on this laptop --- it won't necessarily work 100% out of the box.

## The Ugly

By far the most serious issue is that the laptop is not sturdy enough for
everyday use.  Holding my laptop on the right side causes it to freeze.  When
this happens I have not been able to find any remedy except a hard reboot.  I
am not really sure what the cause of this issue is, but I suspect that holding
the laptop in this way is putting too much stress on the motherboard and
something is shorting or browning out.  This may not be an issue for all (or
even most) Librem laptops, but it is nevertheless indicative that there is not
sufficient quality control in their build.

{% 
    include image name="librem-hold.jpg"
    caption="Holding the Librem 13 like this causes it to freeze.  Once this
    happens the only way out is a hard reboot."
%}

I cannot recommend the Librem 13 for this issue alone.  I have been able to
continue working with mine because I've learned how to hold it, but I can't
hand it to anyone else because there's a good chance that they would hold it
wrong and cause it to freeze.

A second serious issue that I have come across has to do with the thermal
controls.  Occasionally the CPU fan starts to run at 100% while the laptop is
sitting idle.  After about a minute of this the laptop starts to run very
slowly and after about another minute it freezes entirely.  I suspect that a
bug in the thermal controls is causing the firmware to think that the CPU is
overheating and is throttling the CPU until it cools down.  But because the CPU
was never hot to begin with this never happens.  Again the only remedy is a
hard reboot.

When I originally got this laptop this would happen about once a week or so,
but after I disabled `thermlad` in Ubuntu the frequency of this problem
decreased dramatically.  Now it only happens once every month or two.  I can't
say for sure whether or not Purism is to blame for this issue since I don't
know whether it occurs in PureOS as well.  It could be due to some strange
interaction between Ubuntu and the Librem firmware.

Lastly I have occasionally run into an issue where the laptop screen fails to
turn on when I open the laptop.  Again I have been able to find a workaround
when this happens other than to do a hard reboot.

## It could have been wonderful

This laptop feels very close to being amazing.  If the build issues were
addressed, all I really have are a few annoyances, and many of these don't seem
like they are too hard to fix.  (Though having worked around people doing antenna
design, the antenna issues may be more difficult to improve.)  But as it is
this laptop is just not there yet.

Purism is no longer selling the Librem 13 in favor of the Librem 14, so perhaps
some of these issues have been addressed in the new product.  (The larger size
will probably improve the antenna performance at the very least.)  But if I
were buying a new laptop today I'm sad to say that I don't think I would risk
it.

[1]: https://www.pureos.net/

[2]: https://puri.sm/coreboot/

[3]: https://puri.sm/posts/librem-now-most-secure-laptop-under-full-user-with-tamper-evident-features/

[4]: https://puri.sm/products/librem-14/
