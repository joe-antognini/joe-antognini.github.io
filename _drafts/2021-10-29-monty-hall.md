---
layout: post
title: The Monty Hall problem requires a theory of mind
date: 2021-10-29
categories: ml
image:
  feature: constellations3.jpg
---

The Monty Hall problem is a classic puzzle in probability.  A common statement
of the problem goes something like this:

> You are on a game show.  There are three doors.  There is a car behind one of
> the doors, but you do not know which one.  There is an old boot behind both
> of the other doors.  You get to pick a door to open, but before you open it,
> the game show host opens another door, revealing an old boot.  He then gives
> you the opportunity to switch to the remaining unopened door.  Should you
> make the switch?

Intuition suggests that it does not matter which door you pick.  But a careful
solution shows that you double your chances from $$1/3$$ to $$2/3$$ if you make
the switch.

Or does it?

The usual solution relies on Bayes's Theorem.  Suppose for concreteness that
you pick Door 1 and the host opens Door 2.  Let's write the probability that
the reward is behind door $$i$$ as $$p(r = i)$$ and the probability that the
host opens door $$i$$ as $$p(d = i)$$.  The problem is essentially to find
$$p(r = 1 | d = 2)$$.  In other words, what is the probability that the car is
behind Door 1 given that the host has opened Door 2?  If this probability is
less than $$1/2$$ we should switch, if it is greater than $$1/2$$ we should
stay, and if it is exactly $$1/2$$ it doesn't matter what we do.

From Bayes's Theorem we know:

$$
p(r = 1 | d = 2) = \frac{p(d = 2 | r = 1) p(r = 1)}{p(d = 2)}.
$$

The denominator can be expanded out to read:

$$
p(d = 2) = \sum_{i = 1}^3 p(d = 2 | r = i) p(r = i).
$$

Now we know that the car is equally likely to be behind any door, so $$p(r) = 1
/ 3$$.  So all we have to do is figure out $$p(d = 2 | r = i)$$ for the various
choices of $$i$$.

This is where things get subtle.  Continuing with the standard solution, we say
that the probability that the host opens Door 2 given that the reward is behind
Door 1 is $$1/2$$ since the host could have picked *either* Door 2 or Door 3.

$$
p(d = 2 | r = 1) = \frac{1}{2}
$$

The host would not open Door 2 if the reward was behind Door 2, so

$$
p(d = 2 | r = 2) = 0.
$$

And finally if the reward was behind Door 3, then the host had no other choice
than to open Door 2, so

$$
p(d = 2  r = 3) = 1
$$

If we combine this all together, we find that

$$
p(d = 2) = \frac{1}{2}
$$

and from Bayes's Theorem,

$$
\begin{eqnarray}
p(r = 1 | d = 2) & = & \frac{\frac{1}{2} \times \frac{1}{3}}{\frac{1}{2}} \\
& = & \frac{1}{3}.
\end{eqnarray}
$$

So it is apparently in our best interest to switch to Door 3.  This increases
our probability from 1/3 to 2/3.

But this is not in fact a correct solution given the statement of the problem
as I laid it out at the beginning of this post!  Implicit in this solution is a
theory of mind.  Or at least a knowledge of the algorithm that Monty Hall is
using.  This is instead a correct solution to a slightly different statement of
the problem, with the difference in italics:

> You are on a game show.  There are three doors.  There is a car behind one of
> the doors, but you do not know which one.  There is an old boot behind each
> of the other doors.  You get to pick a door you'd like to open, but before
> you open it, *you know that* the game show host *will always* open another
> door, and this *will always* reveal an old boot.  He then gives you the
> opportunity to switch to the remaining unopened door.  Should you make the
> switch?

The difference here is that you know how Monty Hall will behave.  In order to


The point is that to correctly solve this problem, it is not sufficient to know
what actions the host took.  It is also necessary to know the *mechanism* by
which the host took the actions that he did.  Another way of looking at this is
that it requires knowing a counterfactual --- what *would* the host have done
in a situation where the reward was behind a different door than it actually
was?

One 


* Show how this relates to the calculation of p(d|r)
* Compare to the "Monty Hell" and "Dumb Monty" problems
