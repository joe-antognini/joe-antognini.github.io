---
layout: post
title: Why is the KL-divergence asymmetric?
date: 2023-02-23
categories: ml
image:
  feature: constellations3.jpg
---

A common concept one might encounter in statistics or machine learning is the
Kullback-Liebler divergence, or KL divergence.  The definition of the KL
divergence is fairly straightforward:

$$
D_{\textrm{KL}}(P || Q) \equiv \int p(x) \log \left( \frac{p(x)}{q(x)} \right)
\, dx
$$

But why does the KL divergence take this form?  Intuitively, what is the KL
divergence telling us?

The first way to look at it is to note that the expected value of any function
is given by

$$
\mathbb{E}[f(x)] \equiv \int f(x) p(x) \, dx
$$

So the KL divergence is the expected value of the quantity $\log(p(x) / q(x))$
under the distribution $p(x)$.  But what is $\log(p(x) / q(x))$?

At any particular point, $p(x)$ is simply the likelihood of that point under
the distribution $p(x)$, and $q(x)$ is the likelihood of that point under the
distribution $q(x)$.  So $p(x) / q(x)$ is just the ratio of the likelihoods
of a particular point under these two distributions.  If the two distributions
are similar around this point, the likelihoods would also be similar and this
ratio would be about 1.  If they are very different, then the ratio will either
be much smaller than 1 or much greater than 1, depending on which distribution
has the higher likelihood at that point.

Now, since we're interested in knowing whether these two distributions are
similar or different, it makes more sense to transform this ratio.  We want a
quantity that is zero if the likelihoods are similar and very far from zero if
the ratio is quite different --- in other words, we want to take the log.

So 

An intuitive way to think about this is to imagine drawing a large sample of
data points from $p(x)$.  Then for each data point in our sample, we calculate
the difference in the log likelihood for that point using the likelihood under
$p(x)$ and under $q(x)$.  The KL divergence is just the average value of those
differences in the limit that the sample tends to infinity.

### The asymmetry of the KL divergence

With this intuition in mind, we can now understand why the KL divergence is
asymmetric.  Take $p(x)$ to be a Gaussian distribution centered on 0 with unit
variance.  We'll take $q(x)$ to be a mixture of two Gaussians.  99% of the
weight will be in the first Gaussian, which also has mean zero and unit
variance.  But the other 1% in the mixture is a Gaussian with mean 10 and unit
variance.  How does the KL divergence $D_{\textrm{KL}}(P || Q)$ compare to
$D_{\textrm{KL}}(Q || P)$?

The two distributions are very close, except way out near $x = 10$, where
$q(x)$ has substantial mass but $p(x)$ has negligible mass.  So the log
likelihoods between the two distributions are pretty close everywhere except
near $x = 10$.  In this region the ratio of the two likelihoods will be of
order $\sim$$e^{-50}$.  What does this mean for the KL divergences?

Let's take $D_{\textrm{KL}}(P || Q)$ first.  Here, again, the only place where
the likelihoods between $p(x)$ and $q(x)$ are different is out at $x = 10$.  But
$x = 10$ is 10 sigma away from the mean.  We are exceedingly unlikely to sample
any data points out here.  So for any data points we do sample, we'll find that
the likelihoods of $p(x)$ and $q(x)$ are quite close, and the mean difference
in the log likelihood is small.

But the situation for $D_{\textrm{KL}}(Q || P)$ is quite different.  Now there
*is* a non-negligible chance that we will sample some data out at $x = 10$.
When this happens, we will incur a huge cost from the enormous difference in
log likelihoods in this region.  So in this case $D_{\textrm{KL}}(Q || P)$ will
be very large.

### Making it rigorous

## Why do things this way?

This asymmetry in the KL divergence feels a bit inelegant.  Intuitively, the KL
divergence is telling us how different two probability distributions are from
each other?  Why does this thing have to be asymmetric?  What's the point of
adding in the factor of $p(x)$ in the definition?  Couldn't we do something
like:

$$
\int \log \left( \frac{p(x)}{q(x)} \right) \, dx
$$

This quantity *is* symmetric!  Now, of course, we can define whatever , so
there is nothing wrong with this quantity *per se*.  But it does have a few
shortcomings.  Firstly, the KL divergence has some nice properties about
convergence so that it will be finite unless one distribution is exactly zero
at a point where the other distribution has finite mass.  The quantity above
has no such guarantees --- as you integrate out to infinity, any differences in
the log likelihoods just accumulate forever.

But the broader issue is that you can have two distributions which are nearly
identical everywhere except way out deep into the tails where, say, one decays
exponentially and the other decays superexponentially.  If we were to weight
all locations equally, this would result in a big difference between the two
distributions.  But in practice, if we draw samples from both distributions, we
will never be able to distinguish between the two, because we will never sample
any data deep into the tails.  So the KL divergence includes our intuition that
we should only be comparing distributions where it counts --- where there is
actually data.

### Other ways to symmetrize

If the asymmetry is still bothersome, there are other things you can do to get
a symmetric quantity.  The easiest thing you can do is to just take the average
of $D_{\textrm{KL}}(P || Q)$ and $D_{\textrm{KL}}(Q || P)$.  This is known as
the Jeffreys divergence

## The connection to information geometry
