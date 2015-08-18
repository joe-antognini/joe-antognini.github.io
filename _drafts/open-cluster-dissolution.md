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
will be reduced.  The cluster will be out of equilibrium now, and will have
energy

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



[1]: http://adsabs.harvard.edu/abs/1980ApJ...235..986H
[2]: https://en.wikipedia.org/wiki/Virial_theorem
