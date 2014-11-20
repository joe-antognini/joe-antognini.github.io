---
layout: post
title: Apples in a spacecraft
date: 2014-11-20
categories: classics
---

A contribution to a retrospective series on the work of the French
dynamicist Michel Henon by Scott Tremaine inspired me to do a review of an
interesting puzzle in dynamics.

The puzzle goes as follows.  Suppose we are in a spacecraft orbiting the
Earth in a circular orbit.  The spacecraft is rotating such that the same
side of the spacecraft always points toward the Earth.  That is, its
rotation period is equal to its revolution period, just like the Moon's.
Now we release a bushel of apples inside the spacecraft so that they are
floating all around us.  How will the apples be distributed in the
spacecraft after a long time?  We will assume that they are real apples, so
they are inelastic and they are not massive enough for self-gravitation to
be noticeable.  

This question was originally posed by Alfven, but he derived the wrong
answer.  The correct answer was derived by Henon in a short 1978 note.
Henon found that half the apples will end up on the floor of the spacecraft
and half will end up on the ceiling.  (For simplicity, we'll call the side
of the spacecraft closer to Earth the floor, and the other side the
ceiling.)

To see how this answer comes about, consider an apple which starts out
closer to the Earth than the center of mass of the spacecraft.  It is on an
orbit with a slightly smaller radius than the spacecraft, so its orbital
velocity is larger.  Over time, it will drift forward in the spacecraft
until it hits the front wall.  This collision is inelastic, so the apple
will lose energy and its orbit will shrink.  This means that it will drift
slightly towards the floor of the spacecraft and drift even faster towards
the front of the spacecraft for the next collision.  Over time, the apple
will continually collide with the front wall of the spacecraft, losing
energy, and will end up on the floor of the spacecraft.

As for an apple which starts out farther from the Earth than the center of
mass of the spacecraft, it will undergo the opposite process.  Because it is
farther from the Earth, it's orbit has a larger radius and so its orbital
speed is slower than that of the spacecraft.  The apples on the upper half
of the spacecraft will therefore drift backwards to the rear wall of the
spacecraft.  There it will collide with the wall and gain energy because the
spaceship is moving faster.  Since a more energetic orbit has a larger
radius, the apple will slowly drift up towards the ceiling of the
spacecraft.  Thus over time the apple population will bifurcate with the
apples that began closer to the floor collecting on the floor towards the
front of the spacecraft and the apples that began closer to the ceiling
collecting on the ceiling towards the back of the spacecraft. 

How long will it take this process to occur?  If we assume that the apples
are extremely inelastic so that there are not too many collisions, then the
timescale will be of the order of the time it takes the apple to drift to
one end of the spacecraft.  Now, the orbital velocity of the center of
mass of the spacecraft is (assuming the spacecraft is in low Earth orbit)

$$v = \sqrt{\frac{GM\_{\bigoplus}}{R\_{\bigoplus}}},$$

where $$R$$ is the radius of the center of mass of the spacecraft from the
center of the Earth.  If an apple is some small distance $$\Delta R$$ closer
to the Earth than the center of mass of the spacecraft, then its velocity
will be

$$v + \Delta v = \sqrt{\frac{GM\_{\bigoplus}}{R + \Delta R\_{\bigoplus}}.$$

Assuming that $$\Delta R / R \ll 1$$, we have

$$\frac{\Delta v}{v} \simeq \frac{\Delta R}{2 R\_{\bigoplus}}.$$

The drift time is then

$$t = \frac{\Delta R}{\Delta v} = 

If we have a fairly spacious spacecraft that is 10 meters by 10 meters by 10
meters
