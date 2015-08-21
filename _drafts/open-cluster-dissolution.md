---
layout: post
title: How much mass must an open cluster lose to become unbound?
date: 2015-08-17
categories: classics
image:
  feature: constellations3.jpg
description: A look at Hills (1980).
---

Although there is strong evidence that nearly all stars are born in open
clusters, it is clear that open clusters do exist for a very long time.
After all, most stars are not seen in open clusters so they must spend a
small fraction of their lives in them.  It's also possible to measure the
ages of open clusters directly by measuring the masses of stars just
starting to evolve off the main sequence and calculating how long it takes
stars of those masses to reach that point in their evolution.  This
typically gives ages no larger than a few hundred Myr.  While there are a
few open clusters that are over a Gyr old, they are very massive and are the
exception rather than the rule. 

So we know that open clusters dissociate after a short period of time, but
why does this happen?  The very brief answer is that open clusters are only
barely bound --- they consist of a loose collection of gas and stars.  When
the most massive stars in the cluster go supernova, they shocks from the
supernovae drive out much of the gas.  This removes some of the mass from
the cluster, which unbinds it.  But how much mass must be removed to unbind
the cluster?  Is it plausible that enough mass is still in the gas phase at
the time of the supernova to unbind the cluster?  To answer this we turn to
a [brief paper][1] by J. G. Hills from 1980. 

## Sudden mass loss from a static cluster

We will follow Hills (1980) and start with the simpler problem of sudden
mass loss from a cluster which is in equilibrium.  In this case the [virial
theorem][2] applies and so the velocity dispersion of the stars in the
cluster is given by

$$v_0^2 = \frac{G M_0}{2 R_0},$$

where $M_0$ and $R_0$ are the initial mass and effective radius of the
cluster, respectively.  (If all stars in the cluster have the same mass,
then the effective radius is the harmonic mean of all the distances between
the stars.)

Immediately after the gas is driven out of the system, the stars will all
have the same velocities they did before, but the total mass of the cluster
will be reduced to $M$.  The cluster will be out of equilibrium now, and
will have energy

$$E = \frac{1}{2} \left( M v_0^2 - \frac{G M^2}{R_0} \right)$$

Once virial equilibrium is regained, the radius of the cluster will have
changed, but the energy will be the same:

$$E = -\frac{G M^2}{4 R}$$

This then results in an initial-final radius relationship for the cluster:

$$ \frac{R}{R_0} = \frac{M_0 - \Delta M}{M_0 - 2 \Delta M}.$$

We see that this ratio diverges if half the mass of the cluster is lost.
Thus, in a virialized system half the mass needs to be lost to unbind it.

#### An aside: adiabatic mass loss

Hills (1980) next briefly states the case of adiadabatic mass loss.  This
isn't particularly relevant to the question at hand but is good to know, so
I'll present here as an aside.

Adiabatic mass loss occurs whenever the fractional mass lost is small on the
dynamical timescale.  This means that the system always remains in virial
equilibrium.  It is easy to show that the initial-final radius relationship
of the cluster is in this case

$$\frac{R}{R_0} = \frac{M_0}{M_0 - \Delta M}.$$

To show this, take the initial-final radius relationship from the case of
instantaneous mass loss above and substitute $-dm$ for $\Delta M$ and $(R +
dr) / R$ for $R/R_0$ and integrate.

In this case, the initial-final radius relationship diverges only for
$\Delta M = M_0$.  In other words, the cluster always remains bound until
you remove all the mass from it entirely. 

## Mass loss prior to virialization

A real open cluster is not likely to be in virial equilibrium by the time
supernovae from massive stars drive gas out of the cluster.  The cluster
will still be contracting and this will affect the amount of mass loss that
will be necessary to unbind the cluster.

Suppose that a cluster of constant density, $\rho_0$, starts out at a radius
$a_0$ and then some time later has collapsed to a radius $a_1$ when the
supernovae go off and drive mass out of the system.  What is the energy of
the cluster at this point?  Let's start by considering the velocity of the
outer shell.  Initially its energy is all in potential energy, so we have

$$E = - \frac{4}{3} \pi G \rho_0 a_0^2.$$

The energy of the outer shell is conserved, so we have at this later time

$$v(a_1)^2 = \frac{8}{3} \pi G \rho_0 a_0 \left( \frac{a_0}{a_1} - 1
\right).$$

What about the velocity of some interior shell?  Well, since we are assuming
that the density is constant, the mass interior to any shell is $M \sim
r^3$, and since the force on any shell is $F \sim M / r^2$, we have that the
acceleration scales as $a \sim r$.  Since the velocity after some time is
just $v = a t$, we have just $v \sim r$.  Thus we can scale our result above
to arbitrary radii:

$$v(r)^2 = \frac{8}{3} \pi G \rho_0 a_0 \left( \frac{r}{a_1} \right)^2
\left( \frac{a_0}{a_1} - 1 \right).$$

Integrating over the entire shell, we can calculate the kinetic energy of
the entire cluster at this later time to be

$$T_0 = \frac{3 G M_0^2}{5 a_0} \left( \frac{a_0}{a_1} - 1 \right),$$

where $M_0$ is the initial mass of the cluster.  The mean-squared velocity
of the stars in the cluster at the time of mass loss, $\left< v^2 \right> =
2T / M_0$ is then

$$\left< v^2 \right> = \frac{6 G M_0}{5 a_0} \left( \frac{a_0}{a_1} - 1
\right).$$

After the mass loss takes place, the mean-squared velocity of the stars
remains the same, but the kinetic energy is now

$$T = \frac{1}{2} M \left< v_^2 \right>,$$

and the potential energy is (this can be looked up in a textbook or [on
Wikipedia][3]):

$$U = - \frac{3 G M^2}{5 a_1}.$$

Eventually the cluster will come into virial equilibrium with some effective
radius $R$, such that the total energy is half the potential energy:

$$E = - \frac{3 G M^2}{10 R}.$$

We can now use these equations to relate the final radius, $R$, with the initial
radius, $a_0$, to find:

$$\frac{R}{a_0} = \frac{1}{2} \left[ \frac{M_0 - \Delta M}{M_0 - \Delta M
(a_0 / a_1)} \right].$$

An unbound cluster has $R \to \infty$, so from this we can easily see how
much mass loss is necessary to unbind the cluster just by setting the
denominator equal to zero:

$$\frac{\Delta M}{M_0} = \frac{a_1}{a_0}.$$

This means that the fractional amount of mass loss necessary to unbind the
cluster is exactly equal to the fractional change in radius the cluster has
undergone. 

## How much does the cluster radius change?

[1]: http://adsabs.harvard.edu/abs/1980ApJ...235..986H
[2]: https://en.wikipedia.org/wiki/Virial_theorem
[3]: https://en.wikipedia.org/wiki/Gravitational_binding_energy
