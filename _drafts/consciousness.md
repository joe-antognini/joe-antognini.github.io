---
layout: post
title: Consciousness is not computation
date: 2022-02-19
categories: ml
image:
  feature: constellations3.jpg
---

If you spend enough time in the tech world, you will quickly find that it's a
common article of faith that computers will one day gain consciousness.  With
big enough computers and sophisticated enough AI, the reasoning goes, it is
inevitable that sooner or later computers will become conscious just as we are.
In fact, some have made the bolder claim that this isn't merely something that
will happen in the distant future future, but that this day is upon us already.
David Chalmers [famously][1] [argued][2] that we must be open to the idea that
any feedback system, even one as simple as a thermostat, is conscious, even if
in a limited way.  And recently AI researcher Ilya Sutskever [speculated][3]
that today's neural networks may be conscious.

But the idea that consciousness is a special kind of computation is wrong.  Not
only is it wrong, an examination of what computation really is shows the
position to be essentailly incoherent.  Computation alone is insufficient to
produce consciousness.

This is, as I understand it, not a radical position among philosophers of the
mind these days.  The idea that consciousness could be computation gained some
currency back in the 1960s and 1970s as general purpose computers were being
developed and the theoretical tools to formally study computation were
codified.  It was clear as this was happening that a new paradigm was emerging.
Explaining conciousness had been one of the thorniest problems of philosophy
since the time of Descartes --- could this radical new paradigm of computation
explain it?

But a handful of arguments in the late 1970s and early 1980s cast doubt on this
new idea, with John Searle's Chinese Room argument being the most influential.
The Chinese Room argument has had its share of critics, but today, some forty
years later, my sense is that it has .

But I think that the point that the Chinese Room argument is really making can
sometimes get obscured by the details of the thought experiment, so 


This position started to gain some currency among philosophers who studied
philosophy of mind back in the 1960s and 1970s as the [TODO funnctionalism?] .
As general purpose computers were being developed and the theory behind
computer science , and was clear that a new paradigm was emerging.  Explaining
conciousness had been one of the thorniest problems of philosophy since the
time of Descartes --- could this radical new paradigm of computation explain
it?  the idea is But a trio of three counter-arguments around the same time.  Philosophy moves fairly slowly, but I
think it's safe to say that today, 50 years on, the position that consciousness
is computation is not widely held.


The argument that consciousness is not computation [TODO footnote note that
computation may be *necessary*, but it cannot be sufficient] has two parts.
The first is that  [qualia exists] .  The second half is that computation
cannot produce these feelings.

* Qualia is distinct [What Mary Knows]
* System 

So why is it that 


## Some preliminaries

### What I mean by "consciousness"

Before getting too deep we need a working definition of consciousness.  This is
one of the trickiest concepts to define rigorously since it seems that a
rigorous definition of consciousness practically requires a theory of
consciousness itself.  To make matters worse, in these kinds of discussions it
oftentimes gets mingled with related ideas of self-awareness and intelligence.
But in this post I am interested only in consciousness as a sort of perception
--- an awareness of being, or, more loosely, "what it feels like to be
something."

This aspect of consciousness is sometimes called "qualia." [^1] The classic
argument that qualia exists is due to Frank Jackson in the article "What Mary
Didn't Know."  I encourage you to read the original article (and the Wikipedia
article), but in brief, the argument proposes a thought experiment: Suppose
there is a scientist named Mary.  Through extensive study, she has learned all
there is to know about the physics of color, the physiology of the eye, and the
neurology of the brain.  Given some stimulus like looking at a red rose, she
knows exactly how the light impacts the eye, how the image forms on the retina,
how this produces a signal along the optical nerve, and how the brain processes
this signal.  However, Mary has lived her entire life within a black and white
room and has never perceived color herself.  One day, she leaves the room and
looks at a red rose.  Does she learn anything new from this experience?  If she
does, we are forced to conclude that qualia exists --- that an experience is
distinct from perfect knowledge of how the brain reacts to the stimuli that
produced that experience.

