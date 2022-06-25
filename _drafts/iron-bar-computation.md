---
layout: post
title: Can an iron bar really compute?
date: 2022-06-25
categories: ml
image:
  feature: constellations3.jpg
---

In my [last post][1] I outlined the so-called "[triviality argument][2]" that
consciousness cannot be reduced to the process of computing a particular kind
of computer program.  The post generated some [lively discussion][3] on Hacker
News.  A number of commenters raised various objections to the argument as I
presented it, but most of the objetions centered around the leap I made from a
computer that manipulations rocks in a field, to the states of atoms in an iron
bar.  The iron bar is not a *real* computer since the mapping from its states
to the state of a Turing machine is totally arbitrary.  Moreover, because this
mapping is so arbitrary, *producing* this mapping essentially requires you to
perform the computation yourself --- so it's really *you* who are computing not
the iron bar.

I think these objections are incorrect and that a careful understanding of what
a computer really is will force us to accept that in some cases the iron bar is
a computer.  (Or that even if we reject this, we are forced to reject the idea
that consciousness can be reduced to computation.)  So in this post I want to
make the leap from the "rocks in a field" computer to the iron bar a little
more deliberately so we can see what is really going on in the argument.

## I become a Turing machine

Let's imagine we are out in the Mojave desert.  It is an endless flat plain
littered with rocks.  I draw a very long grid on the ground with two rows.  In
each column I place a rock in the upper row or the bottom row.  If the rock is
in the upper row I consider it a "1" and if it is in the bottom row I consider
it a "2."  These two rows will correspond to the ticker tape of a Turing
machine.

Beneath these two rows, I draw a set of $N$ boxes and I place a rock into one
of these boxes.  This set of boxes corresponds to the state of the Turing
machine.  If I have $N$ boxes, I have an $N$-state Turing machine.

Now I start to operate by a set of rules.  I start by standing at one of the
columns on the input row, look at what state I am in, and then update my state
and possibly change the rock from the bottom row to the top row or vice versa.
Then I move either left or right and start the process all over again.
Eventually I get to a special state that tells me that I am done.

For concreteness, we can imagine that my set of state transitions sorts a list.
I can arrange the rocks on the input rows to be whatever list of integers I
want, I follow the steps of my program, and at the end of it I am left with a
sorted list.

There's nothing particularly new here, I am just acting as a Turing machine.
By predetermining the right set of state transitions and starting with the
right set of inputs, I can compute any computable function.  And, in point of
fact, if we believe that consciousness is a consequence of executing a
particular kind of computer program, I will be able to generate a conscious
being by shuffling the rocks in this desert appropriately.

## An automatic Turing machine

Now I am a busy man and I don't have time to stand around in the desert all day
playing around with rocks.  So I build an automaton to do it for me.  It's a
complicated device full of pulleys and gears, but it does exactly what I did
all by myself.  When I press the "START" button it stands at a particular
column and detects whether the rock is in the upper or lower row, it consults
which state it is in by looking at which of the $N$ state boxes has a rock in
it.  Then, depending on the rule, it moves the rock in the input row from the
top to the bottom or vice versa, updates its state rock, and moves left or
right.  It continues to do this until it puts the state rock in the "HALT" box
at which point it shuts down (assuming it ever arrives at this point).

This machine, of course, is a canonical computer.  If we believe that
*anything* is a computer, it should include this machine I have built.

## A mysterious Turing machine

Now I go hiking in the desert.  One day during my travels I come across a very
long line of rocks in two rows and a machine that looks identical to the one I
have built.  I don't want to accidentally break it so I can't open the machine
up and see what's going on inside.  But I wonder if maybe this is a Turing
machine just like the one I built earlier to sort lists.

So I arrange the rocks on the input rows to give this machine a list of
integers in some arbitrary order, press the "START" button and watch it trundle
along and shuffle the rocks.  Lo and behold, it does exactly the same thing as
my own Turing machine did.  Every change to the input row is the same, every
state update is the same, and every move left or right is the same.  I try
running the machine on many different inputs and every time I run it, it
behaves exactly the same as the machine I built did.  In fact, I choose some
large number $N$, and try every possible input with $N$ bits or fewer, and the
machine behaves exactly as my machine does every single time.

