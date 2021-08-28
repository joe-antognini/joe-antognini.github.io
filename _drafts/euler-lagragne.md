---
layout: post
title: Why is the Euler-Lagrange equation the way that it is?
date: 2021-08-27
categories: physics
image:
  feature: constellations3.jpg
---

I remember learning about the Euler-Lagrange equation the first week of a
mechanics course in college.  It looked fairly innocuous during the lecture.
One way you might see the Euler-Lagrange equation written looks like this:

$$
\frac{\partial \mathcal{L}}{\partial x} - \frac{\mathrm{d}}{\mathrm{d}t}
\frac{\partial \mathcal{L}}{\partial \dot{x}} = 0,
$$

where $$\mathcal{L}$$ is the Lagrangian, the difference between the kinetic and
potential energies.  As a somewhat trivial example, if we dropped a ball of
mass $$m$$ and measured its height with $$x$$, the Lagrangian would be

$$
\mathcal{L} = \frac{1}{2} m \dot{x}^2 - m g x.
$$

The Euler-Lagrange equation is equivalent to Newton's laws, so solving the
Euler-Lagrange equation can oftentimes be a more straightforward way of
determining the equations of motion of the system than going through a block
diagram and applying Newton's laws.

But I got very confused when I started working on the first problem set and
tried solving this equation.  How do you take the derivative with respect to
$$x$$?  After all, it seemed to me that this derivative would depend on both
$$x$$ and $$\dot{x}$$.  If you changed the velocity of the ball $$\dot{x}(t)$$,
you'd necessarily change its trajectory $$x(t)$$ as well.  So it seemed to me
that you'd have to somehow apply the chain rule in order to properly
differentiate with respect to $$x$$.  And likewise, you'd have to do the same
thing when you take the derivative with respect to $$\dot{x}$$.  If you change
the velocity of the ball, you're necessarily changing its position over time as
well.

Well I tried some things and got some nonsensical results.  Eventually a friend
helped me out and told me that the partial derivatives meant that you just
ignore the velocity when you're considering the position and vice versa.  So in
the example above, we simply have

$$
\frac{\partial \mathcal{L}}{\partial x} = -mg
$$

and

$$
\frac{\partial \mathcal{L}}{\partial \dot{x}} = m \dot{x}
$$

I was able to follow the procedure and get the right answer.  But the logic of
it never sat well with me.  After all, $$\partial \mathcal{L} / \partial x$$ is
telling you how the Lagrangian changes if you perturb the particle's
trajectory, *while not perturbing its velocity*.  How can this be possible?
How can we change the particle's trajectory without changing the velocity?
After all, onec we've solved the equation, we have a trajectory which uniquely
determines the velocity at all points in time.  It seems we cannot change the
trajectory without changing the velocity even if we denote the derivative with
a fancy $$\partial$$ instead of a $$\mathrm{d}$$ in our notation.

I believe I'm not alone in thinking that this is weird.  In the *Road to
Reality*, Roger Penrose described it as "baffling."  Richard Feynman outlines
the procedure in one of the early lectures in the Feynman Lectures, though he
doesn't actually invoke the Euler-Lagragne equation by name.  He instead talks
about "virtual work" and the idea of .  But the underlying concept is the same,
and it's just as weird.  It seems non-physical!  How does it work?

Well, when I first learned about all this in college I needed to solve problem
sets, so I put these doubts aside for the time being.  But the strangeness of
the method never quite left me.

TODO:
* A derivation of the Euler-Lagrange equation
* Function and derivative really are independent
* Bolza problem
* Why are solutions to the Euler-Lagrange equation nice in practice?