But if we accept that qualia exists (which, after all, seems intuitively
sensible), we are burdened with the apparently impossible task of explaining
how consciousness is generated by physical processes.

#### Consciousness is observer independent

It's worth pausing here and noting one useful property of consciousness:
consciousness is independent of external observers.  By this I mean that my
consciousness does not depend on other observers perceiving me to be conscious.
Even if everyone else in the universe should deny that I am
conscious --- or if those other observers did not exist at all --- this would
have no bearing on my own consciousness.  If, in a terrible apocalypse all life
on Earth should die, except by some strange fortune my own, my consciousness
would not suddenly disappear.

### What is computation?

Next we need a working definition of computation.  Fortunately this is an idea
that is much less fuzzy than consciousness.  Computation, in the broadest
sense, is the manipulation of symbols according to an algorithm.  The largest
and most important category of computation are those algorithms which can, in
principle, be executed on a Turing machine.  As far as we know, every algorithm
that can be run on a physical computer can also be run on a Turing machine (and
the statement that this is necessarily true is known as the Church-Turing
Thesis).  [^2]

#### What is a computer?

This then brings us to the companion question of what exactly constitutes a
computer.  Now, a Turing machine is a purely mathematical abstraction, like a
circle or a logarithm.  We can manifast things in the real world which can be
well modeled by a circle, but the abstract idea of a circle is distinct from a
drawing of a circle.

Likewise we can build an object in the real world which can model the behavior
of the abstract Turing machine.  And, more practically, we can build devices
whose behavior, while not identical to that of a Turing machine, can compute
the same things as some Turing machine.  We call such devices computers.

How accurate does such a device have to be to be considered a computer?  After
all, any physical manifestation of a Turing machine will be an approximation of
the abstract concept, just as any drawing of a circle won't be exactly
circular.  Sometimes the computer will make a mistake --- a cosmic ray will fly
through and flip a bit for example. [^3]  If we decide that a machine is not a
computer simply because it ever makes *any* errors, we will have to conclude
that there are no computers at all in the real world.  And if computers don't
exist, then consciousness cannot be computation.

But this is far too strict a requirement.  A more reasonable definition of a
computer is that it is a machine which produces outputs which correspond to
those of an ideal Turing machine's given the same inputs. [^4]  If it makes a
mistake somewhere and breaks that correspondance, then it stops being a
computer for the time being, or at least a computer corresponding to that
particular Turing machine.

This is a useful definition because it abstracts away the internal physical
workings of the computer.  The computer can use transistors or vacuum tubes or
something else entirely, and we can just focus on what the abstract Turing
machine is doing.  As long as the states and outputs correspond to what you
would get with a Turing machine (no matter what physical mechanism is producing
those states and outputs), we can fairly call the device a computer.

## Consciousness in a field of rocks

Since computation is independent of the physical mechanism it uses to transform
its states and produce outputs, we can imagine (impractical) computers that are
made out of things other than electronics.  We can create mechanical computers
out of [balls falling down a pegboard][4].  A wonderful cartoon from [XKCD][5]
imagined a limit of this principle.  The cartoon imagines an individual who
finds himself in a vast desert filled with rocks.  to allay his boedom, he
manipulates the rocks to produce a computer and simulate the entire universe,
instant by instant.

Now, if consciousness were a consequence of pure computation, it would be
possible to write a very clever computer program (let's call it
`consciousness.py`) that, when executed on a big enough computer, produces a
conscious being.  But computation is indepednent from the physical substrate
that the computation is performed on.  So if a powerful supercomputer can
produce consciousness by running `consciousness.py`, we should also be able to
produce a conscious being by running the same `consciousness.py` program by
manipulating rocks in a desert.

## Does iron become conscious when it's hot?

