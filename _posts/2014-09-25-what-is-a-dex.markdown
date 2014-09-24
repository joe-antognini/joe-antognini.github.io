---
layout: post
title: What is a dex?
date: 2014-09-24
categories: toolkits
---

The term "dex" comes up rather frequently in astronomy discussions and in
the literature, but is rarely defined in textbooks and a Google search
doesn't turn up many good definitions.  The idea of a dex is
straightforward---a dex is simply an order of magnitude.  

We use the term "order of magnitude" all the time, though, so why use the
term dex?  The reason is that it comes in handy when talking about fractions
of an order of magnitude.  It's particularly useful when talking about
metallicity.  Metallicity is measured logarithmically relative to the
abundance of metals in the Sun, and accordingly it must be unitless. 

As an example, let's take a look at Fischer & Valentini
(2005).  In this paper the authors find a correlation between the
metallicity of stars and the probability that the star hosts a
planet---stars with higher metallicities are more likely to host a planet.
This result is presented in Figure 5:

We can see that the sample of stars spans a range of [Fe/H] from -0.5 to
0.5, which is one order of magnitude, or one dex.  Although it was just as
easy to say order of magnitude as it was to say dex in that case, suppose we
asked how wide the bins in this histogram were.  There are ten bins spanning
an order of magnitude, so the width of each bin is a factor of $10^{0.1}
\approx 1.26$.  This is clumsy, so instead we simply say that each bin has a
width of 0.1 dex.

The metallicity of star A is 0.3 dex larger than star B.  This means that
the abundance of metals in star A is larger by a factor of $10^{0.3} \approx
2.0$. 
