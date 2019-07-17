---
layout: post
title: Reflections on the Google AI Residency One Year On
date: 2019-07-15
categories: personal
image:
  feature: constellations3.jpg
---

About a year ago I finished up a year of doing machine learning research at
Google as a Google AI Resident.  (Technically when I started I was a Google
Brain Resident, but midway through the powers that be decided to rebrand the
program.)  I was in the second cohort so the program as a whole was still having
a few teething issues, but it was nevertheless an extraordinarily valuable
experience.

## Application and interview

I think I first heard about the Google Brain Residency from one of Jeff Dean's
tweets and decided to apply almost on a whim.  The cover letter was probably the
most important part of the application.  I treated it almost like a short
reesarch proposal, starting with some unifying threads in my past work and
explaining how they were motivating the questions I wanted to answer at Google
(and why Google would be a great place to try to solve those problems).  In my
case I had been working at a company called [Persyst](https://www.persyst.com)
that does machine learning to interpret EEG data.  Most of my work there had
been working with EKG data to robustly identify heart beats in noisy conditions.
Heart beats can be picked up by the EEG and look very similar to a feature that
is characteristic of epilepsy and could confuse the other classifiers.

As I was trying to build a system that would work even in conditions that it
hadn't been trained on I was thinking more generally about the problem of how to
determine if a neural network has seen something similar to a given data pointor
if it's wildly different form anything it's seen before.  This is distinct from
(though related to) the problem of calibrating the uncertainty of a neural
network.  As an illustration, imagine a NN that was trained to classify
handwritten 1s and 0s.  If you give the NN a very narrow 0, it will return a
confidence of around 0.5.  But if you provide the NN with something like a
pattern of white noise then it will still probably return a confidence of 0.5
even though this example is quite different than a narrow 0.  Unfortunately just
rejecting anything that's classified with a confidence close to 0.5 isn't good
enough because there's also out-of-distribution data that the NN will classify
into one or the other classes with high confidence.  If you give the NN the
letter "t", for example, it will probably think that looks much more like a 1
than a 0 and so will classify it accordingly with high probability.  Adversarial
examples are the extreme limit of this out-of-distribution problem where you
manage to construct an example which perceptually belongs to one class, but the
NN classifies in another class with high probability.

I was fortunate to then be selected for a phone screen where I was interviewed
by Kevin Murphy.  The phone screen mostly focused on the machine learning work
that I had done and delved a little bit into what I wanted to do at Google.  I
believe most candidates had a second phone screen that focused on coding, but I
had previously received an offer from Google for a SWE role so they may have
waived that.

The phone screen went well and I was selected for an onsite interview in late
February.  During the onsite we were given a tour of Google Brain (they had some
robots running around, which made it especially cool!), and got to see a few
short presentations by Brain Residents from the previous cohort about their
research, but of course the reason we were all there was for the interviews.
The interview had two components: a machine learning interview and a programming
interview.  I thought that the programming interview went okay, though not
great, but I thought that I had completely bombed the machine learning
interview.  When I got home I was happy that I had gotten as far along in the
interview process as I did, but was fully prepared to receive a rejection.  But
to my surprise about a month later I heard that I had been accepted!

## Orientation

There ended up being about 30 AI residents in my cohort.  As AI Residents we
were technically "fixed-term full time employees" (so, not contractors or
interns).  As such we went through the Google's normal two-day employee
orientation.  After this we had a separate orientation specific for AI residents
that lasted about two week.  Each of us got an "orientation mentor" who showed
us the ropes about how to do basic things within Google Brain and was someone we
to whom we could ask questions.  (There were varying degrees of helpfulness from
the orientation mentors.  My mentor, Patrick Nguyen was great, but I think some
residents never saw their orientation mentor at all.)  We also went through a
crash course in deep learning taught by Chris Olah.

During this time we also chose a topic for a "mini-project" that we would carry
out to practice working with Tensorflow and Google's infrastructure.  In my case
I decided to train a model to generate captions for New Yorker cartoons.  It
turned out that someone at Google Brain (Chris Shallue) had already done a
project like this, so some code was already available and my plan was to add
some more data to the training set to see if the results improved.

## Research

### Audio textures

### Batch size

### PCA of random walks

## Coming to an end