Now it already seems implausible to me that a vast desert of rocks being
manipulated into various patterns is conscious.  Nevertheless this argument
doesn't convince everybody.  Some believe that while it might be hard to
imagine what it means for this vast desert of rocks to be conscious, there are
lots of unintuitive things in this world.  We shouldn't let our prejudices as
to what substrate consciousness *should* exist in prevent us from accepting
that it could very well exist in a substrate which is unfamiliar to us. [^5]

But let's now follow where this argument takes us.  Rather than manipulating
rocks in a desert, let's imagine a bar of iron heated past the Curie
temperature.  Each atom in the bar has a magnetic moment which points either up
or down.  For simplicity, let's assume that the bar is very hot and that the
magnetic moment of each atom is randomly flipping between up and down.
Moreover we have the means to observe whether the magnetic moment of every atom
in the bar is up or down at any given time.

I want to determine if this bar of iron is consciousness, so I examine its
atoms to see if it is running `consciousness.py`.  I designate the first $N$
atoms to be input bits, another $N$ atoms to be internal states of the Turing
machine, and then another $N$ atoms to be outputs.  Then I look at the magnetic
moments of those atoms sampled at different time steps and see if they
correspond to the inputs, outputs, and intermediate states of
`consciousness.py` by designating a moment pointing "up" as a 1 and a moment
pointing "down" as a 0.  Naturally, there is no correspondance so I conclude
that the bar of iron is not conscious.

Simultaneously, however, my friend Alice performs the same observation.  But
rather than designating atoms pointing "up" as a 1 and a moment pointing down
as a 0, she considers an atom pointing up to be a 1, unless it's the first atom
in teh bar, in which case it's a 0.  Naturally, she, too, observes no
correspondance with `consciousness.py` and concludes that the bar of iron is
not conscious.

But another friend of mine, Bob, makes the same observation, but uses a
slightly different encoding.  He considers an atom pointing up to be a 1,
unless it's the second atom in the bar, in which case it's a 0.  Simiarly Carl
performs the same observation, but in his encoding, an atom pointing up is a 1
unless it's the third atom, and so on.  Eventually we get to Ada, who encodes
an atom pointing up as a 1 unless it's the first or second in which case it's
a 0.  Then Barbara, who encodes an atom pointing up as a 1 unless it's the
first or third.

Continuing this, we can imagine an enormous crowd of observers staring at this
iron bar, each using a unique encoding of atomic states to bits.  With a
sufficiently large number of observers, one of them will, by chance, happen to
observe that the states of the atoms correspond exactly to the bits of a Turing
machine computing `consciousness.py`.  This observer will then conclude that
the bar of iron is a computer running `consciousness.py` and is therefore
concsious.

But!  If a single observer can correctly determine that the bar of iron is
conscious, we must conclude that the bar of iron is conscious for *everybody*,
because concsiousness is observer independent.  If true honest-to-God
concsiousness is just a matter of running `consciousness.py`, we have indeed
found someone who has correctly observed the bar of iron to run
`consciousness.py` and we must conclude that the bar of iron *really is
conscious*.

To go further, I have not specified what `consciousness.py` is, and presumably
there are many possible `consciousness.py` programs.  There is
`joes_consciousness.py` and `dear_readers_consciousness.py`, which are the
programs that generate my consciousness and yours, dear reader, respectively.
And this bar of iron is running *all of them*.  So not only is the bar of iron
conscious, it contains my consciousness, your consciousness, and *all possible
consciousnesses*.

And of course there's nothing special about the iron itself.  We could make the
same argument with any system where we can map states to bits.  We could
imagine doing the same thing with a large enough number of coin tosses or the
locations of atoms in the air of a room.  In all cases we are forced to
conclude that a sufficiently large system contains all possible
consciousnesses.  So the proposition that consciousness is computation leads
quite inextricably to a sort of panpsychism.  But even if we could stomach a
classical panpsychism that has a vague sense that all things are conscious,
even if in a very limited way, this goes far beyond that.  We are forced to
conclude that large groups of atoms aren't merely vaguely conscious, but they
contain *all* consciousnesses, including our own.

