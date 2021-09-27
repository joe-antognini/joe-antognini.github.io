---
layout: post
title: How would you detect a comet that would impact the Earth?
date: 2021-09-26
categories: astronomy
image:
  feature: constellations3.jpg
---

A [clip][1] from a new star-studded satire, Don't Look Up just came out.  The
premise of the movie is that an astronomer discovers that a comet about 5 to 10
kilometers across is going to impact the Earth and has to convince a skeptical
government about the imminant peril.  The movie hasn't come out yet,
but it got me to thinking what such a discovery would look like.  (Specifically
the scientific details of such a discovery, not the social and political
ramifications.)

## How bright would this comet be?

As one of my professors liked to say, observing objects in the Solar System is
hard to the fourth power.  Most sources we observe in astronomy like stars and
galaxies emit their own light.  Their observed brightness here on Earth obeys
the inverse square law.  If two objects have the same intrinsic luminosity but
one is twice as distant as the other, we will receive one-fourth the light as
the more distant one.  This makes observing distant objects not just hard, but
hard squared!

But objects in the Solar System are even worse because they don't emit their
own light --- they reflect light that originates from the Sun.  Thus we have to
deal with the inverse square law *twice* --- once for the light going from the
Sun to the object, and then a second time from the light going from the object
to us on Earth.  So for Solar System objects, the observed brightness varies as
$1 / r^4$.  An object twice as distant will be 16 times fainter!

Another factor to consider when observing Solar System objects is their albedo
--- the fraction of light that their surface reflects.  One of the challenges
with observing comets is that their appearance changes dramatically over the
course of their orbit.  When they are far from the Sun, only the nucleus is
present.  Unfortunately, the albedo of a cometary nucleus is exceedingly low,
of order $\sim$0.04.  (By comparison, asphalt has an albedo of about 0.07.)

But comets are more complicated objects than the $1 /r^4$ law would predict.
As the comet gets closer to the Sun, its surface starts to heat up and
sublimate gas off of the nucleus, forming a coma.  This coma is far more
reflective than the nucleus so the comet can suddenly increase dramatically in
brightness over a very short time period.  In 2007, [Comet Holmes][2] increased
from magnitude 17 to 2.8 in just 42 hours, an increase by a factor of
$\sim$500,000.

Nevertheless, let's assume that the comet was discovered far enough away that
there was no appreciable coma.  How far away could such an object be observed,
at least in principle?



## How would you detect that the object is a comet?

So at a distance of TODO, we could at least see the object as a faint dot on an
image.  But images of the sky are almost nothing but faint dots and the vast
majority of these faint dots are stars.  How would we know that this particular
faint dot is a comet?  The trick


## How would you know that the comet was going to hit the Earth?

In principle, we only need two images to establish that the object is in the
Solar System.  But this is not enough to determine that the object is a threat
to the Earth.  How much more data would we need for this?  Surprisingly,
perhaps, you would only need a single additional image, or three in total,
to uniquely determine the orbit of the object.

How can this be?  The orbit of any object in the Solar System has six degrees
of freedom: three position coordinates $(x, y, z)$, and three velocity
coordinates, $(v_x, v_y, v_z)$.  Each image provides you with a location on the
sky, which has two degrees of freedom, 
 so
with three images you get six independent constraints on the coordinates of the
object and can fix the trajectory of the object. [^1]  Of course, going from
the locations on the sky to an orbit 

As always, however, there are more details than the textbook answer.  We can
never any quantity with perfect precision, and particularly when the object is
distant, small uncertainties in the observed location of the object on the sky
can result in a huge uncertainty in the orbit of the object.

### How much does the comet move in the images?

### Going from dots on the sky to orbital parameters

## How much time would we have?

## Postscript: What could we do?

As I mentioned at the beginning, the movie hasn't come out yet but from the
trailer it looks like they're sending up a space shuttle.  Maybe they're going
to detonate a nuclear bomb on the comet or something like in Armageddon.  

One of the general principles here is that the sooner you do something like
this, the better.

## Footnotes

[^1]: You might wonder if there are any degenerancies here.  TODO

[1]: https://www.youtube.com/watch?v=Op_v2PHDn-0

[2]: https://en.wikipedia.org/wiki/Comet_Holmes
