---
layout: post
title: The Ambartsumian distribution
date: 2014-12-2
categories: classics
image:
  feature: constellations3.jpg
---

In our look at [Jeans's 1919 paper][1] in [this post][2] we derived the
eccentricity distribution of a population of thermalized binaries.  Recall
that we assumed that the binaries obeyed equipartition of energy and then
showed that the eccentricity distribution must follow the law

$$f(e) = 2e \: de.$$

After deriving this law, Jeans compared this to the eccentricity
distribution of known binaries and did not find a satisfactory fit.  In
particular, Jeans noted that although the observed eccentricity distribution
appears to somewhat match the above distribution at lower eccentricities,
there is a substantial deficit of high eccentricity binaries.  

By the mid-1930s Hubble's law and the expansion of the Universe had been
discovered and had added new data to the important question of the age of
the Universe.  The newly measured Hubble constant could was used to estimate
the age of the universe as about $$10^{10}$$ years old.  Jeans, however,
argued that if equipartition of energy were to be reached for binary
systems, the universe would have to be at least $$10^{13}$$ years old.  Thus
an open question in astronomy at the time was whether the "short timescale"
or the "long timescale" was correct.  

By this point, measurements of the orbital parameters of more binary systems
led Jeans to reexamine the question of whether binaries were thermalized.
With a larger (though still biased) sample, Jeans found a good agreement
with the thermal eccentricity distribution for eccentricities less than 0.6,
but poor agreement for larger eccentricities.  Jeans argued that the
discrepancy at high eccentricities was due to selection effects --- it is in
general difficult to measure the eccentricities of and discover high
eccentricity binaries.  With this new data, Jeans concluded that
equipartition of energy was observed, which implied the long timescale.

The Soviet-Armenian astronomer Victor Ambartsumian published a paper in
1937, [On the Statistics of Double Stars][3], in which he pointed out an
important flaw in Jeans's reasoning.  In a nutshell, Jeans's fallacy was to
affirm the consequent.  Jeans showed that a thermalized population of
binaries should obey the above eccentricity distribution and argued that
because this distribution is observed, binaries must be thermalized.  But
Ambartsumian demonstrated that the above eccentricity distribution will be
produced under a wide variety of conditions, so it does not follow that the
population of binaries has thermalized if the thermal eccentricity
distribution is observed. 

(A bibliographic note: the paper was originally written in Russian and it is
hard to find an original copy.  D.  W. Goldsmith translated it and a copy is
hosted on Douglas Heggie's website [here][4].)

### Deriving eccentricity distributions the easy way

In our post on Jeans's paper we took a somewhat intuitive, but nevertheless
long path to derive the simple thermal eccentricity distribution.
Ambartsumian discovered a much simpler and more general derivation.

We began our derivation of the thermal eccentricity distribution by
supposing that the number distribution follows the Boltzmann distribution:

$$dN \sim \exp \left(-\frac{E}{T} \right) \, dx \, dy \, dz \, dp_x \, dp_y
\, dp_z.$$

But recall that nowhere in our derivation did the Boltzmann factor actually
play a role.  In fact, we shall now show that we derive the same result if
we just assume that the number density depends only on the energy:

$$dN \sim f(E) \, dx \, dy \, dz \, dp_x \, dp_y \, dp_z,$$

where $$f(E)$$ is an arbitrary function.  To now transform this distribution
to a coordinate system that involves eccentricity we will make a canonical
transformation rather than the ad hoc transformations that Jeans employed.
When studying orbits, one of the most convenient canonical coordinate
systems to use is the Delaunay elements: the mean anomaly, $$l$$; the
argument of periastron, $$g$$; and the longitude of ascending node, $$h$$.
Their corresponding conjugate momenta are:

$$L = \mu \sqrt{GMa},$$

$$G = L \sqrt{1 - e^2},$$

and

$$H = G \cos i,$$

where $$\mu$$ is the reduced mass, $$M$$ is the total mass, $$a$$ is the
semi-major axis, and $$i$$ is the inclination relative to a reference
plane.

Since we are making a canonical transformation, we don't have to do any
work --- phase space volume is conserved:

$$dx \, dy \, dz \, dp_x \, dp_y \, dp_z = dl \, dg \, dh \, dL \, dG \,
dH.$$

Now the energy is given by

$$E = -\frac{GM \mu}{2a},$$

which can be written in terms of the Delaunay elements as

$$E = -\frac{\mu}{2} \left( \frac{GM\mu}{L} \right)^2.$$

Thus the energy depends only on $$L$$.  We can then write the distribution
as

$$dN = f(L) \, dl \, dg \, dh \, dL \, dG \, dH.$$

We can now start integrating out the dependence of all variables except for
$$L$$ on $$N$$.  The canonical coordinates are easy because they are just
angles that vary from 0 to $$2\pi$$, so the integral of each one of them
yields a factor of $$2 \pi$$.  As for the conjugate momenta, note that $$H$$
varies from 0 to $$G$$ and $$G$$ varies from 0 to $$L$$.  Furthermore, if we
want the number of systems with an eccentricity less than some value
$$e^{\prime}$$, we want the values of $$G$$ that are greater than some
corresponding $$G^{\prime}$$.  This gives us

$$N(e < e^{\prime}) = 8 \pi^3 f(L) \, dL \, \int_{G^{\prime}}^L \, dG \,
\int_0^G \, dH.$$

These integrals become

$$N(e < e^{\prime}) = 4 \pi^3 f(L) (L^2 - G^{\prime \, 2}) \, dL.$$

Now, remember that $$G = L \sqrt{1 - e^2}$$, so 

$$L^2 - G^{\prime \, 2} = L^2 e^{\prime \, 2}.$$

We therefore have that the eccentricity distribution is

$$N(e < e^{\prime}) = 4 \pi^3 e^{\prime \, 2} \, \int_0^{\infty} f(L) \, L^2
\, dL.$$

This last integral is not dependent on $$e$$ and so is just a constant.
Note, however, that depending on our choice of $$f(L)$$, it might not
converge.  (This was what happened when we took it to be the Boltzmann
factor.)

This derivation of the eccentricity distribution is much simpler and much
more general.  Because the assumption that the binaries are thermalized is
not required to obtain this distribution, it is often called an Ambartsumian
distribution instead of the thermal eccentricity distribution.

From this result Ambartsumian concluded that even if the observed
eccentricity distribution of binaries matched this distribution, one would
be unable to conclude that the binaries actually obeyed equipartition of
energy.  Ambartsumian ended his paper with a few other arguments against
Jeans.  Ambarstumian pointed out what we mentioned in our original post on
the thermal eccentricity distribution that over time the binaries will
dissociate so the presence of as many binaries as are observed is strong
evidence against thermalization.  Ambartsumian also performed a careful
calculation of the relaxation time of binaries in the Galaxy and estimated
that binaries with semi-major axes of around $$10^4$$ AU would have a
relaxation time of $$5 \times 10^9$$ years, far shorter than the timescale
of $$10^{13}$$ years that Jeans advocated.

[1]: http://adsabs.harvard.edu/abs/1919MNRAS..79..408J
[2]: ../../classics/thermal-eccentricities
[3]: ../../papers/ambartsumian37.pdf
[4]: http://www.maths.ed.ac.uk/~douglas/Ambartsumian1937001.pdf 
