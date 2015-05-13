---
layout: post
title: Understanding the modes of mass transfer in binary stars
date: 2015-05-07
categories: toolkit
image:
  feature: constellations3.jpg
---

Suppose we have a pair of stars orbiting each other in a binary system.
Each star has a [Rcohe lobe][1], beyond which matter is not gravitationally
bound to the star.  What happens if one of the stars grows larger than its
Roche lobe?  Since this material is no longer bound to the original star it
is clear that mass will be lost from the original star and it is likely that
the secondary will accrete some or all of the matter.  But over what
timescale will this mass transfer take place?  This is the queston addressed
in Section 3.3 of the wonderfully thorough book [Evolutionary Processes in
Binary and Multiple Stars][2] by Peter Eggleton.  Although the detailed
answer to this question is quite involved, the qualitative picture is
enlightening, so I will summarize it here.  To keep things simple, in this
note I am just going to concern myself with conservative mass transfer.
This means that no mass or angular momentum is lost in the system --- any
mass lost from star 1 is accreted by star 2. 

## Timescales

As with any process in astronomy it is instructive to examine the timescales
in the problem.  In this case there are three relevant timescales.  In order
of decreasing time:

1. The **nuclear timescale**.  This is the evolutionary timescale of an
isolated star.  As the star evolves the composition of the core changes due
to nuclear burning.  These composition changes lead to changes in the
luminosity of the star, and ultimately, its radius.  The nuclear timescale
is the time for the star to change its core composition by a factor of order
unity.  For a Sun-like star the nuclear timescale is ~10 Gyr.
  
2. The **thermal timescale**.  Also known as the [Kelvin-Helmholtz
timescale][3], this is the time for the star to lose energy due to
gravitational contraction.  For a Sun-like star the thermal timescale is ~10
Myr. 
  
3. The **hydrodynamic timescale**.  This is the timescale for a star which
has exceeded its Roche lobe to return to the Roche lobe.  This timescale can
be estimated by using Bernoulli's equation to calculate the mass flow
through the first Lagrange point by modeling the mass transfer as flow
through a cylindrical pipe.  It is difficult to calculate the hydrodynamic
timescale exactly, but it is of order the dynamical time of the star (i.e.,
the sound crossing time).  For a Sun-like star the hydrodynamic timescale is
~1 hour.

## The radius-mass relationship

[1]: https://en.wikipedia.org/wiki/Roche_lobe
[2]: http://adsabs.harvard.edu/abs/2006epbm.book.....E
[3]: https://en.wikipedia.org/wiki/Kelvin%E2%80%93Helmholtz_mechanism
