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

f \sim \exp \left( -\frac{E}{T} \right)

where $$\tau$$ is some measure of the thermal content of the system.  Now,
the energy of an individual binary system is

E = \frac{1}{2} \mu v^2 - \frac{G M \mu}{r}

where $$r$$ and $$v$$ are the relative distance and velocity, respective,
$$M$$ is the total mass of the system, and $$\mu$$ is the reduced mass of
the system,

$$\mu \equiv \frac{m1 m2}{M}.

The total number of systems in a differential element of phase space is

f d\dot{x} d\dot{y} d\dot{z} dr r^2 d\Omega \sim \exp \left[ \frac{1}{T}
\left( \frac{1}{2} \mu (\dot{x}^2 \dot{y}^2 \dot{z}^2) - \frac{G M \mu}{r}
\right) \right] d\dot{x} d\dot{y} d\dot{z} dr r^2 d\Omega

It helps if we decompose the velocity into its radial and tangential
components --- $$v^2 = \dot{r}^2 + \tau^2$$.  

We so far have been using real, physical coordinates as much as possible to
describe the binaries.  But what we would like is to transform this
distribution function into a set of coordinates describing the overall
properties of the binary, like its semi-major axis and eccentricity.
