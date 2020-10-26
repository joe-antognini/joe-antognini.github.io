---
layout: post
title: Expected values in the vote lottery
date: 2020-10-25
categories: misc
image:
  feature: constellations3.jpg
---

Voting is an odd thing.  We all in some sense know that our individual votes
are exceedingly unlikely to impact the election, but many of us find ourselves
highly motivated to vote anyway.  There are, of course, many reasons to vote
--- a sense of civic duty, an expression of political solidarity, or just as
something to do to break up an otherwise ordinary Tuesday afternoon.  But let
us set those aside for the time being.  What if you were only concerned with
having a non-negligible effect on the outcome of the election?  Does it still
make sense to vote?

First, what does it mean to have a non-negligible effect on the outcome?  The
strange thing about elections is that only in one circumstance can a single
vote have any influence --- in the case that one candidate receives as many as
the other plus one.  In every other case the winning candidates surplus votes
are akin to the blank "conscience round" of a firing squad.  Any individual
could have voted a different way without affecting the outcome and therefore
cannot have cast a deciding vote.  There was no deciding vote!  The outcome is
decided by *group* dynamics rather than individual behavior.

So our question boils down to finding the probability that the two candidates
will receive exactly the same number of votes.  (Now, of course, we're brushing
aside other issues.  An election that comes down to a single vote will be
heavily contesetd.  An election that is won by a single vote will have
different political implications than an election that is won in a landslide.)

## Maximizing the likelihood of a decisive vote

Let's start by putting an upper bound on the probability that a single vote
could decide a presidential election.  Since the president is elected by the
electoral college, the voting patterns of the nation as a whole are not so
relevant as votes within certain individual states.  At the moment
[FiveThirtyEight](https://projects.fivethirtyeight.com/2020-election-forecast/)
predicts that Pennsylvania is most likely to be the tipping-point state.  If
the election were to come down to the votes of a single state, Pennsylvania is
most likely to have the smallest margins.

So let's suppose that you are a voter in Pennsylvania and the election does, in
fact, come down to the outcome of your state.  Now what is the probability that
your vote determines the election?

To further maximize the probability of this hypothetical scenario, let's
suppose that there are only two candidates on the ballot and the polls have
Pennsylvania at exactly 50-50.  Naturally there is some error in the polls so
there is a distribution of outcomes that are consistent with a 50-50 polling
result.  Polls have uncertainty in them that can be broken into two components:
statistical and systematic.  The statistical error is uncertainty that
originates from our measurement of only a subset of the population.  So long as
the sample size is moderately large, the central limit theorem guarantees that
the statistical error has a Gaussian distribution, and the larger the sample
size, the smaller the error will be.

The systematic error is due to any biases in the polling methodology.
Different subpopulations may have different repsonse rates and different voting
patterns.  A naive random sample of the entire population can easily produce
extremely biased results.  Infamously, a poll by *The Literary Digest* in 1936
predicted that Republican candidate Alfred Landon would win 57% of the popular
vote in the election against President Roosevelt.  In fact Roosevelt won over
60% of the popular vote.  Though *The Literary Digest* had a sample of over 2
million responses, they did not correct for biases in the response rate.  Much
of the art of polling comes down to breaking the population into
subpopulations, weighting their results appropriately, and correcting for any
biases in response rates (along with estimating turnout for the subpopulations,
which we are completely ignoring here).

At any rate, we shall assume that the total uncertainty in the polling result
follows a Gaussian distribution.  As we'll discuss in more detail below, this
is not generally correct the systematic error, but so long as we're considering
outcomes that are not too far from the polling result, it is not a terrible
approximation.

In this case we are interested in finding the probability that the outcome of
the election is 50% to within one vote, in which case our lone vote will be
decisive.  Let's denote the voting population by $$N$$ and the polling
uncertainty in raw votes by $$\sigma$$.  Then the probability that the outcome
is within a single vote is:

$$
p = \frac{1}{\sqrt{2 \pi} \sigma} 
    \int_{\frac{1}{2}(N - 1)}^{\frac{1}{2}(N + 1)}
    e^{-\frac{(x - N/2)^2}{2 \sigma^2}} \, dx.
$$

To make this a little easier to deal with, let's normalize the variables by
population.  Rather than specifying the total uncertainty in raw numbers of
votes, let's instead consider the uncertainty as a fraction of the population:
$$\widetilde{\sigma} \equiv \sigma / N$$, and similarly the outcome of the vote
as a fraction of the population: $$\widetilde{x} \equiv x / N$$.  The
probability of an exactly equal outcome can then be written N:

$$
p = \frac{1}{\sqrt{2 \pi} N \widetilde{\sigma}}
    \int_{(1 + 1/N)/2}^{(1 - 1/N)/2}
    e^{-\left(\widetilde{x} - \frac{1}{2}\right)^2 / 2 \widetilde{\sigma}^2}
    \, d\widetilde{x}
$$

Since $$N$$ is very large, we don't in fact need to calculate this integral.  
