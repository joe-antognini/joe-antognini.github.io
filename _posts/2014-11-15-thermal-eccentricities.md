---
layout: post
title: The thermal eccentricity distribution
date: 2014-11-15
categories: astronomy
image:
  feature: constellations3.jpg
---

One of the most beautiful results in dynamics is the thermal eccentricity
distribution.  Suppose we have a population of binary stars which is, in
some sense, "thermalized."  That is, these binaries have all interacted with
each other and exchanged energy many times and have reached statistical
equilibrium.  We would like to know what these binaries look like.  In
particular we would like to know the distribution of their periods and
eccentricities.  The derivation of this result is due to the British
astronomer J. H. Jeans in a [1919 paper][1] and this post loosely follows
Jeans's derivation.  I have updated some of the notation, simplified the
derivation somewhat, and provided some motivation behind Jeans's sometimes
cryptic coordinate transformations.

It is clear from the outset that the problem as we have posed it has a small
issue.  It is not obvious that there is any statistical equilibrium that can
be reached at all.  When these binaries interact, it seems that some of them
will dissociate and others of them will form triples.  So a thermalized
population of binaries won't be a population of binaries at all, but a
population of binaries mixed with single stars and triples (and given that
these objects will all interact with each other, there will also be higher
order systems as well).  If this is the case, then there can be no such
thing as a thermal population of binaries.  This objection turns out to be
valid because a population of binaries will naturally form single and triple
systems.  But we will here make a small swindle and suppose that such a
thermalized population of binaries exists.  This population need not have to
have come about naturally, but we can imagine that it was instead created ab
initio and then ask what its properties will be knowing that there is
equipartition of energy.  We should not object to this swindle too much
because Jeans is already notorious for a far greater swindle.  Moreover, we
will find that, having made this swindle, the distribution of eccentricities
takes a remarkably simple form and the distribution of periods validates the
very objection we had raised!  

So let's begin.  By assumption, we have a population of binaries which is
thermalized.  This is to say that the distribution of energies follows a
Boltzmann distribution:

$$f \sim \exp \left( -\frac{E}{T} \right),$$

where $$T$$ is some measure of the thermal content of the system.  Now, the
energy of an individual binary system is

$$E = \frac{1}{2} \mu v^2 - \frac{G M \mu}{r},$$

where $$r$$ and $$v$$ are the relative distance and velocity, respective,
$$M$$ is the total mass of the system, and $$\mu$$ is the reduced mass of
the system,

$$\mu \equiv \frac{m_1 m_2}{M}.$$

The total number of systems in a differential element of phase space, $$d
\tilde{V}$$, is

$$f \, d\tilde{V} \sim \exp \left[ \frac{1}{T} \left( \frac{1}{2} \mu
(\dot{x}^2 + \dot{y}^2 + \dot{z}^2) - \frac{G M \mu}{r} \right) \right]
d\dot{x} \, d\dot{y} \, d\dot{z} \, dr \, r^2 \, d\Omega,$$

where $$d\Omega$$ is a differential solid angle.  It helps if we decompose
the velocity into its radial and tangential components: 
$$v^2 = \dot{r}^2 + \tau^2$$.  We can pick $$\dot{r}$$ to be along the 
$$z$$ direction, in which case we have $$dx \, dy = \tau \, d\tau \,
d\phi$$, where $$\phi$$ is an azimuthal angle.  Now, integrating over
$$\Omega$$ and $$\phi$$, which gives us a factor of $$4\pi$$ and $$2\pi$$,
respectively, we get

$$f \, d\tilde{V} \sim 8 \pi^2 \exp \left[ \frac{1}{T} \left( \frac{1}{2}
\mu (\dot{r}^2 + \tau^2) - \frac{G M \mu}{r} \right) \right] d\dot{r} \,
\tau \, d\tau \, r^2 \, dr.$$

We so far have been using real, physical coordinates to describe the
binaries.  But what we would like is to transform this distribution function
into a set of coordinates which represent the overall properties of the
binary, like its specific energy and angular momentum.  As it turns out,
using the angular momentum itself complicates the derivation quite a bit and
the inverse of the angular momentum is the better coordinate to use.  So we
have two new coordinates:

$$E = \frac{1}{2} \left( \dot{r}^2 + \tau^2 \right) - \frac{G M}{r},$$

$$k \equiv \frac{1}{r \tau}.$$

The shape of an orbit is fully determined by its energy and angular momentum
(recall that we have already integrated over all possible orientations).  We
are therefore missing only one coordinate, namely a phase angle specifying
where the stars are in their orbits.  For this purpose we use the true
anomaly, $$\theta$$, which is related to $$r$$ by

$$\frac{1}{r} = GMk^2 \left( 1 + \frac{A}{GM \mu^2} \cos \theta \right)$$

where $$A$$ is the magnitude of the Runge-Lenz vector:

$$A = GM\mu^2 e.$$

