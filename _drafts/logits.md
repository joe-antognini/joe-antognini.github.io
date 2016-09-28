---
layout: post
title: Reverse engineering the logit
date: 2016-09-28
categories: toolkit
image:
  feature: constellations3.jpg
---

If you spend some time working with neural networks you will inevitably
begin hearing the term "logit" all around.  The logit has a simple
definition:

$$\textrm{logit} p \equiv \log \left( \frac{p}{1 - } \right).$$

But it's useful to understand where this definition comes from and why
logits are so natural in machine learning.

But why is this a natural
definition and why are logits so frequently used?


Neural networks are inherently going to be a little "fuzzy" when used on
real data.  Real data are noisy, and as the inputs jitter around, the
activations of different neurons will jitter around a little bit as well.
The neural network should be robust to this jitter --- most small
perturbations of the input should not produce big changes to the output.
But when we start considering the output of the neural network, we have to
be careful about what we consider a "big change."

Suppose, for concreteness, we have a neural network that is a binary
classifier.  On one input, the NN gives a probability that the input belongs
to class A of 0.5.  On the second input the NN gives a class A membership
probability of 0.99.  We now perturb the inputs very slightly and the
probabilities change by 0.009.  The class A membereship probability is now
0.509 for the first input, and 0.999 for the second input.  The As far as
the neural network is concerned, the changes here are equivalent.  But they
are not at all.  

How could we try to account for this?  Instead of trying to train directly
to the probability, we could instead try to train to $$\log(1 - p)$$.  This
way, the relative difference between 0.9 and 0.99 is the same as the
relative difference between 0.99 and 0.999.  This works well for
probabilities which are nearly 1, but what about very small probabilities?
We would like to similarly distinguish between 0.01, and 0.001, and 0.0001.
In the case of small probabilities, it's natural then to train simply to
$$\log p$$.

But we clearly wouldn't like to have two separate things we're training, one
in the case of small probabilities and one in the case of large
probabilities.  We'd like to stitch the two of these together.  Since $$\log
p \to 0$$ as $$p \to 1$$ and $$\log (1 - p) \to 0$$ as $$p \to 0$$, we can
simply add them up.

What we've basically done here, is make a function that takes as its domain
the unit real line $(0, 1)$, and stretches it out over the entire real line,
so that as you get exponentially close to 0, the function gets negative
linearly, and as you get exponentially close to 1, the function gets
positive linearly.  

With this intuition of what we want out of the function, we could have
simply guessed the correct answer all along!  A useful tool in the
mathematics toolbag is that if you want a differentiable function that
maps the real numbers onto the range $(0, 1)$ the sigmoid function fits the
bill.  (In fact, the sigmoid function is commonly used for this purpose in
proofs that the real numbers in the range $(0, 1)$ are uncountable.)  Since
we want to do the opposite (take the reals between $(0, 1)$ and map them
onto the reals between $(-\infty, \infty)$, we want to use its inverse:
which turns out to be the definition of the logit!