## But computers can still be conscious!

Now I want to be quite clear about the position I am arguing for.  By saying
that consciousness is not computation, I am *not* claiming that computers are
not or never can be conscious.  We could imagine a world in which consciousness
is produced by electric fields that fluctuate in the right patterns.  Perhaps,
in such a world, a digital computer running `consciousness.py` produces the
right patterns just as the neurons in the brain do.

But in this world, consciousness is, at root, a *physical* phenomenon, not a
purely computational phenomenon.  Computation may be necessary to produce
consciousness, but my claim is that it cannot be sufficient.  I can run
`consciousness.py` on a digital computer and produce a conscious being, but if
I run the same program on the "rocks in a desert" computer or the "hot iron
bar" computer, I will not.  In this case, consciousness is then
hardware-dependent.  But computational phenomena are independent of the
hardware they are run on. If consciousness were a purely computational phenomenon,
this would not be possible.  Any machine that runs the same computation would
produce the same phenomenon.

## Syntax is not semantics

The argument that computation is not consciousness can be summed up in a single
slogan: syntax is not semantics.  All computers can do is shuffle lumps of
matter around, whether that be rocks in a vast desert, or states of voltage .
But these lumps of matter have no intrinsic meaning.  The only reason we call a
box with a CPU in it a "computer" is because the operation of the voltages
across different parts of the CPU happen to map onto bits that we have defined,
and when these voltages interact they do so according to the rules of a set of
logical operations which we have defined.  But there is no meaning to the
physical system apart from what we, as external observers, have imposed on it.

Of course it is simplest to build a computer where the high voltage states
correspond to 1s and the low voltages states 0s.  But there is no requirement
to build a computer that way.  We could build a perfectly valid computer where
the high voltage states of even valued states correspond to 1s and where they
correspond to 0s in the odd valued states.  The system only "computes" because
of the way we have encoded information.

So computer simulations can never , since the "simulation" is not an
independent system.  It is only defined in terms of its relation to an external
observer.  A simulation of a brain cannot produce consciousness any more than a
simulation of the weather can produce rain.

## So what is consciousness then?

The idea that consciousness comes from computing a particular kind of program
is seductive because it seems to lay out a path towards understanding where
consciousness comes from.  If only we could write a clever enough computer
program, we could figure it out.

But if consciousness is not computation, then what is it?  This, of course, is
perhaps the hardest problem there is.  I don't claim to have the answer to this
question, but I think there are a few properties of consciousness that we have
to explain if we want a good theory of consciousness.

### Consciousness is in the brain

The first mots basic fact about consciousness is that consciousness seems to be
very closely linked to the brain.  This has been suspected since antiquity and
modern neuroscience backs up this intuition.  My consciousness does not fall
off my body if I clip off a fingernail or even chop off my arm.  But if a
neurosurgeon slices off a piece of my brain, or severs some connections, my
consciousness may radically alter.  If my body is functioning but my brain is
not, I will not have consciousness, whereas if my brain is functioning, my body
can be in very bad shape and I can maintain my consciousness.

So clearly consciousness has something to do with what is going on the brain,
and any theory of consciousness needs to explain the connection between what is
going on in the brain and qualia.  Beyond that, such a theory needs to explain
why the *rest* of me is apparently *not* conscious.  There is something special
going on in the brain and only the brain (as far as we can tell) that seems to
produce consciousness.

### Consciousness is unitary

The second important property of consciousness that any theory needs to explain
is that consciousness is a single, individual experience.  My consciousness is
of my entire self.  It is not of half of myself, nor is it of some
superposition of you and me.  Somehow, whatever is going on in my brain to
produce my consciousness contains my whole brain, not just a subset of it, and
that it doesn't also include anyone else's brain.

