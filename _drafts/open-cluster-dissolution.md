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

where $$M_0$$ and $$R_0$$ are the initial mass and effective radius of the
cluster, respectively.  (If all stars in the cluster have the same mass,
then the effective radius is the harmonic mean of all the distances between
the stars.)

Immediately after the gas is driven out of the system, the stars will all
have the same velocities they did before, but the total mass of the cluster
will be reduced to $$M$$.  The cluster will be out of equilibrium now, and
will have energy

$$E = \frac{1}{2} \left( M v_0^2 - \frac{G M^2}{R_0} \right)$$

Once virial equilibrium is regained, the radius of the cluster will have
changed, but the energy will be the same:

$$E = -\frac{G M^2}{4 R}$$

This then results in an initial-final radius relationship for the cluster:

$$ \frac{R}{R_0} = \frac{M_0 - \Delta M}{M_0 - 2 \Delta M}.$$

We see that this ratio diverges if half the mass of the cluster is lost.
Thus, in a virialized system half the mass needs to be lost to unbind it.

### An aside: adiabatic mass loss

Hills (1980) next briefly states the case of adiadabatic mass loss.  This
isn't particularly relevant to the question at hand but is good to know, so
I'll present here as an aside.

Adiabatic mass loss occurs whenever the fractional mass lost is small on the
dynamical timescale.  This means that the system always remains in virial
equilibrium.  It is easy to show that the initial-final radius relationship
of the cluster is in this case

$$\frac{R}{R_0} = \frac{M_0}{M_0 - \Delta M}.$$

To show this, take the initial-final radius relationship from the case of
instantaneous mass loss above and substitute $$-dm$$ for $$\Delta M$$ and
$$(R + dr) / R$$ for $$R/R_0$$ and integrate.

In this case, the initial-final radius relationship diverges only for
$$\Delta M = M_0$$.  In other words, the cluster always remains bound until
you remove all the mass from it entirely. 

## Mass loss prior to virialization

A real open cluster is not likely to be in virial equilibrium by the time
supernovae from massive stars drive gas out of the cluster.  The cluster
will still be contracting and this will affect the amount of mass loss that
will be necessary to unbind the cluster.

Suppose that a cluster of constant density, $$\rho_0$$, starts out at a
radius $$a_0$$ and then some time later has collapsed to a radius $$a_1$$
when the supernovae go off and drive mass out of the system.  What is the
energy of the cluster at this point?  Let's start by considering the
velocity of the outer shell.  Initially its energy is all in potential
energy, so we have

$$E = - \frac{4}{3} \pi G \rho_0 a_0^2.$$

The energy of the outer shell is conserved, so we have at this later time

$$v(a_1)^2 = \frac{8}{3} \pi G \rho_0 a_0 \left( \frac{a_0}{a_1} - 1
\right).$$

What about the velocity of some interior shell?  Well, since we are assuming
that the density is constant, the mass interior to any shell is $$M \sim
r^3$$, and since the force on any shell is $$F \sim M / r^2$$, we have that
the acceleration scales as $$a \sim r$$.  Since the velocity after some time
is just $$v = a t$$, we have just $$v \sim r$$.  Thus we can scale our
result above to arbitrary radii:

$$v(r)^2 = \frac{8}{3} \pi G \rho_0 a_0 \left( \frac{r}{a_1} \right)^2
\left( \frac{a_0}{a_1} - 1 \right).$$

Integrating over the entire shell, we can calculate the kinetic energy of
the entire cluster at this later time to be

$$T_0 = \frac{3 G M_0^2}{5 a_0} \left( \frac{a_0}{a_1} - 1 \right),$$

where $$M_0$$ is the initial mass of the cluster.  The mean-squared velocity
of the stars in the cluster at the time of mass loss, $$\left< v^2 \right> =
2T / M_0$$ is then

$$\left< v^2 \right> = \frac{6 G M_0}{5 a_0} \left( \frac{a_0}{a_1} - 1
\right).$$

After the mass loss takes place, the mean-squared velocity of the stars
remains the same, but the kinetic energy is now

$$T = \frac{1}{2} M \left< v_{\infty}^2 \right>,$$