We may rewrite the equation for the true anomaly in this simple form:

$$\frac{A k}{\mu^2} \cos \theta = \tau - \frac{GM}{r \tau}.$$

To make this transformation we need to calculate the determinant of the
Jacobian.  Thanks to Jeans's judicious choice of coordinates, this turns out
to be simple by noting that neither $$k$$ nor $$\theta$$ depend on
$$\dot{r}$$, so

$$\left| \frac{ \partial(E, k, \cos \theta)}{\partial(\dot{r}, \tau, r)}
\right| = \frac{\partial E}{\partial \dot{r}} 
\left| \begin{array}{cc}
\frac{\partial k}{\partial r} & \frac{\partial k}{\partial \tau} \\
\frac{\partial \cos \theta}{\partial r} & \frac{\partial \cos
\theta}{\partial \tau} \\ 
\end{array} \right| 
= \frac{\mu^2 \dot{r}}{A k r^2 \tau}.$$

This implies that the volume element transforms as

$$d\dot{r} \, d\tau \, dr = \frac{Ak \tau r^2}{\mu^2 \dot{r}} \, dE \, dk \,
d \cos \theta.$$

Writing the old, physical coordinates in terms of the new ones, we have

$$\tau = \frac{Ak}{\mu^2} \cos \theta + GMk, \qquad r =
\frac{\mu^2}{k^2 (A \cos \theta + GM \mu^2)},$$

and

$$\dot{r} = \sqrt{2E + (GMk)^2 - \left( \frac{Ak}{\mu^2} \right)^2 \cos^2
\theta}.$$

Now recall the relationship between the magnitude of $$A$$ and the energy
and angular momentum:

$$A^2 = (GM)^2 \mu^4 + 2 E l^2 \mu^4.$$

This means that we can rewrite $$\dot{r}$$ as

$$\dot{r} = \left( \frac{Ak}{\mu^2} \right) \sqrt{1 - \cos^2 \theta} =
\left( \frac{Ak}{\mu^2} \right) \sin \theta.$$

Putting all this into the distribution function, we find

$$f \, d\tilde{V} \sim 8 \pi^2 \exp \left( -\frac{E}{T} \right)
\frac{\mu^4}{(A \cos \theta + G M \mu^2)^2 \sin \theta} d \cos \theta
\frac{dk}{k^6} dE.$$

We can now integrate this over $$\theta$$ to get the distribution function
in terms of the variables we wanted all along---the energy and angular
momentum.

$$f \, d\tilde{V} \sim 8 \pi^2 \exp \left( -\frac{E}{T} \right)
\int_0^{2\pi} \frac{\mu^4}{(A \cos \theta + G M \mu^2)^2} d\theta
\frac{dk}{k^6} dE.$$

After performing the integral we find the distribution function to be

$$f \, d\tilde{V} \sim 16 \pi^3 \exp \left( -\frac{E}{T} \right) \frac{GM
\mu^6}{ \left[ (GM \mu^2)^2 - A^2 \right]^{3/2}} \frac{dk}{k^6} dE.$$

Here things start to simplify dramatically.  First, note that $$A$$ is
related to the eccentricity by 

$$A = GM\mu^2 e.$$

Substituting into the distribution to rid ourselves of $$A$$ forever, we get

$$f \, d\tilde{V} \sim 16 \pi^3 \exp \left( -\frac{E}{T} \right)
\frac{1}{(1-e^2)^{3/2}} \frac{dk}{k^6} \frac{dE}{(GM)^2}.$$

Of course, we're not so much interested in the distribution of angular
momenta as we are in the distribution of eccentricity.  So now that the
distribution is fairly simple, let's change coordinates once more, this time
moving from $$k$$ to $$e$$.  The two are related by

$$k = \frac{\sqrt{2E}}{GM} \frac{1}{(1 - e^2)^{1/2}}, \qquad 
\frac{\partial k}{\partial e} = \frac{\sqrt{2E}}{GM} \frac{e}{(1 -
e^2)^{3/2}}.$$

When we make this coordinate transformation we find that the distribution
function has simlpified dramatically to

$$f \, d\tilde{V} \sim 16 \pi^3 \exp \left( -\frac{E}{T} \right)
\frac{(GM)^3}{(2E)^{5/2}} dE \, e \, de$$

The eccentricity dependence of the distribution function is contained
entirely in the term $$e \, de$$ and is independent of the energy.  We may
therefore write the distribution function in terms of the eccentricity alone
as

$$f(e) \, de = 2e \, de,$$

where we have now properly normalized $$f$$.  After all our work, this is
our grand result---the thermal eccentricity distribution.  If a population
of binaries has thermalized, the eccentricities will be distributed linearly
and nearly circular orbits will be rare.  In fact, the median eccentricity
of this distribution is $$1/\sqrt{2}$$.

Let us turn now to the energies of the binaries.  Here the result seems
elegant:

$$f(E) \, dE \sim \frac{1}{(2E)^{5/2}} \exp \left( - \frac{E}{T} \right) \,
dE$$

However, when we try to normalize this distribution function we encounter a
problem---it diverges as $$E \to 0$$ and as $$E \to -\infty$$.  This result
would appear to contradict our entire analysis---a thermal population of
binaries cannot exist at all!  And indeed, this is the case.  The divergence
of this distribution function at both limits is a direct consequence of
Heggie's law.  Heggie's law, first stated in the [dense monograph][2] on
three-body dynamics by the British astronomer Douglas Heggie, states that in
general, when a passing star interacts with a soft binary (i.e., a binary
whose binding energy is less than the kinetic energy of the incoming star),
the binary will tend to become softer and when a passing star interacts with
a hard binary (i.e., a binary whose binding energy is greater than the
kinetic energy of the incoming star), the binary will tend to become harder.
This means that if we start with a population of binaries of all different
sizes and moving with a variety of velocities, after many interactions, the
hard binaries will have hardened indefinitely (they will have $$E \to
-\infty$$) and the soft binaries will have softened indefinitely (i.e.,
disrupted).  So our inability to normalize the distribution function
actually fits in quite well with our understanding of dynamics. 

Unfortunately Jeans predated the discovery of Heggie's law by many decades,
so he was unable to interpret the energy distribution as easily as us.
Jeans nevertheless noted three conclusions from his derivation:

1. "There would be no correlation between period and eccentricity."

2. "The eccentricities would be distributed according tot he law $$2e \,
de$$---in other words, all values of $$e^2$$ would be equally likely."

3. "The periods would conform to the law of distribution."

Jeans then compared these results with the observations available to him in
1919 to see how thermalized the population of binaries that had been
observed was.  It is obvious from the distribution of energies that the
binaries cannot be thermalized.  But it is possible (and indeed it is the
case) that the eccentricities could thermalize before the energies.
Nevertheless, the sample of binaries Jeans uses do not follow a thermal
eccentricity distribution---there is a deficit binaries with eccentricities
above 0.6.  Moreover, the sample of binaries also exhibits a strong
correlation between period and eccentricity.  Jeans therefore concludes that
binaries have not yet thermalized, and so the distribution of their orbital
parameters must provide information about their formation.

Jeans's sample (which he draws from [_The Binary Stars_][3] by Robert
Aitken) was not ideal.  It's small (87 stars) and biased.  How does a modern
sample hold up?  An excellent overview of the properties can be found in the
review by [Duchene & Kraus (2013)][4].  In short period binaries the
eccentricities are almost all very low due to tidal circularization.  In
longer period binaries ($$P \gtrsim$$ 100 days) the eccentricity
distribution is consistent with flat, although there appears to be a dearth
of systems at very high eccentricities.  At any rate, modern samples confirm
Jeans's original observation that binaries in the field do not appear to be
thermalized.  Nevertheless, the modern samples do not find a correlation
between eccentricity and period aside from the circularization of very short
period binaries already mentioned.  

It is not very surprising that binaries in the field do not exhibit a
thermal eccentricity distribution because even over the lifetime of the
Galaxy nearly all binaries have not had time to interact with each other
even once.  In a more compact system like a globular cluster we would expect
the system to be more thermalized because the binaries would have many
opportunities to interact with one another.  Unfortunately it is generally
difficult to measure the orbital properties of binaries in globular
clusters---even getting an accurate measurement of the binary fraction has
proven to be difficult.  It is possible to get accurate orbital periods from
millisecond pulsars and these seem to show a bias towards circular orbits.
But it is reasonable to believe that millisecond pulsars represent a special
case because the partner would necessarily have to be very close to the
neutron star to spin it up and therefore a bias towards circular orbits
would be expected.  Without observations, we have to resort to numerical
simulations, which seem to indicate that binaries in globular clusters
should exhibit a thermal eccentricity distribution, but this cannot be
concluded too definitely because it is standard for numerical simulations to
begin with a thermal eccentricity distribution.  Nevertheless it is a good
confirmation of the theory that the thermal eccentricity distribution is
maintained.

The thermal eccentricity distribution was also derived by the
Soviet-Armenian astronomer [Victor Ambartsumian in 1937][5] and we have a
separate post about his derivation [here][6].  Ambartsumian's derivation is
more general and shows that the same eccentricity distribution can occur
even if the binaries are not thermalized.  For this reason the thermal
eccentricity distribution is sometimes referred to as the Ambartsumian
distribution instead. 

[1]: http://adsabs.harvard.edu/abs/1919MNRAS..79..408J
[2]: http://adsabs.harvard.edu/abs/1975MNRAS.173..729H
[3]: http://adsabs.harvard.edu/abs/1918bist.book.....A
[4]: http://adsabs.harvard.edu/abs/2013ARA&A..51..269D
[5]: ../../papers/ambartsumian37.pdf
[6]: ../../classics/ambartsumian-distribution
