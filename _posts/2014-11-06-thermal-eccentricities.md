---
layout: post
title: The thermal eccentricity distribution
date: 2014-11-06
categories: classics
---

One of the most beautiful results in dynamics is the thermal eccentricity
distribution.  Suppose we have a population of binaries which is, in some
sense, "thermalized."  That is, these binaries have all interacted with each
other and exchanged energy many times and have reached statistical
equilibrium.  We would like to know what these binaries look like.
eccentricities is.  The derivation of this result is due to Jeans in a 1919
paper and this post loosely follows Jeans's derivation.

Now it is clear from the outset that the problem as we have posed it has a
small issue.  It is not obvious that there is any statistical equilibrium
that can be reached at all.  When these binaries interact, it seems that
some of them will dissociate and others of them will form triples.  So a
thermalized population of binaries won't be a population of binaries at all,
but a population of binaries mixed with single stars and triples (and given
that these objects will all interact with each other, there will also be
higher order systems as well).  If this is the case, then there can be no
such thing as a thermal population of triples.  This objection turns out to
be valid because a population of binaries will naturally form single and
triple systems.  But we will here make a small swindle and suppose that such
a thermalized population of binaries exists.  This population need not have
to have come about naturally, but we can imagine that it was instead created
ab initio and then ask what its properties will be knowing that there is
equipartition of energy.  We should not object to this swindle too much
because Jeans is already notorious for a far greater swindle.  Moreover, we
will find that, having made this swindle, the distribution of eccentricities
takes a remarkably simple form and the distribution of periods validates the
very objection we had raised!  

So let's begin.  By assumption, we have a population of binaries which is
thermalized.  This is to say that the distribution of energies follows a
Boltzmann distribution:

$$f \sim \exp \left( -\frac{E}{T} \right)$$

where $$\tau$$ is some measure of the thermal content of the system.  Now,
the energy of an individual binary system is

$$E = \frac{1}{2} \mu v^2 - \frac{G M \mu}{r}$$

where $$r$$ and $$v$$ are the relative distance and velocity, respective,
$$M$$ is the total mass of the system, and $$\mu$$ is the reduced mass of
the system,

$$\mu \equiv \frac{m1 m2}{M}.$$

The total number of systems in a differential element of phase space is

$$f d\dot{x} d\dot{y} d\dot{z} dr r^2 d\Omega \sim \exp \left[ \frac{1}{T}
\left( \frac{1}{2} \mu (\dot{x}^2 \dot{y}^2 \dot{z}^2) - \frac{G M \mu}{r}
\right) \right] d\dot{x} d\dot{y} d\dot{z} dr r^2 d\Omega$$

where $$d\Omega$$ is a differential solid angle.  It helps if we decompose
the velocity into its radial and tangential components --- $$v^2 = \dot{r}^2
+ \tau^2$$.  We can pick $$\dot{r}$$ to be along the $$z$$ direction, in
which case we have $$dx \, dy = \tau d\tau d\phi$$, where $$\phi$$ is an
azimuthal angle.  Now, integrating over $$\Omega$$ and $$\phi$$, which gives
us a factor of $$4\pi$$ and $$2\pi$$, respectively, we get

$$f d\tilde{V} \sim 8 \pi^2 \exp \left[ \frac{1}{T} \left( \frac{1}{2} \mu
(\dot{r}^2 + \tau^2) - \frac{G M \mu}{r} \right) \right] d\dot{r} \tau d\tau
r^2 dr$$

We so far have been using real, physical coordinates to describe the
binaries.  But what we would like is to transform this distribution function
into a set of coordinates which represent the overall properties of the
binary, like its specific energy and angular momentum.  As it turns out,
using the angular momentum itself complicates the derivation quite a bit and
the inverse of the angular momentum is the better coordinate to use.  So we
have two new coordinates:

$$E = \frac{1}{2} \left( \dot{r}^2 + \tau^2 \right) - \frac{G M}{r}$$

$$k \equiv \frac{1}{r \tau}$$

The shape of an orbit is fully determined by its energy and angular momentum
(recall that we have already integrated over all possible orientations).  We
are therefore missing only one coordinate, namely a phase angle specifying
where the stars are in their orbits.  For this purpose we use the true
anomaly, $$\theta$$, which is related to $$r$$ by

$$\frac{1}{r} = GMk^2 \left( 1 + \frac{A}{GM \mu^2} \cos \theta \right)$$,

where $$A$$ is the magnitude of the Runge-Lenz vector:

$$A = GM\mu^2 e$$.

We may rewrite the equation for the true anomaly in this simple form:

$$\frac{A k}{\mu^2} \cos \theta = \tau - \frac{GM}{r \tau}$$.

This turns out to be equivalent to

$$\sigma = \tau^2 \left( 1 - \frac{v\_{\textrm{circ}}^2}{\tau^2} \right)$$,

where $$v\_{\textrm{circ}}$$ is the velocity the star would have in a
circular orbit at that radius.  It is clear that at periastron $$\tau$$ is
going to be larger than $$v\_{\textrm{circ}}$$ giving a negative $$\sigma$$
and that at apastron $$\tau$$ will be smaller than $$v\_{\textrm{circ}}$$
giving a positive $$\sigma$$, so $$\sigma$$ will be a measure of the phase
angle of the orbit as we want.  

To make this transformation we need to calculate the determinant of the
Jacobian.  Thanks to Jeans's judicious choice of coordinates, this turns out
to be simple by noting that neither $$k$$ nor $$\sigma$$ depend on
$$\dot{r}$$, so

