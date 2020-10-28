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
relevant as votes within particular states.  At the moment
[FiveThirtyEight](https://projects.fivethirtyeight.com/2020-election-forecast/)
predicts that Pennsylvania is the most likely to cast the decisive electoral
college vote.

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
p = \frac{1}{\sqrt{2 \pi} \widetilde{\sigma}}
    \int_{(1 - 1/N)/2}^{(1 + 1/N)/2}
    e^{-\frac{\left(\widetilde{x} - 1/2\right)^2}{2
    \widetilde{\sigma}^2}}
    \, d\widetilde{x}
$$

Since $$N$$ is very large, we don't in fact need to calculate this integral
explicitly.  Since the probability density function does not change very much
over the narrow range $$\left[ 1/2(1 - 1/N), 1/2(1 + 1/N) \right]$$, so we can
approximate the probability by the value of the function at $$\widetilde{x} =
1/2$$ times the width:

$$
p \simeq \frac{\Delta \widetilde{x}}{\sqrt{2 \pi} \widetilde{\sigma}}.
$$

And since the width is simply $$\Delta \widetilde{x} = 1 / N$$, we have

$$
p \simeq \frac{1}{\sqrt{2 \pi} N \widetilde{\sigma}}.
$$

So what is the probability of casting the decisive vote for some reasonable
numbers for Pennsylvania?  Pennsylvania has $$\sim$$9 million registered voters
for the [2020
election](https://philadelphia.cbslocal.com/2020/10/19/pennsylvania-nears-9-million-voters-at-registration-deadline/).
Let's furthermore assume the polling uncertainty is 4%, which is the
[historical accuracy of polls in the general
election](https://fivethirtyeight.com/features/the-state-of-the-polls-2019/).
high side based on historical polling performance.)  With these numbers we
have:

$$
p \approx 1.1 \times 10^{-6}
$$

or, slightly better than one in a million.

### The expected value of a decisive vote

These look like long odds!  And indeed they are.  But does this mean that we
shouldn't bother with voting?  No!  We can't make that determination until we
compare it with the value of casting the decisive vote relative to the cost of
voting.

So how much is casting the decisive vote worth?  It is hard to really quantify
this.  We could ask, "How much would you be willing to pay to guarantee the
outcome of a presidential election?"  But that is probably not the right
metric.  The value shouldn't be determined by its value to the median voter,
but rather by its value to society as a whole.  As a lower bound we could put
its value at the total amount spent on campaigning.  But this still likely a
significant underestimate since campaign spending has diminishing returns.  The
marginal dollar spent on Biden or Trump's campaign has a very weak impact on
the likelihood of the outcome.  We could imagine that if one could guarantee
the outcome of an election with a certain amount of spending, donors would be
willing to fork up quite a bit more.

But since we don't know exactly how much that would be, we'll instead content
ourselves with the total campaign spending for the 2020 presidential election,
which is about [$11
billion](https://www.opensecrets.org/news/2020/10/2020-election-to-near-11-billion-in-total-spending-smashing-records).

The expected value of casting a vote in a hypothetical Pennsylvania that's in a
dead heat is $$\sim$$**$12,000**.

So as long as it costs you less than $12,000 to vote in this hypothetical
scenario, you can at least go to the polls with the comfort that the expected
value of your vote is quite high!  While the odds that you'll cast the decisive
vote are quite low, the payoff is so high as to make it worth it.

### A realistic Pennsylvania

We've now found a best-case secnario where the probability is casting the
decisive vote is maximized by assuming that the polls put Pennsylvania in a
dead heat.  But as of this writing, Pennsylvania is not in a dead heat.
FiveThirtyEight's polling average has Biden up by [5.6%
points](https://projects.fivethirtyeight.com/polls/president-general/pennsylvania/)
in Pennsylvania.  How does this affect the expected value?

Let's call the polling differential $$\delta$$.  Then we have $$\widetilde{x} =
1/2 \pm \delta / 2$$.  With this change we now have the probability of casting
the decisive vote as

$$
p \simeq \frac{1}{\sqrt{2 \pi} N \widetilde{\sigma}} e^{-\frac{\delta^2}{8
\widetilde{\sigma}^2}}.
$$

Plugging in our assumed values we find that the probability of casting the
decisive vote has now gone down to $$9 \times 10^{-7}$$ with an expected value
of $9500.

### Correcting for the probability of being in the tipping point state

So far we have simply assumed that Pennsylvania will cast the decisive vote.
But there is no guarantee that this will happen.  As of this writing,
FiveThirtyEight gives Pennsylvania a 30% chance of being the tipping point
state.  (The tipping point state is found by arranging the states in order of
decreasing margins for the winner of the election and then taking the state
that pushes the winning candidate over 270 votes.  Note that if the tipping
point state is won by a single vote, then the electoral college came down to
the results of that state.)

So we should multiply the probabilities we found above by 30% to account
for this.  This means that a voter in Pennsylvania has a probability of $2.6
\times 10^{-7}$ of deciding the election, which corresponds to an expected
value of $2900.

## Voting in California

It's reasonable to conclude that voting in Pennsylvania is worth it this
election.  But what if you live in California?  Should you vote then?

FiveThirtyEight doesn't explicitly provide the probability of California being
the tipping point state, but simply puts it at less than 1%.  Let's
nevertheless assume the probability to be 1% in order to calculate an upper
bound.

As of this writing FiveThirtyEight puts the polling differential in California
at 29.1%.  If we naively use the same method as above but now take the number
of registered voters to be [21
million](https://www.sacbee.com/news/politics-government/capitol-alert/article245571555.html)
the probability of casting a decisive vote in the presidential election is $$6
\times 10^{-12}$$.  Even assuming the prodigious payoff of $11 billion for
pulling off that feat, the expected value of a California vote is a mere 7¢.

But how much can we trust these numbers?  We can have more confidence in the
numbers for Pennsylvania because an outcome that is decided by a single vote
would require a polling error of a little more than a single standard
deviation.  But the probability of casting a decisive vote in California is so
low because it would require nearly an outlier of nearly six standard
deviations.  (That would be enough to even fool the notoriously conservative
particle physics community, who consider an outlier of five standard deviations
to be evidence of new physics.)  If the uncertainties were in fact distributed
as a Gaussian distribution, this would result in a .  

However, it is more likely that they only approximately have a Gaussian
distribution near the mean.  But in the tails this approximation would prove
much poorer.  In the tails the uncertainty becomes dominated by the systematic
uncertainty of the polls, and there is no easy way to model these.  One could
make a plausible argument that the tails are much fatter than a Gaussian would
imply, and hence that the odds of casting a decisive vote in California are
much higher than we calculated above (perhaps the pollsters are missing an
especially motivated demographic this cycle).  But one could make a plausible
argument going the other way, and the tails of the distribution are thinner
than a Gaussian, and in fact the probability we calculated was an
*overestimate*.  (After all, if California were really in play, one would think
there would be some other evidence of this even if it wasn't showing up in
polls.)

The difficulty of systematic errors is that when they are potentially large,
you have no other choice but to deeply understand where they are coming from so
that you can correct for them.

## Is a third party vote wasted?

So if your vote is (probably) not going to be decisive in California, should
you just vote for a third party candidate you better agree with instead?
Naturally it is *a fortiori* the case that if your vote for a major party
candidate is unlikely to be decisive, it is vastly less likely for it to be so
for a candidate polling at just a few percent.  But there are other thresholds
that fall short of victory which are nevertheless valuable.  In particular a
candidate that exceeds 5% of the national vote unlocks federal funding in the
following election.  In 2020 this grant is [$100
million](https://www.fec.gov/help-candidates-and-committees/understanding-public-funding-presidential-elections/presidential-spending-limits-2020/).

So let's calculate the expected value of a vote for the highest polling
third-party candidate in the 2020, Libertarian nominee Jo Jorgensen.  The
[RealClearPolitics](https://www.realclearpolitics.com/epolls/2020/president/us/general_election_trump_vs_biden_vs_jorgensen_vs_hawkins-7225.html#polls) polling average puts Jorgensen at 1.8%.

At this point we need to be a little careful with our choice of distribution.
For polls that are close to 50% with $$\sim$$4% uncertainty, a Gaussian
distribution is not terrible.  But this is clearly a poor distribution for a
candidate polling in single digits because it puts substantial odds that the
candidate will achieve negative votes!

Unfortunately doing a principled derivation of the correct distribution would
require a deep understanding of the the systematic uncertainties of these polls
(which I certainly do not possess).  So instead in the spirit of attempting to
obtain an order of magnitude estimate, we shall instead fly by the seat of our
pants.  What we would like is a reasonable distribution of outcomes for
Jorgensen that are consistent with a polling average of 1.8% and a $$\sim$$4%
uncertainty on the major party candidates.  Let us suppose that the 4%
uncertainty on the outcomes of the major party candidates were purely
statistical.  If this were the case then it would correspond to some effective
sample size $$N_{\textrm{eff}}$$ that consisted of a truly representative
sample of voters.

So what is the effective sample size?  The sample itself is drawn from a
binomial distribution, so its standard deviation is
$$\sqrt{N_{\textrm{eff}}p(1-p)}$$, and by the central limit theorem the
uncertainty on an estimate of $$p$$ is then $$\sqrt{p(1-p)/N_{\textrm{eff}}}$$.
Taking $$p \sim 1/2$$ for the major party candidates (remember this is just an
order of magnitude estimate!) we have 

$$
\frac{1}{2 \sqrt{N_{\textrm{eff}}}} = 0.04.
$$

Solving for $$N_{\textrm{eff}}$$ gives us an effective sample size of 156,
which we will round to 160 in the order-of-magnitude spirit.

With the effective sample size in hand, we can now turn to Bayesian analysis to
derive the distribution of outcomes for Jorgensen.

To do this let's turn to Bayesian
analysis.  Essentially we want to find $$p(f_L | \mathcal{D})$$, where $$f_L$$
is the fraction of votes for Jorgensen and $$\mathcal{D}$$ represents the data
that went into the polls.  From Bayes's Theorem, this probability is equal to

$$
p(f_L | \mathcal{D}) = \frac{p(\mathcal{D} | f_L) p(f_L)}{p(\mathcal{D})}.
$$

What should the prior $$p(f_L)$$ be?  For simplicity we'll use a beta
distribution as it is the conjugate prior for a binomial distribution.  But the
beta distribution has two hyperparameters, $$\alpha$$ and $$\beta$$ --- what
should they be?  Choosing a prior is oftentimes subjective.  A common choice is
to set $$\alpha = \beta = 1$$ which makes this distribution uniform and
therefore, in some sense, minimally informative, but this is not a good prior
in this situation.  It places the probability of Jorgensen achieving 1% of the
popular vote the same as her achieving 99%, which seems unlikely.

, which should give us an upper bound in our calculation of the
expected value of a .  But this is *not* a good prior.  It is not reasonable 

#### Measuring the effective sample size

We can then treat the 

where the logit is given by

% End with a note comparing voting to Jane Jacobs's statement about how
% secession is an emotional decision, not a rational one.