and the potential energy is (this can be looked up in a textbook or [on
Wikipedia][3]):

$$U = - \frac{3 G M^2}{5 a_1}.$$

Eventually the cluster will come into virial equilibrium with some effective
radius $$R$$, such that the total energy is half the potential energy:

$$E = - \frac{3 G M^2}{10 R}.$$

We can now use these equations to relate the final radius, $$R$$, with the
initial radius, $$a_0$$, to find:

$$\frac{R}{a_0} = \frac{1}{2} \left[ \frac{M_0 - \Delta M}{M_0 - \Delta M
(a_0 / a_1)} \right].$$

An unbound cluster has $$R \to \infty$$, so from this we can easily see how
much mass loss is necessary to unbind the cluster just by setting the
denominator equal to zero:

$$\frac{\Delta M}{M_0} = \frac{a_1}{a_0}.$$

This means that the fractional amount of mass loss necessary to unbind the
cluster is exactly equal to the fractional change in radius the cluster has
undergone.  This then leads to the question:

## How much does the cluster radius change?

The basic picture of the formation of a star cluster is that the
protocluster begins as a molecular cloud with some radius and average
density, $$\left< \rho_0 \right>$$ which then shrinks under its own
gravitational influence.  However, the cloud is not of uniform density ---
some pockets of the cloud will be somewhat denser than others and will
therefore collapse faster.  To determine how much the cluster radius changes
we must estimate by how much the cluster has collapsed at the time the
densest pockets have formed stars (which, for the purposes of this estimate
is the time that these dense pockets have collapsed to zero radius).  

We'll begin by writing down the equation of motion for some shell that
starts at radius $$r_0$$:

$$\frac{ d^2 r}{dt^2} = - \frac{G M(r_0)}{r^2} = - \frac{4 \pi G \left<
\rho_0 \right> r_0^3}{3 r^2}.$$

If we multiply both sides by $$dr/dt$$, we can integrate to find

$$\frac{1}{r_0} \frac{dr}{dt} = - \sqrt{\frac{8}{3} \pi G \left< \rho_0
\right> \left( \frac{r_0}{r} - 1 \right)}.$$

This is a tricky differential equation to solve, but if we make the clever
substitution $$r/r_0 = \cos^2 \beta$$, we can rewrite it as

$$\frac{d \beta}{dt} = \frac{1}{2} \sqrt{ \frac{8}{3} \pi G \left< \rho_0
\right>} \sec^2 \beta,$$

which is then easily integrated to yield the collapse equation:

$$\beta + \frac{1}{2} \sin 2 \beta = t \sqrt{ \frac{8}{3} \pi G \left<
\rho_0 \right>}.$$

Now suppose that some pocket in the protocluster began with a slight
overdensity, $$\rho^{\prime}$$.  The time this pocket to collapse to zero
radius can be found by setting $$\beta = \pi / 2$$ and solving for $$t$$:

$$t_c = \sqrt{ \frac{3 \pi}{32 G \rho^{\prime}}}.$$

We can then write the collapse equation in terms of $$t_c$$ and radii:

$$\frac{r}{r_0} + \sqrt{\frac{r}{r_0} - \left( \frac{r}{r_0} \right)^3} =
\frac{\pi}{2} \sqrt{ \frac{\left< \rho_0 \right>}{\rho^{\prime}}}.$$

So in order to estimate the radius of the cluster at the time the most
massive stars form (i.e., $$r/r_0$$), we must estimate $$\left< \rho_0
\right> / \rho^{\prime}$$.  If we assume that the molecular cloud is rather
homogeneous, and the greatest density fluctuations are only 10%, then we can
numerically solve the above equation to find $$r/r_0 \approx 0.2$$.  The
more homogeneous the cloud begins, the smaller $$r/r_0$$ is.  It is
therefore plausible that a typical protocluster will have $$r_0 / r \sim
10$$.  If we use this estimate with our result from the previous section, we
find that the cluster needs to lose only 10% of its mass to become unbound. 

## Why does so little mass need to be lost?

