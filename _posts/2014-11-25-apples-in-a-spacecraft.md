---
layout: post
title: Apples in a spacecraft
date: 2014-11-25
categories: classics
image:
  feature: constellations3.jpg
---

[Scott Tremaine's contribution][1] to a retrospective series on the work of
the French dynamicist Michel Hénon inspired me to do a review of an
interesting problem in dynamics.

### The puzzle

Suppose we are in a spacecraft orbiting the Earth in a circular orbit.  The
spacecraft is rotating such that the same side of the spacecraft always
points toward the Earth.  That is to say its rotation period is equal to its
revolution period, just like the Moon's.  Now we release a bushel of apples
inside the spacecraft so that they are floating all around us.  How will the
apples be distributed in the spacecraft after a long time?  We will assume
that they are real apples, so they are inelastic and they are not massive
enough for self-gravitation to be noticeable.  

### The solution

This question was originally posed by the Swedish physicist Hannes Alfvén in
a [1971 paper][2], but he derived the wrong answer.  The correct answer was
derived by Hénon in a [short note in 1978][3].  Hénon found that half the
apples will end up on the floor of the spacecraft and half will end up on
the ceiling.  (For simplicity, we'll call the side of the spacecraft closer
to Earth the floor, and the other side the ceiling.)

To see how this answer comes about, consider an apple which starts out
closer to the Earth than the center of mass of the spacecraft.  It is on an
orbit with a slightly smaller radius than the spacecraft, so its orbital
velocity is larger.  Over time, it will drift forward in the spacecraft
until it hits the front wall.  This collision is inelastic, so the apple
will lose energy and its orbit will shrink.  This means that it will drift
slightly towards the floor of the spacecraft and drift even faster towards
the front of the spacecraft for the next collision.  Over time, the apple
will continually collide with the front wall of the spacecraft, losing
energy, and will end up on the floor of the spacecraft.

As for an apple which starts out farther from the Earth than the center of
mass of the spacecraft, it will undergo the opposite process.  Because it is
farther from the Earth, its orbit has a larger radius and so its orbital
speed is slower than that of the spacecraft.  The apples on the upper half
of the spacecraft will therefore drift backwards to the rear wall of the
spacecraft.  There it will collide with the wall and gain energy because the
spaceship is moving faster.  Since a more energetic orbit has a larger
radius, the apple will slowly drift up towards the ceiling of the
spacecraft.  Thus over time the apple population will bifurcate with the
apples that began closer to the floor collecting on the floor towards the
front of the spacecraft and the apples that began closer to the ceiling
collecting on the ceiling towards the back of the spacecraft. 

### Timescales

How long will it take this process to occur?  If we assume that the apples
are extremely inelastic so that there are not too many collisions, then the
timescale will be a few times longer than the time it takes the apple to
drift to one end of the spacecraft.  Now, the orbital velocity of the center
of mass of the spacecraft is (assuming the spacecraft is in low Earth orbit)

$$v = \sqrt{\frac{GM_{\bigoplus}}{R_{\bigoplus}}},$$

where $$R$$ is the radius of the center of mass of the spacecraft from the
center of the Earth.  If an apple is some small distance $$\Delta R$$ closer
to the Earth than the center of mass of the spacecraft, then its velocity
will be

$$v + \Delta v = \sqrt{\frac{GM_{\bigoplus}}{R + \Delta R_{\bigoplus}}}.$$

Assuming that $$\Delta R / R_{\bigoplus} \ll 1$$, we have

$$\frac{\Delta v}{v} \simeq \frac{\Delta R}{2 R_{\bigoplus}}.$$

If we take $$\Delta R$$ to be 1 m then we find the drift velocity to be

$$\Delta v = 0.6 \, \textrm{mm} \: \textrm{s}^{-1}.$$

If the spacecraft is a spacious 10 meters long, the time it takes the apple
to drift from near the center of the spacecraft to the front wall will be 

$$t \sim 2.25 \, \textrm{hr}.$$

So it will take the apple about two hours and fifteen minutes to drift
towards the front wall of the spacecraft and less than a day for all the
apples to collect on the floor and ceiling of the spacecraft.

### The perils of a more careful analysis --- or, where Alfvén went wrong

The solution we presented above is intuitive, but does it come out of a
careful derivation?  Here we follow Tremaine's article.  The energy and
angular momentum of the system are given by

$$E = \sum_{i = 0}^N m_i \left( \frac{1}{2} v_i^2 - \frac{G
M_{\bigoplus}}{r_i} \right),$$

$$\mathbf{L} = \sum_{i=0}^N m_i \mathbf{r}_i \times \mathbf{v}_i.$$

Since the apples are inelastic, over time, collisions with the walls of the
spacecraft will dissipate energy, but not angular momentum.  We therefore
seek the minimum energy configuration for the given angular momentum.  We
can do this using a Lagrange multiplier, $$\mathbf{\lambda}$$:

$$0 = \delta E - \mathbf{\lambda} \cdot \delta \mathbf{L}.$$

The variations of the energy and angular momentum are

$$\delta E = \sum_{i=0}^N m_i \mathbf{v}_i \cdot \delta \mathbf{v}_i +
\frac{G M_{\bigoplus} m_i}{r_i^3} \mathbf{r}_i \cdot \delta \mathbf{r}_i,$$

$$\delta \mathbf{L} = \sum_{i=0}^N m_i \left( \delta \mathbf{r}_i \times
\mathbf{v}_i + \mathbf{r}_i \times \delta \mathbf{v}_i \right)$$

Grouping the terms by their differentials, we must have that

$$0 = \sum_{i=0}^N m_i \left[ \left( \mathbf{v}_i - (\mathbf{\lambda} \times
\mathbf{r}_i) \right) \cdot \delta \mathbf{v}_i + \left( \frac{G
M_{\bigoplus}}{r_i^3} \mathbf{r}_i - \mathbf{v}_i \times \mathbf{\lambda}
\right) \cdot \delta \mathbf{r}_i \right].$$

Since the differentials act independently, for this equation to be
satisfied we must have that 

$$\mathbf{v}_i = \mathbf{\lambda} \times \mathbf{r}_i,$$

$$\mathbf{\lambda} \times \mathbf{v}_i + \frac{GM_{\bigoplus}}{r^3}
\mathbf{r}_i = 0.$$

Substituting the first equation into the second, we have

$$\mathbf{\lambda} \times (\mathbf{\lambda} \times \mathbf{r}_i) +
\frac{GM_{\bigoplus}}{r_i^3} \mathbf{r}_i = 0.$$

The vector triple product vanishes if $$\mathbf{\lambda}$$ is parallel to
$$\mathbf{r}_i$$ and the equation cannot be satsified.  This implies that

$$\mathbf{\lambda} \cdot \mathbf{r}_i = 0.$$

Now taking advantage of the identity for vector triple products and using
the above relation, we have

$$\lambda^2 = \frac{GM_{\bigoplus}}{r_i^3}.$$

Since $$\lambda$$ is the same for all the apples, this implies that at an
energy extremum all the apples have the same orbital radius.  Moreover,
because $$\mathbf{\lambda} \cdot \mathbf{r}_i = 0$$ for all the apples, all
the apples must have the same orbital plane.  This result would then seem to
contradict our earlier, intuitive derivation ---  we appear to be finding
that all the apples will collect in the middle of the spacecraft.

This is where Aflvén originally went wrong.  After this derivation, he
concluded that the coplanar solution was the minimum energy solution.  But
the Legendre multiplier technique does not necessarily give us the energy
minimum --- it only gives us energy _extrema_.  In this case the coplanar
solution is actually a saddle point, so the solution we have just derived is
unstable.  To do the analysis properly, we would have to introduce another
constraint, namely, that the radii of the apples must be between the floor
and ceiling of the spacecraft.  This complicates the analysis, so we omit it
here, but we can at least understand how the minimum energy solution comes
about without doing this directly by noting that there are two singular
solutions in our above derivation: the variational equation can be satisfied
if the radius is infinite and the velocity is zero or if the radius is zero
and the velocity is infinite.  To minimize the energy we would have that all
the particles move to zero radius, but this would violate conservation of
angular momentum.  To keep angular momentum conserved, some fraction of the
apples would have to move to infinity.  In this extreme limit only an
infinitesimal number of apples would have to move out to infinity to
conserve angular momentum, but if the radii are bounded to some $$\Delta r$$
which is much less than $$r$$ then half the apples will have to move up and
half the apples will have to move down.

### Jet streams and planet formation

As interesting as this problem may be on its own, there was some motivation
for raising it --- Alfvén proposed it in the context of planet formation.
Particles in an accretion disk around a protostar can be considered to be
inelastic particles for which self gravity is negligible --- that is,
apples.  If Alfvén's solution to the apple problem was correct, then
particles in an accretion disk would naturally clump together at the same
radius in what was termed a "jet stream."  These jet streams could aid in
the formation of planets by increasing the local density and leading the
particles to stick together to form larger clumps.

But as we saw, Hénon's analysis showed that this wouldn't work.  Rather than
being brought together in a jet stream, the opposite would occur --- the
particles would dissipate.  Thus jet streams are no longer considered a
viable mechanism for planet formation.

[1]: http://arxiv.org/abs/1411.4938
[2]: http://www.jstor.org/stable/1732245
[3]: http://www.jstor.org/stable/1745593
