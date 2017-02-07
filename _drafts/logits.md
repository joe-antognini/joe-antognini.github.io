---
layout: post
title: Reverse engineering the logit
date: 2016-09-28
categories: ml
image:
  feature: constellations3.jpg
---

If you spend some time working with neural networks you will inevitably
begin hearing the term "logit" all around.  The definition of the logit is
simple enough:

$$\textrm{logit} p \equiv \log \left( \frac{p}{1 - p} \right).$$

But it's useful to understand where this definition comes from and why
logits are so natural in machine learning.

While one of the big tasks we commonly deal with in machine learning is
classification, oftentimes what we really would like is a classification
probability.  That way, not only can we place a test instance in a
particular class, but we can also make some claim about how likely we
believe that instance actually belongs to that class.  (And ideally, we
would *really* prefer some sort of confidence interval around that
probability, but that seems to be too much to ask for with commonly
available, over-the-counter methods.)

Suppose, for concreteness, we have a simply have a linear model as a binary
classifier:

$$p = \textbf{w} \textbf{x}$$,

where $$\textbf{x}$$ is an input, $$\textbf{w}$$ is a weight matrix that we
fit to some training data, and $p$ is the class probability.  Let's suppose
we train this model by naively minimizing the squared error between $p$ and
the true class (0 or 1 for the negative and positive classes, respectively). 

Now we have two issues here.  The first is that probabilities are restricted
to the range $(0, 1)$, but our model could conceivably output any real
number.  We could making some ad hoc changes to deal with this by, say,
clamping outputs below 0 to 0, and outputs above 1 to 1.  But this points to
a deeper issue with interpreting the output of our linear model as a
probability --- namely, that these outputs don't seem to behave the way we
would expect probabilities to.

To make this concrete, let's say that on one case in the training set the
model gives a probability that the input belongs to the positive class of
0.5.  On a second training case the NN gives a probability that the input
belongs to the positive class of 0.99.  We now perturb the inputs very
slightly, and by the same amount, so the predicted probabilities increase by
0.009.  The positive class membership probability is now 0.509 for the first
input, and 0.999 for the second input.  

As far as the model's loss function is concerned, these two changes are
equivalent.  But they are not at all.  In the first case, we started with
the case being equally likely to belong to the positive or negative classes,
and after the perturbation the case is only very slightly more likely to
belong to the positive class than the negative class.  In the second case,
we started with the case being very likely to belong to the positive class,
but after the perturbation the case was *overwhelmingly* more likely to be
in the positive class.  Nothing much changed in the first case, but in the
second case the probability of being in the negative class fell by an order
of magnitude!

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
simply add them up since each one will be small when the other is big.  And
this gives us the logit.

What we've basically done here, is make a function that takes as its domain
the open unit real line $(0, 1)$, and stretches it out over the entire real
line, so that as you get exponentially close to 0, the function gets
negative linearly, and as you get exponentially close to 1, the function
gets positive linearly.  

With this intuition of what we want out of the function, we could have
simply guessed the correct answer all along!  A useful tool in the
mathematics toolbag is that if you want a differentiable function that maps
the real numbers onto the range $(0, 1)$ the sigmoid function fits the bill.
(In fact, the sigmoid function is used for this purpose to prove that the
real numbers in the range $(0, 1)$ are uncountable.)  Since we want to do
the opposite and take the reals between $(0, 1)$ and map them onto the reals
between $(-\infty, \infty)$, we want to use its inverse: which turns out to
be the definition of the logit!
