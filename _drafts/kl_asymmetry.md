---
layout: post
title: Why is the KL-divergence asymmetric?
date: 2017-01-17
categories: ml
image:
  feature: constellations3.jpg
description: An intuitive explanation.
---

I occasionally see questions come up on Stack Exchange asking for an
intuitive explanation of why the Kullback-Liebler divergence is asymmetric.
There are some good answers there, but I thought I would explain the way I
think about it.

Intuitively, the KL-divergence is the extra cost, in bits per data point,
that you have to pay when using one probability distribution to describe
data drawn from another.  The asymmetry essentially comes about from the
fact that it costs much more to explain the existence of data points that
your reference distribution predicts to be extremely unlikely compared to
the cost of describing the non-existence of data points that your reference
distribution predicts to be common.

To make this explanation concrete, consider two Gaussian, $p_1$ and $p_2$,
both centered around 0, where one is extremely narrow and the other is
extremely wide.  Let us call the standard deviations of the two Gaussians
$\sigma_1$ and $\sigma_2$, respectively, so we have $\sigma_1 \ll \sigma_2$.

If we draw data from the narrow Gaussian, we will, of course, find that all
the data points are very close to 0.  The probability that you would pick a
data point very close to zero from the wide Gaussian is not quite as large,
but it's certainly not negligible.  After all, you are more likely to pick a
data point from that particular narrow range than any other narrow range on
the real number line.  So if you use the wide Gaussian to describe data
drawn from the narrow Gaussian there will be some KL divergence because the
two Gaussians aren't the same.

But now consider the situation the other way around.  Suppose we have drawn
data from the wide Gaussian.  There will be some points which are quite far
from zero.  The probability of drawing these points from the narrow Gaussian
is vanishingly small.  So if we try to describe the data from the wide
Gaussian with the narrow Gaussian we will find that the KL divergence is
much higher.

## Making the intuition rigorous

Let's see how this explanation works out with the math.  Our probability
distributions are given by

$$p_1(x) = \frac{1}{\sqrt{2 \pi \sigma_1^2}} \exp \left( - \frac{x^2}{2
\sigma_1^2} \right),$$

and

$$p_2(x) = \frac{1}{\sqrt{2 \pi \sigma_2^2}} \exp \left( - \frac{x^2}{2
\sigma_2^2} \right).$$

For a continuous probability distirbution, the KL divergence is defined as

$$D_{KL}(p_1 || p_2) \equiv \int p_1(x) \log \frac{p_1(x)}{p_2(x)} dx.$$

For our Gaussians we therefore have

$$D_{KL}(p_1 || p_2) = \frac{1}{\sqrt{2 \pi \sigma_1^2} \int \exp \left( -
\frac{x^2}{2 \sigma_1^2} \right) \left[ \log \left(
\frac{\sigma_1}{\sigma_2} \right) + \frac{x^2}{2\sigma_1^2} \left(
\frac{\sigma_1^2}{\sigma_2^2} - 1 \right) \right] dx.$$

After integrating, we find

$$D_{KL}(p_1 || p_2) = \frac{1}{\sqrt{\sigma_1}} \left( \log \left(
\frac{\sigma_2}{\sigma_1} \right) + \sqrt{\frac{\pi}{2}} \left[ \left(
\frac{\sigma_1}{\sigma_2} \right)^2 - 1 \right] \right).$$

Now, let's look at the asymmetry between the KL divergences of the two
distributions by taking the ratio of $D_{KL}(p_1 || p_2)$ to $D_{KL}(p_2 ||
p_1)$.  If it is much costlier to use the narrow distribution to describe
the wide distribution than vice versa, we should find that this ratio will
approach zero.  If we calculate the ratio, we have

$$\frac{D_{KL}(p_1 || p_2)}{D_{KL}(p_2 || p_1)} =
\sqrt{\frac{\sigma_2}{\sigma_1} \left( \frac{ \log (\sigma_2 / \sigma_1) +
\sqrt{\pi/2} [(\sigma_1 / \sigma_2)^2 - 1]}{\log (\sigma_1 / \sigma_2) +
\sqrt{\pi/2} [(\sigma_2 / \sigma_1)^2 - 1]}.$$

If we now take the limit as $\sigma_1 / \sigma_2 \to 0$, we find that 

$$ \lim_{\sigma_1 / \sigma_2 \to 0} \frac{D_{KL}(p_1 || p_2)}{D_{KL}(p_2 ||
p_1)} = 0,$$

which is what we predicted.
