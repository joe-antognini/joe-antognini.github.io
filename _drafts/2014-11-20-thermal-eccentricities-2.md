---
layout: post
title: The Thermal Eccentricity Distribution, Part II
date: 2014-11-20
categories: classics
image:
  feature: constellations3.jpg
---

In our look at [Jeans's 1919 paper][1] in [this post][2] we derived the
eccentricity distribution of a population of thermalized binaries.  Recall
that we assumed that the binaries obeyed equipartition of energy and then
derived that the eccentricity distribution must follow the law

$$f(e) = 2e \: de.$$

After deriving this law, Jeans compared the eccentricity distribution of
known binaries to it and did not find a satisfactory fit.  In particular,
Jeans noted that although the observed eccentricity distribution appears to
somewhat match the above distribution at lower eccentricities, there is a
substantial deficit of high eccentricity binaries.  

By the mid-1930s Hubble's law and the expansion of the Universe had been
discovered and had added new data to the important question of the age of
the Universe.  The newly measured Hubble constant could was used to estimate
the age of the universe as about $$10^{10}$$ years old.  Jeans, however,
noted that if equipartition of energy were to be reached for binary systems,
the universe would have to be at least $$10^{13}$$ years old.  Thus a major
open question in astronomy at the time was whether the "short timescale" or
the "long timescale" was correct.  

By this point, measurements of the orbital parameters of more binary systems
lead Jeans to reexamine the question of whether binaries were thermalized.
With a larger (though still biased) sample, Jeans found a good agreement
with the thermal eccentricity distribution for eccentricities less than 0.6,
but poor agreement for larger eccentricities.  Jeans argued that the
discrepency at high eccentricities was due to selection effects --- it is in
general difficult to measure the eccentricities of and discover high
eccentricity binaries.  With this new data, Jeans concluded that
equipartition of energy was observed, which implied the long timescale.

The Soviet-Armenian astronomer Victor Ambartsumian published a paper in
1937, [On the Statistics of Double Stars][3] in which he pointed out an
important flaw in Jeans's reasoning.  In a nutshell, Jeans's fallacy was to
affirm the consequent.  Jeans showed that a thermalized population of
binaries should obey the above eccentricity distribution and argued that
because this distribution is observed, binaries must be thermalized.  But
Ambartsumian demonstrated that the above eccentricity distribution will be
produced under a wide variety of conditions, so it does not follow that the
population of binaries has thermalized if the thermal eccentricity
distribution is observed. 

### Deriving eccentricity distributions the easy way

In our post on Jeans's paper we took a somewhat intuitive, but nevertheless
long path to derive the simple thermal eccentricity distribution.
Ambartsumian discovered a much simpler and more general distribution.

We began our derivation of the thermal eccentricity distribution by
supposing that the number distribution follows the Boltzmann distribution:

$$dN \sim \exp \left(\frac{E}{T} \right) \, dx \, dy \, dz \, dp_x \, dp_y
\, dp_z.$$

But recall that nowhere in our derivation did the Boltzmann factor actually
play a role.  In fact, we shall now show that we derive the same result if
we just assume that the number density depends only on the energy:

$$dN \sim f(E) \, dx \, dy \, dz \, dp_x \, dp_y \, dp_z,$$

where $$f(E)$$ is an arbitrary function.  To now transform this distribution
to a coordinate system that involves eccentricity we will make a canonical
transformation rather than the ad hoc transformations that Jeans employed.
When studying orbits, one of the most convenient canonical coordinate
systems to use is the Delaunay variables: the mean anomaly, $$l$$; the
argument of periastron, $$g$$; and the longitude of ascending node, $$h$$.
Their corresponding conjugate momenta are:

$$L = \mu \sqrt{GMa},$$

$$G = L \sqrt{1 - e^2},$$

and

$$H = G \cos i,$$

where $$\mu$$ is the reduced mass, $$M$$ is the total mass, $$a$$ is the
semi-major axis, and $$i$$ is the inclination relative to a reference
plane.
