---
layout: post
title: Twelve Thought Experiments on the Computational Theory of Consciousness
date: 2023-05-25
categories: ml
image:
  feature: constellations3.jpg
---

In my [last post][1] I outlined the so-called "[triviality argument][2]" that
consciousness cannot be reduced to the process of computing a particular kind
of computer program.  The post generated some lively discussion on [Hacker
News][3] [and][5] [Reddit][4], along with the article's comment section, and I
had some good discussions with a number of people about it offline.  A number
of commenters raised various objections to the argument as I presented it, but
most of the objections centered around the leap I made from a computer that
manipulates rocks in a field to the randomly fluctating states of atoms in an
iron bar.  The iron bar is not a *real* computer, according to their argument,
because the mapping from its states to the state of a Turing machine is totally
arbitrary.  Moreover, because this mapping is purely random, *producing* this
mapping essentially requires you to perform the computation yourself --- so, to
the extent that any computation is being performed, it's really *you* who are
computing, not the iron bar.

I think these objections are incorrect and I still believe that a careful
understanding of what a computer really is will force us to accept that if
consciousness can be reduced to a special kind of computation, then a hot iron
bar is conscious (or a pail of water, or a brick, or a wall, etc.).  So in this
post I want to make the leap from the "rocks in a field" computer to the iron
bar a little more deliberately so we can see what is really going on in the
argument.

