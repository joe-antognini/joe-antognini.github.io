---
layout: post
title: Can the hot iron bar really compute?
date: 2022-06-25
categories: ml
image:
  feature: constellations3.jpg
---

In my [last post][1] I outlined the so-called "[triviality argument][2]" that
consciousness cannot be reduced to the process of computing a particular kind
of computer program.  The post generated some lively discussion on [Hacker
News][3] [and][5] [Reddit][4], and I had some good discussions with people about it
offline.  A number of commenters raised various objections to the argument as I
presented it, but most of the objections centered around the leap I made from a
computer that manipulates rocks in a field to the randomly fluctating states of
atoms in an iron bar.  The iron bar is not a *real* computer, according to
their argument, because the mapping from its states to the state of a Turing
machine is totally arbitrary.  Moreover, because this mapping is purely random,
*producing* this mapping essentially requires you to perform the computation
yourself --- so, to the extent that any computation is being performed, it's
really *you* who are computing, not the iron bar.

I think these objections are incorrect and still believe that a careful
understanding of what a computer really is will force us to accept that in some
cases the iron bar acts as a computer.  (Or that even if we reject this, we are
forced to reject the idea that consciousness can be reduced to computation.)
So in this post I want to make the leap from the "rocks in a field" computer to
the iron bar a little more deliberately so we can see what is really going on
in the argument.  I will proceed with a series of thought experiments.

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
the effect of sorting a list.  I can arrange the rocks on the input rows to
encode whatever list of integers I desire.  Then I follow the steps of my
program and when I finish in the halting state, the sequence of rocks on the
grid describes the same list that I started with, but sorted.

*The moral of the story*: A Turing machine is nothing more than manipulating a
sequence of bits by a particular set of rules.  By predetermining the right set
of state transitions and starting with the right set of inputs, I can use these
rocks to compute any computable function.  And, in point of fact, if we believe
that consciousness is a consequence of executing a particular kind of computer
program, this implies that I will be able to generate a conscious being by
shuffling the rocks in this desert appropriately.

## Thought Experiment № 2

### Wherein I tire of my game and automate it

Now I am a busy man and I don't have time to stand around in the desert all day
playing around with rocks.  So I build an automaton to do it for me.  It's a
complicated device full of pulleys and gears, but it does exactly what I did
all by myself.  When I press the "START" button it stands at a particular
column on the grid of rocks and detects whether the rock is in the upper or
lower row, it consults which state it is in by looking at which of the $$N$$
state boxes has a rock in it.  Then, depending on the rule, it moves the rock
in the input row from the top to the bottom or vice versa, updates its state
rock, and moves left or right.  It continues to do this until it puts the state
rock in the "HALT" box at which point it shuts down (assuming it ever arrives
at this point).  This is a very complicated machine to build, but after I am
done I am confident that it will always carry out the rules of the Turing
machine I have programmed.

*The moral of the story*: This machine is, of course, a canonical computer.  If
we believe that *anything* is a computer, it should include this machine I have
built.  It is a physical manifestation of a Turing machine.  It is easy to see
the correspondence between every state of the Turing machine and a physical
state of this machine.

## Thought experiment № 3

### Wherein I discover my machine's clone

Having automated my work of sorting lists, I relax by taking a long hike in the
desert.  One day during my travels I come across a very long line of rocks in
two rows and a machine that looks identical to the one I have built.  I open it
up and everything on the inside is just the same as the one that I built.  I do
not know who built this device or why.  I test it out by arranging some rocks
on the grid to represent a list, I press the "START" button and observe that it
does exactly what my machine would have done and ends up with a sorted list.

*The moral of the story*: For a device to be a computer it does not matter who
built it or what their intention was in building it.  It is sufficient that I
can guarantee that the device will appropriately follow the rules of the Turing
machine.

## Thought Experiment № 4

### Wherein I discover a mysterious Turing machine