Some individuals with severe epilepsy have to have the corpus callosum severed.
The corpus callosum joins the left hemisphere to the right hemisphere.  Once
these individuals have the corpus callosum severed, they seem to exhibit having
*two* consciousnesses rather than one.


The "consciousness is computation" argument essentially fails to account for
this fact.  Since "a computing system" is not well defined in physical space,
it's impossible to say where the computer ends and the rest of the world
begins.  We are fooled by the fact that the computers we are familiar with are
put in neat boxes, but if our computer is just a bunch of rocks on the sand the
limits of the "computer" are much less clear.  If I toss a new rock into the
mix does that join the consciousness?  The "consciousness is computation"
argument plays on our intuition that the CPU is like a brain and the box that
the computer is in is like a skull.

### New biology or new physics?

The "hard problem of consciousness" is that there appears to be what David
Chalmers has called an "explanatory gap" between a purely physical description
of the universe and the subjective experience of qualia.  How do you go from
the positions and motions of atoms and fields to awareness?  There seems to be
no scientific tools available to us that bridge this gap.  This has led some to
assume that the answer to these questions lies in currently undiscovered
biological effects or even new physics.

John Searle is perhaps one of the more well known proponents of what he calls
"naive realism" and has argued that the only reason that we can't explain
consciousness is that we just don't know enough about the biology of the brain.
In the late 1800s here were heated philosophical debates about whether life
required a mysterious "vital force" or if it could be produced through ordinary
physical interactions.  As biochemists learned more about the chemistry of life
they found that it was the latter and people forgot that this was even a
question that had ever been debated.


I have to admit that I am somewhat partial to Roger Penrose's idea that
consciousness has its origins in some kind of quantum mechanical phenomenon.
The main advantage of this idea is that entanglement is a physical mechanism
that unifies multiple objects separated across space in a deep way.  We could
imagine that somehow different parts of the brain produce states which are
entangled with each other   

But I will concede that this is nevertheless a far-fetched idea just because the
brain is a warm and noisy environment.  Entanglement, at least in any form that
we know of, is too delicate a state to be maintained in the brain for any
length of time.

[^1]:
    Strictly speaking, "qualia" refers to individual conscious experiences ---
    the sensation of hearing a bell, for example --- whereas consciousness is
    the unified collection of all qualia that a conscious being experiences. In
    fact this makes the problem of consciousness harder than qualia on its own,
    becaues a theory of consciousness needs to explain not only individual
    perception experiences, but how a collection of these experiences across
    space and time can be unified into single, coherent experience of being.

[^2]:
    Some algorithms can be exponenitally faster if they are run on a quantum
    computer than if they are run on a Turing machine (which is inherently
    classical).  Nevertheless, for our purposes the algorithmic efficiency
    isn't relevant.  The Turing machine can still compute the algorithm which
    is all that matters to us.

[^3]:
    This happens more frequently than you might think.  You can actually run an
    app on your smartphone that uses the camera as a cosmic ray detector.

[^4]:
    If we like we can tighten the definition such that the machine must not
    only produce identical outputs to the Turing machine, but must maintain
    identical internal states as well.  This makes no difference to the
    argument.

[^5]:
    This is the so-called "systems response" to John Searle's Chinese Room
    argument, though presented in an oblique way.  The argument is that while
    the rocks themselves might not be conscious, the whole *system* of the
    rocks being manipulated *is* conscious.  In Searle's thought experiment the
    computation being performed was an individual in a room manipulating
    symbols according to rules in a book rather than rocks in a desert, but the
    underlying idea is the same.

[1]: https://annakaharris.com/chalmers/

[2]: http://www.consc.net/notes/lloyd-comments.html

[3]: https://twitter.com/ilyasut/status/1491554478243258368

[4]: https://www.turingtumble.com/

[5]: https://xkcd.com/505/