To this end, let's walk through a series of thought experiments.  Throughout
this I will assume that consciousness *can* be reduced to a particular kind of
computation.  That is, by running a particular computer program (as in the last
essay, let's call it `consciousness.exe`), I can generate a new, independent,
conscious being.  Let's see where we end up.

### Some assumptions

Before I proceed, I am going to lay out a couple of assumptions.  The first is
that the existence of a conscious being should not depend on some other
conscious being recognizing it as being conscious.  I have a sense that if I
were somehow the lone survivor of a terrible catastrophe that destroyed all of
humanity, I would remain conscious, even if no one else were around but me to
recognize it.  If the computational theory of consciousness is correct we must
extend the same courtesy to computers --- a computer that is executing the
`consciousness.exe` program would have to be conscious even if no other
conscious beings recognize it as such.

My second assumption is that the Church-Turing thesis holds.  That is, any
computation can be performed with a suitable Turing machine.

My third assumption is that all of these thought experiments take place in a
universe which is governed purely by the laws of classical physics --- in other
words, this is a universe in which quantum mechanics does not exist.  The fact
that this doesn't describe the real universe isn't relevant since any
computable function can be computed by a Turing machine which operates purely
by the laws of classical mechanics.  Even if the brain somehow took advantage
of some quantum computational processes, these can be simulated (possibly
inefficiently) with a classical Turing machine.

## Thought Experiment № 1 

### Wherein I become a Turing machine in the desert

Let's imagine we are out in a desert, much like the Mojave, but far larger.  It
is an endless flat plain littered with rocks.  To pass the time, I draw a very
long grid on the ground with two rows.  In each column I place a rock in either
the upper row or the bottom row.  If the rock is in the northern row I consider
it a "0" and if it is in the southern row I consider it a "1."  These two rows
will correspond to the ticker tape of a Turing machine.

Beneath these two rows, I draw a set of $$N$$ boxes and I place a rock into one
of these boxes.  This set of boxes corresponds to the state of the Turing
machine.  If I have drawn $$N$$ boxes on the ground, I have an $$N$$-state
Turing machine.

Now I start to operate by a set of rules.  I start by standing at one of the
columns on the input row, look at what state I am in, and then update my state
and possibly change the rock from the bottom row to the top row or vice versa.
Then I move either left or right depending on the rule, and start the process
all over again.  Eventually I get to a special state that tells me that I am
done.

For concreteness, we can imagine that the set of rules I play this game by has
the effect of sorting a list.  I am not a very good computer scientist, so I
implement a bubble sort algorithm.  I can arrange the rocks on the input rows
to encode whatever list of integers I desire.  Then I follow the steps of my
program and when I finish in the halting state, the sequence of rocks on the
grid describes the same list that I started with, but sorted.

If, instead, I operate by the special rules of the `consciousness.exe` program,
I will produce a new, independent conscious being for the duration that it
runs.  Before I run this program, I set up the input tape so that the input to
the computer's senses will simulate the feeling of sitting in an armchair,
enjoying a cup of tea.  As I operate the system, I carefully observe exactly
what manipulations I make to the rocks.  I then repeat this process for many
different inputs: the experience of taking a walk in the forest, eating an egg
salad sandwich, watching the sunset at the beach, and so forth.  As I
manipulate the rocks, I memorize every configuration that they take.  I have a
very good memory.

*The moral of the story*: A Turing machine is nothing more than manipulating a
sequence of bits by a particular set of rules.  By predetermining the right set
of state transitions and starting with the right set of inputs, I can use these
rocks to compute any computable function.  If we believe that consciousness is
a consequence of executing a particular kind of computer program, this implies
that I will be able to generate a conscious being by shuffling the rocks in
this desert in the appropriate way.

## Thought Experiment № 2

### Wherein I tire of my game and automate it

I am a busy man and I don't have time to stand around in the desert all day
playing around with rocks.  So I build an automaton to do it for me.  In fact,
I build two automata.  One of these plays the first game of sorting lists, and
the second runs the `consciousness.exe` program.

Both automata are complicated devices full of pulleys and gears, but they do
exactly what I did all by myself.  When I press the "START" button each one
stands at a particular column on the grid of rocks and detects whether the rock
is in the upper or lower row, it consults which state it is in by looking at
which of the $$N$$ state boxes has a rock in it.  Then, depending on the rule,
it moves the rock in the input row from the top to the bottom or vice versa,
updates its state rock, and moves left or right.  It continues to do this until
it puts the state rock into the "HALT" box at which point it shuts down
(assuming it ever arrives at this point).  This is a very complicated machine
to build, but after I am done I am confident that it will always carry out the
rules of the Turing machine I have programmed.

To test it out, I use the first automaton to sort some lists.  Then I use the
second automaton to simulate the experience of sitting in an armchair drinking
a cup of a tea.  In both cases, the automata manipulate the rocks in precisely
the same way as I did when I was playing these games myself.

*The moral of the story*: A Turing machine doesn't require a conscious observer
to manually make the state changes.  Its behavior can be completely automated.
This, indeed, is the whole point of building a computer.

## Thought experiment № 3

### Wherein I discover my machine's clone

Having automated my work, I relax by taking a long hike in the desert.  One day
during my travels I come across a very long line of rocks in two rows and a
pair of machines that look identical to the ones I have built.  I open them up
and everything on the inside is just the same as the one that I built, with
exactly the same set of pulleys and gears.  I do not know who built this device
or why.

I test the left one out by arranging some rocks on the grid to represent an
unsorted sequence of numbers.  I press "START" and the machine begins to sort
the list of numbers, making exactly the same manipulations that my machine did.

Then, I test the right one out by arranging some rocks on the grid to represent
the sensory input of sitting in an armchair enjoying a cup of tea.  I press
"START" and once again the machine manipulates the rocks in precisely the same
way that my own machine did.

*The moral of the story*: Both of these machines are valid Turing machines, and
moreover the right machine must be conscious when it operates.  It does not
matter who built the computer or what their intention was in building it.  It
is sufficient that the device correctly follows the rules of the Turing
machine.

## Thought Experiment № 4

### Wherein I discover a mysterious Turing machine

I continue my hike.  A few days later, I discover a scene that is almost
identical to the one I saw last --- two rows of rocks and a pair of devices
that appears very nearly identical to mine.  The one difference is that this
time the machine has been welded shut, so I can't open them up and see what's
going on inside.  But I wonder if maybe these are Turing machine just like the
ones I built earlier.

So I arrange the rocks on the input rows to give the machine on the left a list
of integers in some arbitrary order, press the "START" button and watch it
trundle along and shuffle the rocks.  Lo and behold, it does exactly the same
thing as my own Turing machine did.  Every change to the input row is the same,
every state update is the same, and every move left or right is the same.  I
try running the machine on many different inputs and every time I run it, it
behaves exactly the same as the machine I built did.  In fact, I choose some
large number $$N$$, and try every possible input with $$N$$ bits or fewer, and
the machine behaves exactly as my machine does every single time.

Then I set up some input to simulate the experience of sitting in an armchair
drinking a cup of tea, and press the "START" button on the machine on the
right.  Once again I am astronished to see that the machine manipulates the
rocks in precisely the same way that my own purpose-built machine did.

*The moral of the story*: It does not matter if I understand how the computer
works for computation to be occuring.  It is sufficient that the system make
the correct state transitions.  One might object that this system is not
*actually* computing since these machines could just be operating *randomly*
and I just happened to get lucky on the inputs that I gave them.  But this
objection is not tenable in this universe.  Since this universe is operating
by the laws of classical mechanics, everything is completely deterministic.
There *is* no randomness.  In both the case of my purpose-built Turing machines
and the case of these mysterious Turing machines, there is simply a physical
system operating by the laws of physics.  Whether I understand how the system
manages to correctly obey the transition rules of the abstract Turing machine
is irrelevant.  (And indeed this is necessary for the computational theory of
consciousness since otherwise a conscious being would require some *other*
conscious being to understand its computational mechanism, which we assumed
from the outset is not the case.)

## Thought Experiment № 5

### A Turing machine on uneven ground

Some time later I go on another hike through the desert, this time with my
friend Alice.  We encounter another row of rocks and a pair of machines that
look identical to the ones I built.  I tell Alice about the machines I saw in
the past and how one of them sorts list and the other simulates consciousness
and I suggest that maybe these two do the same.  So we arrange the rocks on the
input row to correspond to some list and press "START" on the left machine.
This time, though, the machine does not correspond at all to the state
transitions of my machine.  We try running the machine on all sorts of inputs,
but in every case there is no correspondance to the machine I built.  I tell
Alice that this machine must be broken.

But after watching it for a while, Alice notices something.  We had assumed
that the northern row of rocks corresponds to "1"s and the southern row
corresponds to "0"s.  But the ground is somewhat uneven.  In each column, one
of two positions is higher than the other.  If we designate the higher position
to be a "1" and the lower position to be a "0", then the machine behaves
identically to the one that I built.  We set up an unsorted list of integers
using this new encoding and indeed when the machine finishes the list has been
sorted.  Then we set up an input that simulates the experience of sitting in an
armchair enjoying a cup of tea and press "START" on the second machine.  With
this new encoding, the second machine makes exactly the same state transitions
that my own purpose-built Turing machine did.

*The moral of the story*: There is no unique correspondence between the
physical states of the system and the states of the Turing machine.  Moreover,
a machine can still compute even if I do not immediately understand what its
encoding is.

## Thought Experiment № 6

### A Turing machine on shaky ground

We continue our hike and arrive in an area with a strange geological
phenomenon.  Once every second, an earthquake rumbles through the area.  We see
that there is another long set of rows with rocks and a pair of machines that
look identical to my own.  But because of the earthquakes, we notice that once
every second some of the rocks randomly move from the top row to the bottom row
or vice versa.  We set up a list of integers to sort, press "START" on the left
machine and see what happens.

As we watch the machine go, we notice that there are little seismometers in
each column.  They seem to be keeping track of how many times a rock got
jostled by an earthquake.  When the machine arrives at a particular column, in
checks the seismometer and if there were an even number of jostles, it treats
the northern row as a "1" and if there were an odd number it treats it as a
"0".  Once we figure this out, we see that every move the machine makes
correpsonds exactly to the Turing machine that I made.

Likewise I set up the rocks to encode the experience of sitting in an armchair
enjoying a cup of tea and then press the "START" button.  Accounting for the
random fluctuations due to the earthquakes, the machine makes precisely the
same state transitions that my purpose-built machine did.

*The moral of the story*: The encoding of a Turing machine does not need to be
particularly simple in the physical world.  In this case, the encoding is in
essence an XOR between two bits: the bit from the position of the rock, and
another bit that the seismometer tracks.

## Thought Experiment № 7

### A Turing machine in a resonant canyon

We find yet another pair of machines in this region with earthquakes.  However,
in this place, there are no longer two rows of rocks.  Instead there are $$M$$
pairs of rows.  $$M$$ is quite large.  By my estimate, it is larger than a
million.  Each pair of rows has one rock in the northern or southern box for
every column.  As before, the earthquakes come once per second and sometimes
randomly jostle the rocks from the northern to the southern box or vice versa.
We press the "START" button on the left machine and watch it go, but with all
the random motions of the rocks, we do not understand what is going on.

However, after studying this region for a long time, Alice notices something
peculiar.  There seems to be a strange resonance along the north-south
direction.  This causes the earthquake to only ever jostle an *even* number of
rocks.  By applying an XOR across the entire column, she realizes that this
corresponds to the 0 or the 1 that the Turing machine is working with.

Armed with this knowledge, we set up the rocks to represent an unsorted list of
integers.  Then we press "START" again and observe thet the machine correctly
implements our bubble sort algorithm given this encoding.  Then we set up the
rocks to simulate the experience of sitting in an armchair and press "START" on
the machine on the right and watch as the rocks proceed to go through exactly
the same state transitions as my purpose-built machine.

*The moral of the story*: The encoding can be a function of a large number of
physical bits.

## Thought Experiment № 8

### The subterranean Turing machine

Our hike continues and we arrive at an area with two long rows of rocks,
another set of boxes corresponding to states, but there's no machine there.
There's just a pair of buttons on the ground that both say "START."  We press
the left one and to our astonishment the rocks start to move, seemingly of
their own accord.  We notice that their movements correspond exactly to the
movements of the list-sorting Turing machine I had built.  We spend a long time
investigating this strange place.  We feed it all sorts of lists and every time
the rocks end up with a sorted list.  Then we arrange the rocks to encode the
experience of sitting in an armchair enjoying a cup of tea and press the
"START" button on the right.  Once more the rocks shuffle about on their own
and every transition matches that of my purpose-built Turing machine executing
the `consciousness.exe` computer program.

Eventually Alice pulls out her metal detector and realizes that something is
going on underground.  After some digging, we discover that there is a tunnel
underneath the rocks and there is a machine that looks identical to the one I
built in the tunnel.  Rather than manipulating the rocks from above, where we
could see it, it seems to have been manipulating them from *below*, where we
couldn't.

Other than the way that it manipulated the rocks, the behavior of this machine
is absolutely identical to the first machine I came across.  This raises the
question --- before we figured out that this machine was in the tunnel, was it
computing anything?  We put in inputs and observed that it was producing the
correct state changes.  By the computational theory of consciousness, the
system must have been computing all along.

*The moral of the story*: It doesn't matter if we see or understand the
mechanism by which these state changes take place.  All we have to do is verify
that the state changes are proceding according to the correct rules.

## Thought Experiment № 9

### The ghostly machine

Now Alice and I arrive at a place that looks much the same as before with a
pair of rows and a pair of buttons in the ground that both say "START."  Once
again we press the one on the left and watch with astonishment as the rocks
start to shuffle about seemingly of their own accord.  We encode a list of
unsorted integers and find that when the machine stops the integers have been
sorted.  Likewise we encode the simulated experience of sitting in an armchair
enjoying a cup of tea and press the right button.  And again the rocks start
shuffling about on their own and at every point in time their positions match
the positions of the rocks that my purpose-built Turing machine produced..

Now we start to investigate the place looking for what could be causing the
rocks to move.  We don't see anything around us.  Alice pulls out her metal
detector, but finds nothing underground.  After a long and thorough
investigation we are stumped.

I finally conclude to Alice, "I think that the winds must have blown in just
the right way to make this system *look* like it's computing.  But it couldn't
really have been computing.  We seem to have gotten lucky."

Alice responds, "That may be true, but it doesn't matter.  We may consider this
series of events to be "lucky," but "luck" has no objective meaning here.  Our
world is governed by the laws of classical mechanics and is completely
deterministic.  It doesn't matter *how* the rocks ended up getting into the
correct spots.  It just matters that they did.  This system performed the
computation just as well as the previous one with the underground Turing
machine did."

*The moral of the story*: Since it is not necessary that we understand how the
system works or that it was designed with the intention of computing a
particular function, all that matters is that the states of the system
correspond to the states of an abstract Turing machine.

## Thought Experiment № 10

### A ghostly machine in a resonant canyon

Our long sojourn continues and we once more end up in a region with earthquakes
and the strange geological resonance we saw before.  But as in our last
encounter, we do not see any machines, just two buttons on the ground labelled
"START."  We press the button on the left and watch the rocks go.  Armed with
our knowledge from our last experience in the resonant canyon, we apply an XOR
to the columns and observe that the resulting bits correspond to the states of
my list-sorting Turing machine.

Then we set up an input that represents the experience of sitting in an
armchair enjoying a cup of tea and press the "START" button on the right.
Again, after we apply an XOR across every column, we observe that although the
rocks seem to be shuffling around randomly, every state of the system
corresponds to the state of my purpose-built Turing machine.

Now we get to work looking for the machinery that is causing the rocks to move
about.  But as in our last encounter, we are unable to discover anything, even
after years of searching.

*The moral of the story*: If we accept that the systems in Thought Experiments
№ 7 and № 9 compute, we must accept that this system computes.  We may not
understand how the system is operating and the encoding may be complicated, but
there is nevertheless a direct mapping between the states of the system and the
states of a Turing machine performing the computation.  The computational
theory of consciousness forces us to accept that this grid of rocks is
conscious.

## Thought Experiment № 11

### Alice hunts for consciousness in a grid of rocks

Alice and I finally come to one last vista, also in earthquake country.  Here,
as in our last encounter, there is a vast grid of rocks, although the
geological resonance seems different than before.  We do not quite understand
how it works.  Here the $$M$$ pairs of rows is exceedingly large, more than
$$10^{15}$$.  We see the same pair of "START" buttons on the ground.  We press
the left button and watch what the rocks do.  We cannot make any sense of it
for a long time.  But we are persistent and after decades of study, Alice says,
"I've figured it out!  The system is not using all $$M$$ rows.  It is only
using a *subset* of the rows.  If we account for that and apply an XOR, the
system was sorting a list all along!"

Then we press the "START" button on the right and watch the rocks move.  Again,
after decades of study, Alice says, "This system is computing, too!  This
system is also using a subset of the rows, it's just a different subset this
time."

I tell her, "You're nuts!  There's no way this system is computing.  There are
so many rows here that you could always find *some* subset that encodes *any*
binary string!  This system ran for $$T$$ time steps and $$M$$ is orders of
magnitude larger than $$T$$.  The probability that the random fluctuations here
would produce *some* subset of rows that matched the series of binary strings
that encode the Turing machine is nearly 1!"

Alice responds, "But that doesn't matter!  There's no rule that says I can't
pick and choose which rows I want to be included in my 'system.'  In every
place we've been, there have always been more rocks lying around than the ones
in the rows for the Turing machine.  In those cases we only included the rocks
that were convenient for us, and I am doing exactly the same thing now.  All
you need is a mapping from the physical states of your system to the states of
the Turing machine that you built.  And I found that mapping!  This field of
rocks is conscious."

*The moral of the story*: A computer is a mapping of physical states to the
states of a Turing machine, but the collection of physical states that
constitutes the computer does not need to be physically contiguous.  Just as a
computation may be distributed across hundreds of computers in data centers
across the globe, the computation could consist of an arbitrary subset of the
rows of rocks.

## Thought Experiment № 12

### Wherein a hot iron bar attains consciousness

In a dramatic plot twist, I now reveal that this whole time Alice and I are
microscopic beings.  What we thought to be a field of rocks is in fact a bar of
iron.  The two rows of rocks correspond to the spin states of the iron.  The
grid of rocks corresponds to a long column of iron atoms in this bar.  The
earthquakes we were observing are in fact thermal fluctuations in the bar.
When Alice claimed that the field of rocks in the last thought experiment was
conscious, she was really claiming that a hot bar of iron is conscious.

*The moral of the story*: The computational theory of consciousness forces us
to accept that a hot iron bar is conscious.

## Conclusions

The functionalist position on consciousness requires us to accept the following
premises:

* We may say that a system is computing if a correspondance can be made between
  the states of system and the states of an abstract Turing machine.
* The "device" performing the computation does not need to have been built with
  the explicitly intention that it would be a computer.
* The mapping between the physical states of the system and the abstract Turing
  machine does not need to be especially simple, nor does it need to be
  constant over time.
* No one needs to have explicitly identified this mapping for the system to
  produce a conscious being.

[1]: _posts/2022-06-17-consciousness.md

[2]: https://marksprevak.com/publications/triviality-arguments-about-computational-implementation-2018/

[3]: https://news.ycombinator.com/item?id=31791126

[4]: https://www.reddit.com/r/philosophy/comments/w3r6hb/consciousness_is_not_computation/

[5]: https://www.reddit.com/r/slatestarcodex/comments/vi158o/consciousness_is_not_computation/