I continue my hike.  A few days later, I discover a scene that is almost
identical to the one I saw last --- two rows of rocks and a device that appears
very nearly identical to mine.  The one difference is that this time the
machine has been welded shut, so I can't open it up and see what's going on
inside.  But I wonder if maybe this is a Turing machine just like the one I
built earlier to sort lists.

So I arrange the rocks on the input rows to give this machine a list of
integers in some arbitrary order, press the "START" button and watch it trundle
along and shuffle the rocks.  Lo and behold, it does exactly the same thing as
my own Turing machine did.  Every change to the input row is the same, every
state update is the same, and every move left or right is the same.  I try
running the machine on many different inputs and every time I run it, it
behaves exactly the same as the machine I built did.  In fact, I choose some
large number $$N$$, and try every possible input with $$N$$ bits or fewer, and
the machine behaves exactly as my machine does every single time.

Now we come to the first key question: Is this a computer?  On the one hand, I
have no idea how it works.  Maybe it just moves around randomly and I got lucky
with the inputs I gave it.  On the other hand, regardless of whether I got
lucky or not, I *did* give it a series of lists and it sorted them all.  And
what's more, it didn't just randomly permute the order of the rocks --- I could
see that it was implementing every step of a particular sorting algorithm.
Even though I don't understand exactly how the machine is detecting the
positions of the rocks or how it knows to transition the state rock correctly,
in practice it always seems to do the right thing.

At this juncture we have two options.  One option is to say that this is *not*
a computer because I do not understand how it works.  The other option is to
say that it *is* a computer because it behaves the way an ideal computer does.

Let's consider this first option.  It is certainly plausible!  I don't know
whether or not the machine I found has some internal mechanism to *guarantee*
that it always makes the correct updates.  By contrast, I built *my* computer
in order to compute a specific function, and I know that it was constructed in
such a way that no other outcome was possible.  But I cannot make any such
guarantees about a machine whose mechanism I do not understand.

But I do not believe this option is tenable.  If I say that the machine I found
in the desert is not a computer because I could have just gotten lucky with the
inputs I gave it, I am implicitly assuming that there is some source of
randomness.  But everything in the desert operates by the laws of classical
physicsa and is 100% deterministic.  In both cases there is just a collection
of atoms blindly obeying the laws of physics.  I understood the physical
mechanics at play in the first machine whereas I do not understand thim in the
second machine.  But in both cases the behavior is completely deterministic.
If I provide some inputs both machines always do the same thing.

If we reject this second machine as being a computer then, it has to come down
to *intent*.  The machine I built is a computer because I *intended* it to be a
computer.  But I do not know the intention of whoever it was that built this
other machine.  But this position forces us to accept some absurd conclusions.
If I built an atom-for-atom reproduction of my machine, but declared it to be
"art," you would be forced to accept that one of the machines is a computer and
the other is not, even though they are physically identical.  And, more
practically, it means that the devices we use every day and call "computers"
cannot really be computers because we can't be sure of the intention of the
people who built them.  (And, more relevant to the question of whether
consciousness can be reduced to computation, it implies that you cannot have
consciousness without some external being who built the computer and called it
a computer.)

So we are left with the second option.  This is to say that we can treat this
mysterious device as a computer because it does exactly what an ideal computer
should do.  This is the functionalist position and is the standard position in
the philosophy of computing (and in computer science more generally).  In this
position, it doesn't matter *how* the machine works or what the intent of its
builder was (or if there even was a builder).  The only thing that matters is
that it does the right thing.  We provide it with an input, and we observe that
it makes the sequence of operations that an ideal Turing machine would.

## Thought Experiment № 5

### A Turing machine on uneven ground

Some time later I go on another hike through the desert, this time with my
friend Alice.  We encounter another row of rocks and a machine that looks
identical to the one I built.  I tell Alice about the machine I saw in the past
and how it sorts list and say that maybe this one does the same.  So we arrange
the rocks on the input row to correspond to some list and press "START."  This
time, though, the machine does not correspond at all to the state transitions
of my machine.  We try running the machine on all sorts of inputs, but in every
case there is no correspondance to the machine I built.  I tell Alice that this
machine must be broken.