$$\left| \frac{ \partial(E, k, \sigma)}{\partial(\dot{r}, \tau, r)} \right|
= \frac{\partial E}{\partial \dot{r}} 
\left| \begin{array}{cc}
\frac{\partial k}{\partial r} & \frac{\partial k}{\partial \tau} \\
\frac{\partial \cos \theta}{\partial r} & \frac{\partial \cos
\theta}{\partial \tau} \\ 
\end{array} \right| 
= \frac{\mu^2 \dot{r}}{A k r^2 \tau}$$

This implies that the volume element transforms as

$$d\dot{r} d\tau dr = \frac{Ak \tau r^2}{\mu^2 \dot{r}} dE dk d \cos \theta$$.

Writing the old, physical coordinates in terms of the new ones, we have

$$\tau = \frac{Ak}{\mu^2} \cos \theta + GMk, \qquad r =
\frac{\mu^2}{k^2 (A \cos \theta + GM \mu^2)},$$

and

$$\dot{r} = \sqrt{2E + (GMk)^2 - \left( \frac{Ak}{\mu^2} \right)^2 \cos^2
\theta}.$$

Now recall the relationship between the magnitude of $$A$$ and the energy
and angular momentum:

$$A^2 = (GM)^2 \mu^4 + 2 E l^2 \mu^4$$.

This means that we can rewrite \dot{r} as

$$\dot{r} = \left( \frac{Ak}{\mu^2} \right) \sqrt{1 - \cos^2 \theta} =
\left( \frac{Ak}{\mu^2} \right) \sin \theta$$.

Putting all this into the distribution function, we find

$$f \sim 8 \pi^2 \exp \left( -\frac{E}{T} \right) \frac{\mu^4}{(A \cos
\theta + G M \mu^2)^2 \sin \theta} d \cos \theta \frac{dk}{k^6} dE$$.

We can now integrate this over $$\theta$$ to get the distribution function
in terms of the variables we wanted all along---the energy and angular
momentum.

$$f \sim 8 \pi^2 \exp \left( -\frac{E}{T} \right) \int\_0^{2\pi}
\frac{\mu^4}{(A \cos \theta + G M \mu^2)^2} d\theta \frac{dk}{k^6} dE$$.

After performing the integral we find the distribution function to be

$$f \sim 16 \pi^3 \exp \left( -\frac{E}{T} \right) \frac{GM \mu^6}{ \left(
(GM \mu^2)^2 - A^2 \right)^{3/2}} \frac{dk}{k^6} dE$$.

Here things start to simplify dramatically.  First, note that $$A$$ is
related to the eccentricity by 

$$A = GM\mu^2 e$$.

Substituting into the distribution to rid ourselves of $$A$$ forever, we get

$$f \sim 16 \pi^3 \exp \left( -\frac{E}{T} \right) \frac{1}{(1-e^2)^{3/2}}
\frac{dk}{k^6} \frac{dE}{(GM)^2}$$.

Of course, we're not so much interested in the distribution of angular
momenta as we are in the distribution of eccentricity.  So now that the
distribution is fairly simple, let's change coordinates once more, this time
moving from $$k$$ to $$e$$.  The two are related by

$$k = \frac{\sqrt{2E}}{GM} \frac{1}{(1 - e^2)^{1/2}}, \qquad 
\frac{\partial k}{\partal e} = \frac{\sqrt{2E}}{GM} \frac{e}{(1 -
e^2)^{3/2}}.$$

When we make this coordinate transformation we find that the distribution
function has simlpified dramatically to

$$f \sim 16 \pi^3 \exp \left( -\frac{E}{T} \right) \frac{(GM)^3}{(2E)^{5/2}
dE \, e \, de$$

The eccentricity dependence of the distribution function is contained
entirely in the term $$e \, de$$ and is independent of the energy.  We may
therefore write the distribution function in terms of the eccentricity alone
as

$$f(e) = 2e \, de$$,

where we have now properly normalized $$f$$. 

coordinates 

At this point we pause to discuss the limits of these quantities.  Since the
orbits are bound, the energies must be negative, so they range from 0 to
$$-\infty$$.  The phase angle naturally ranges from 0 to $$2\pi$$.  The
angular momenta can be anywhere from zero for a radial orbit to $$\infty$$
for an infinitely wide orbit.  However, for a fixed energy, there is a
maximum angular momentum, namely the angular momentum of the circular orbit
of that energy.  

It is clear that bound orbits can have
angular momenta ranging from 0 to $$\infty$$ and energies ranging from 0 to
$$-\infty$$, but it is less clear what the range of $$\sigma$$ is.  We can
neveretheless see that the range of $$\sigma$$ must be dependent on the
$$E$$ and $$L$$ of a particular orbit.  Recalling our earlier interpretation
of $$\sigma$$ as a relationship between the tangential velocity and the
circular velocity, the minimum value of $$\sigma$$ occurs at periastron and
the maximum value occurs at apastron.  Moreover, at periastron and apastron,
$$\dot{r} = 0$$, so from our definition of $$\dot{r}$$, we have that

$$2E + (GMk)^2 - \sigma^2 = 0$$

for the limits of $$\sigma$$.  We are now in a position to put all this
together into the distribution function.  But before we do this we have up
to address one subtlety we have so far overlooked---over the course of a
single orbit, the star will encounter each value of $$\sigma$$ twice (except
for the extrema): once when $$\dot{r}$$ is negative and once when it is
positive.  To account for this, we must multiply the distribution function
by an extra factor of two.  This then yields

$$f \sim \frac{16 \pi^2}{(\sigma + GMk)^2 k^4 \sqrt{2E + (GMk)^2 -
\sigma^2}} \exp \left( -2 \frac{E}{T} \right) dE dk d\sigma.$$

Now, we are only interested in the distributions of the eccentricities and
the periods, so we will have to integrate over the phase variable
$$\sigma$$.
