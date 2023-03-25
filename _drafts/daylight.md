---
layout: post
title: How Fast the Days Are Getting Longer
date: 2023-03-20
categories: ml
image:
  feature: constellations3.jpg
---

As I write this here in the northern hemisphere the vernal equinox is quickly
approaching and the days are quickly longer.  One of my colleagues lives in
Stavanger, Norway and for the past six months I've been accustomed to seeing
the window in his background be pitch black because our team standup is at
6:30pm his time.  But he was on vacation and missed one meeting and when he
returned one week later his window had gone from pitch black to light.  This
led me to think about a basic astronomy question I had never given much thought
to before --- just how fast do the days get longer?

## How long is the Sun up for?

TODO: Derivation of the sunrise equation.

Ultimately this becomes

$$
H = \arccos (-\tan \lambda \tan \delta)
$$

To translate the hour angle into the number of hours the Sun is up for, we just
need to convert from an angle to hours and multiply by two (because the hour
angle just gets us the time from rising to culmination, but we also want the
time from culmination to setting).  So, if H is in radians,

$$
\begin{eqnarray}
t_{\textrm{daylight}} & = &
    2 \times \frac{24}{2 \pi} \times H \, \textrm{hr} \\
& = & \frac{24}{\pi} \times H \, \textrm{hr}
\end{eqnarray}
$$

So what is the declination of the Sun?  It varies over the course of the year,
but to first order it can be modeled very easily with a sinusoid as

$$
\delta = \epsilon \cos \left( \frac{d}{365} \right)
$$

where $$\epsilon$$ is the tilt of the Earth's rotation axis (the "obliquity of
the ecliptic" in the astronomical jargon), about $$23.45^{\circ}$$ (which is
about 0.409 in radians), and $$d$$ is just the number of days since the vernal
equinox.

Putting this all together, if you have a latitude and day of the year you can
calculate the length of daylight by using this formula:

$$
t_{\textrm{daylight}} \approx
    \frac{24}{\pi} \arccos \left(-\tan \lambda \tan \left(0.409 \times
    \frac{d}{365} \right) \right) \, \textrm{hr}
$$

### Daylight across the globe

TODO: What are some features at various latitudes?

TODO: An interactive Bokeh plot to show the daylight length over the year at a
specified latitude.

## The derivative of daylight

Now that we have an equation for the length of daylight, seeing how much it
changes is 

## Complications

### Atmospheric refraction

### The eccentricity of the Earth's orbit

## Footnotes