But after watching it for a while, Alice notices something.  We had assumed
that the northern row of rocks corresponds to "1"s and the southern row
corresponds to "0"s.  But the ground is somewhat uneven.  In each column, one
of two positions is higher than the other.  If we designate the higher position
to be a "1" and the lower position to be a "0", then the machine behaves
identically to the one that I built.  We set up an unsorted list of integers
using this new encoding and indeed when the machine finishes the 

*The moral of the story*: There is no unique correspondence between physical
states and states of the Turing machine.  The machine is still a computer even
if I do not immediately understand what its encoding is.

## Thought Experiment № 6

### A Turing machine on shaky ground

We continue our hike and arrive in an area with a strange geological
phenomenon.  Once every second, an earthquake rumbles through the area.  We see
that there is another long set of rows with rocks and a machine that looks
identical to my own.  But because of the earthquakes, we notice that once every
second some of the rocks randomly move from the top row to the bottom row or
vice versa.  We set up a list of integers to sort, press "START" and see what
happens.

As we watch the machine go, we notice that there are little seismometers in
each column.  They seem to be keeping track of how many times a rock got
jostled by an earthquake.  When the machine arrives at a particular column, in
checks the seismometer and if there were an even number of jostles, it treats
the northern row as a "1" and if there were an odd number it treats it as a
"0".  Once we figure this out, we see that every move the machine makes
correpsonds exactly to the Turing machine that I made.

*The moral of the story*: The encoding of a Turing machine does not need to be
constant over time.

## Thought Experiment № 7

### The subterranean Turing machine

Our hike continues and we arrive at an area with two long rows of rocks,
another set of boxes corresponding to states, but there's no machine there.
There's just a button on the ground that says "START."  We press it and to our
astonishment the rocks start to move, seemingly of their own accord.  We notice
that their movements correspond exactly to the movements of the Turing machine
I had built.  We spend a long time investigating this strange place.  We feed
it all sorts of lists and every time the rocks end up with a sorted list.

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
correct state changes.

Once again, the functionalist position is that it must have been computing all
along.  

*The moral of the story*: It doesn't matter if we see or understand the
mechanism by which these state changes take place.  All we have to do is verify
that the state changes are proceding according to the correct rules.

## Thought Experiment № 8

### An underground Turing machine on shaky ground

Finally we arrive at a new location, in the same region that has an earthquake
once per second.  Just as in the last location, there are two rows of rocks and
another rock outside those rows.  We arrange the rocks and press "START," and
the rocks start changing their position every second.  Now we have no idea
what's going on because we can't tell if a rock moves because of the earthquake
or because of a machine underground that we can't see.

We feed it some inputs, but all the movements look random to us.  Eventually we
dig underground and find that, not only is there a tunnel with a machine just
like the one I built, but there are also seismometers buried at each column so
that the machine can keep track of how many times a rock has been jostled.

Once we, too, can keep track of which rock are being moved by the machine and
which are being jostled by the earthquakes, we can verify that the machine has
been running my list sorting algorithm.

## Thought Experiment № 9

### The ghostly machine

## Thought Experiment № 10

### The machine thinks

## Thought Experiment № 11

### Wherein a hot iron bar attains consciousness

I now claim that there is no real difference between this last example and a
hot iron bar.

[1]: _posts/2022-06-17-consciousness.md

[2]: https://marksprevak.com/publications/triviality-arguments-about-computational-implementation-2018/

[3]: https://news.ycombinator.com/item?id=31791126

[4]: https://www.reddit.com/r/philosophy/comments/w3r6hb/consciousness_is_not_computation/

[5]: https://www.reddit.com/r/slatestarcodex/comments/vi158o/consciousness_is_not_computation/