Let us picture the process of virialization.  We begin with a cluster of
stars, all stationary and at a very large distance.  Due to their mutual
gravitational attraction, they begin to fall to the center of the cluster
and pick up speed.  As they pass through the center of the cluster, they
have strong gravitational interactions with each other.  This process
transfers energy among the stars and redirects their trajectories.  However,
the stars generally have enough velocity that they make it out to nearly the
same distance that they started at roughly the same time.  Over a long
enough time, the strong gravitational encounters at the center of the
cluster serve to transfer enough energy between stars that the trajectories
of the stars become sufficiently randomized that as some stars are at
apocenter, other stars are passing through the center of the cluster and the
cluster has become virialized. 

Now, if the cluster loses mass at the very beginning of its life when the
stars are at a very large distance it is not going to affect this process.
The stars will pass through the center with lower speed, but qualitatively
nothing else will change.  This is because when the mass is lost from the
system, it takes the gravitational potential energy it had away with it.

If, however, the mass loss takes place as the stars are passing through the
center of the cluster the situation is different.  At this point, the
gravitational potential energy from the mass that is lost has been
transferred to the mass that remains in the form of kinetic energy.  In
other words, the extra mass has increased the speed of the stars as they
pass through the center of the cluster.  When the mass is then lost, it is
unable to contribute to the gravitational attraction that slows the stars
down enough to keep them bound.  The closer the stars are to the center of
the cluster when mass is lost, the more mass needs to remain to keep the
cluster bound since nearly all of the energy is in kinetic energy at this
point.  Since the cluster will have collapsed by quite a bit by the time the
first supernovae go off if it began relatively homogeneous, this means that
only a modest amount of mass needs to be lost to unbind the cluster.

## What is the velocity of the unbound stars?

If the mass loss succeeds in unbinding the cluster, how fast do the stars
escape?  Conservation of energy states that after mass loss we have

$$\frac{1}{2} M \left< v_{\infty}^2 \right> = \frac{1}{2} M \left< v^2
\right> - \frac{3}{5} \frac{G M^2}{a_1},$$

which can be rewritten in terms of the velocity dispersion that the cluster
would have after virialization if mass loss had not occured, $$\left< v_c^2
\right>$$, as

$$\left< v_{\infty}^2 \right>^{1/2} = \left< v_c^2 \right>^{1/2} \sqrt{
\left( \frac{a_0}{a_1} \right) \left( \frac{ \Delta M}{M_0} \right) - 1}.$$

So for reasonable amounts of mass loss the expansion velocity will be only a
few times larger than the velocity dispersion of the virialized cluster.
This means that for a massive O star with a lifetime of a few tens of
millions of years and an escape velocity of a few km / s, the supernova will
take place of order 100 pc away from its birthsite!

## A postscript: What about magnetic fields?

We have been working with a very simplified model of a protocluster.  A
realistic protocluster will have magnetic fields which will affect the
evolution of the cluster.  In particular, as the cluster collapses, the
magnetic fields threading the cluster will become more compact, leading to a
higher magnetic energy density.  This will result in an additional source of
pressure which will serve to resist the collapse of the cluster.  Thus,
although we estimated that the cluster would have collapsed to some fraction
of its radius, $$r / r_0$$ at the time of mass loss, the cluster will
actually have only collapsed to some larger fraction of its radius
$$r^{\prime} / r_0$$ (where $$r^{\prime} > r$$) due to the extra magnetic
pressure.  The exact amount by which $$r^{\prime}$$ is larger than $$r$$
will depend on how much energy is in magnetic fields compared to
gravitational potential energy.  

Since the energy density in magnetic fields in the ISM is comparable to the
thermal energy density (and pretty much every thing else, as it happens), we
can a priori guess that magnetic fields will have an order unity effect on
the evolution of the cluster.  So, for the cluster above where we estimated
that only 10% of mass loss was necessary to unbind the cluster, it might be
more like 15% or 20%.  As it happens, this guess is correct.

[1]: http://adsabs.harvard.edu/abs/1980ApJ...235..986H
[2]: https://en.wikipedia.org/wiki/Virial_theorem
[3]: https://en.wikipedia.org/wiki/Gravitational_binding_energy