Now we come to the first key question: Is this a computer?  On the one hand, I
have no idea how it works.  Maybe it just moves around randomly and I got lucky
with the inputs I gave it.  On the other hand, I gave it a series of lists and
it sorted them all.  And what's more, it didn't just randomly permute the order
of the rocks --- I could see that it was implementing every step of the
quicksort algorithm.  Even though I don't understand how exactly it's detecting
the positions of the rocks or how it knows to transition the state rock
correctly, it always does the right thing.

We now have two options.  One option is to say that this is not a computer
because I do not understand how it works.  Because I don't know how it works, I
don't know if it has some internal mechanism to *guarantee* that it always
makes the correct updates.  By contrast, I built my computer in order to
compute a specific function, and I know that it was constructed in such a way
that no other outcome was possible.  I cannot make any such guarantees about a
machine whose mechanism I do not understand.

But I do not believe this option is tenable.  If I say that the machine I found
in the desert is not a computer because I could have just gotten lucky with the
inputs I gave it, I am implicitly assuming that there is some source of
randomness.  But everything in the desert is very large --- everything is
purely classical and 100% deterministic.  In both cases there is just a
collection of atoms blindly obeying the laws of physics.  I understood the
physical mechanics at play in the first machine whereas I do not understand
thim in the second machine.  But in both cases the behavior is completely
deterministic.  If I provide some inputs both machines always do the same
thing.

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

## Turing machines on uneven ground

Some time later I go on another hike through the desert, this time with my
friend Alice.  We come across another row of rocks and a machine that looks
identical to the one I built.  I tell Alice about the machine I saw in the past
and how it sorts list and say that maybe this one does the same.  So we
arrange the rocks on the input row to correspond to some list and press
"START."  This time, though, the machine does not correspond at all to the
state transitions .  I tell Alice that this machine must be broken.

But after watching it for a while, Alice notices something.  We had assumed
that the top row of rocks corresponds to "1"s and the bottom row corresponds to
"0"s.  But the ground is somewhat uneven.  In each column, one of two positions
is higher than the other.  If we designate the higher position to be a "1" and
the lower position to be a "0", then the machine behaves identically to the one
that I built.

## A Turing machine on shaky ground

We continue our hike and arrive in an area with a strange geological
phenomenon.  Once every second, an earthquake rumbles through the area.  We see
that there is another long set of rows with rocks and a machine that looks
identical to my own.  But because of the earthquakes, we notice that once every
second the rocks randomly move from the top row to the bottom row.  The machine
also operates at one step per second in the interval between the earthquakes.
We set up a list of integers to sort, press "START" and see what happens.

As we watch the machine go, we notice that there are little seismometers in each
column.  They seem to be keeping track of how many times a rock got jostled by
an earthquake.  When the machine arrives at a particular column, in checks the
seismometer and if there were an even number of jostles, it treats the top row
as a "1" and if there were an odd number it treats it as a "0".  Once we
figure this out, we see that every move the machine makes correpsonds exactly
to the Turing machine that I made.

## The underground Turing machine

Our hike continues and we arrive at an area with two long rows of rocks,
another set of boxes corresponding to states, but there's no machine there.
There's just a button on the ground that says "START."  We press it and to our
astonishment, the rocks start to move seemingly of their own accord.  We notice
that their movements correspond exactly to the movements of the Turing machine
I had built.  We spend a long time investigating this strange place, we feed it
all sorts of lists and every time the rocks end up with a sorted list.

Eventually Alice pulls out her own seismometer and realizes that something is
going on underground.  With some work we discover that there is a tunnel
underneath the rocks and there is a machine that looks identical to the one I
built in the tunnel.  Rather than manipulating the rocks from above, where we
could see it, it seems to have been manipulating them from *below*, where we
couldn't.

Now the behavior of this machine is absolutely identical to the first machine I
came across.  This raises the question --- before we figured out that this
machine was in the tunnel, was it computing anything?  We put in inputs and
observed that it was producing the correct state changes.

Once again, the functionalist position is that it must have been computing all
along.  It doesn't matter if we see or understand the mechanism by which these
state changes take place.  All we have to do is verify that the state changes
are proceding according to the correct rules.

## An underground Turing machine on shaky ground

Finally we arrive at a new location, in the same region that has an earthquake
once per second.  Just as in the last location, there is two rows of rocks and
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

## Does the machine matter?

## The hot iron bar

I now claim that there is no real difference between this last example and a
hot iron bar.

[1]: _posts/2022-06-17-consciousness.md

[2]: https://marksprevak.com/publications/triviality-arguments-about-computational-implementation-2018/

[3]: https://news.ycombinator.com/item?id=31791126
