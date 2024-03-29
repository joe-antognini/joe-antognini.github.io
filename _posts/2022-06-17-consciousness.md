---
layout: post
title: Consciousness is not computation
date: 2022-06-17
categories: ml
image:
  feature: constellations3.jpg
---

Spend enough time in the tech world and you will sooner or later find that it
is a common article of faith that computers will one day gain consciousness.
With powerful enough computers and sophisticated enough AI, the reasoning goes,
it is inevitable that computers will eventually become conscious just as we
are.  In fact, some are even bolder and claim that this isn't just something
that will happen off in the distant future, but that the age of sentient
computers is upon us already.  David Chalmers [famously argued][2] that we must
be open to the idea that any feedback system --- even one as simple as a
[thermostat][1] --- is conscious, even if in a limited way.  Recently AI
researcher Ilya Sutskever [speculated][3] that today's large neural networks
may be "slightly conscious."  And a few months later Google engineer Blake
Lemoine was fired after [going public][23] with his concerns that the [LaMDA
language model][24] is sentient.

The idea that consciousness is fundamentally computational is admittedly
attractive.  At the core of the philosophy of mind is what Chalmers called "the
hard problem of consciousness."  How can purely physical processes give rise to
the apparently subjective experience of consciousness?  This problem has
bedeviled philosophers since the time of Descartes, and I think a fair
(tongue-in-cheek) assessment of their centuries of collective effort is that
the time would have been better spent abiding by Hume's counsel of playing
backgammon and enjoying the company of friends instead.

But as computers developed in the 20th century, a promising idea emerged.  It
went like this: Perhaps the brain is like a computer and the mind is like a
computer program.  What is important, then, is not so much the specific
hardware of the brain, but the computer program that the brain is running.
This idea seemed to break the stranglehold of physical matter on consciousness
and introduced an abstract, non-physical entity that sits on top of the
hardware, which seems to neatly correspond to the way that consciousness seems
to sit on top of the brain. [[^7]] After centuries of fruitless efforts by
philosophers at explaining the origin of consciousness, it's easy to see why
those who worked with these new machines latched onto this revolutionary
paradigm, especially as this idea began to be [represented][8] in [science][9]
[fiction][10] and, as the decades progressed, computers started to surpass
humans in a [variety][11] of [tasks][12].

But we must resist the allure of this seductive idea.  The theory that
consciousness is nothing but running the right kind of computer program is
wrong.  Computation alone is insufficient to produce consciousness.

This is, as I understand it, not a radical position among philosophers of the
mind these days.  Back in the 1980s John Searle cast doubt on the computational
theory of consciousness with the [Chinese Room argument][13], and today it
seems that most philosophers accept its validity.  But this position is not
universal.  Some philosophers have raised a number of objections to Searle's
argument.  And it certainly does not appear that the consensus within the tech
world matches the consensus among philosophers, since the notion that computers
will one day attain consciousness is still popular.

My purpose in this blog post is to outline another argument against the idea
that consciousness can be reduced to computation.  This is the so-called
"[triviality argument][16]."  It is less famous than the Chinese Room argument
(perhaps because the name is not as catchy), but I think it refutes the
computational theory of consciousness at a more fundamental level.

## Some preliminaries

### What I mean by "consciousness"

Before getting too deep we need a working definition of consciousness.  This is
a tricky concept to define rigorously since it seems that a rigorous definition
of consciousness practically requires a theory of consciousness itself.  To
make matters worse, in these kinds of discussions it oftentimes gets mingled
with related ideas like self-awareness, intelligence, and executive function.
But in this post I am interested only in consciousness as a sort of perception
or sentience --- an awareness of being, or, more loosely, "what it feels like
to be something."

This aspect of consciousness is sometimes called "qualia." [[^1]]  I won't
rehearse the classic arguments for the existence of qualia since, like
Descartes, I regard my own qualia as an empirical fact --- perhaps the only
empirical fact that I can know for certain. [[^6]]  Of course given any
position in philosophy you can find *some* philosopher who has made the case
for it [[^4]], and Daniel Dennett has made the case that [qualia does not
exist][6].  But I will take it as an axiom that qualia and consciousness exist.

So if we accept that qualia exists (which, after all, seems intuitively
sensible), we are burdened with the apparently impossible task of explaining
how consciousness can be generated by physical processes.  This is the crux of
the "hard problem of consciousness."

#### Consciousness is observer independent

It's worth pausing here and noting one property of consciousness that will be
of use to us later: consciousness is independent of external observers.  By
this I mean that the existence of my consciousness does not depend on other
observers perceiving me to be conscious.  Even if everyone else in the universe
should deny that I am conscious --- or if those other observers did not exist
at all --- this would have no bearing on my own consciousness.  If, in a
terrible catastrophe all life on Earth should perish, except by some strange
fortune my own, my consciousness would not suddenly dissolve into the ether.

### What is computation?

We also need a working definition of computation.  Fortunately here we are on
much firmer ground.  Computation, in the broadest sense, is the manipulation of
symbols according to an algorithm.  The largest and most important category of
computation is the set of algorithms which can, in principle, be executed on a
Turing machine.  As far as we know, every algorithm that can be run on a
physical computer can also be run on a Turing machine. [[^2]]

#### What is a computer?

There is then the follow-up question of what exactly constitutes a computer.
Now, a Turing machine is a purely mathematical abstraction, like a circle or a
fractal.  We can create or identify things in the real world which can be well
modeled by a circle, but the abstract idea of a circle is distinct from a
drawing of a circle.

Likewise we can build an object in the real world which can model the behavior
of the abstract Turing machine.  And, more practically, we can build devices
whose behavior, while not identical to that of a Turing machine, can compute
the same things.  We call such devices computers.

A little more formally, we can define a computer to be a device which has
physical states, and whose physical states map onto the states of a Turing
machine.  The computer is then the instantiation of that abstract Turing
machine in the physical world.  We can, for example, make a correspondence
between the voltage levels in a CPU register with the state of the Turing
machine; likewise we can make a correspondence between the magnetic moments of
sections of a hard drive with the states of the Turing machine's ticker tape.

#### How accurate does a computer need to be?

We generally expect computers to be deterministic.  If we run the same program
twice, the computer should generate the same results. [[^9]]  But achieving
complete determinism is impossible.  Sometimes, very rarely, the computer will
make a mistake --- a cosmic ray, for example, will fly through and flip a bit
somewhere.  [[^3]]  If we decide that a machine is not a computer simply because
it ever makes *any* errors, we will have to conclude that there are no
computers at all in the real world.  And if computers don't exist, then
consciousness cannot be computation.

But it's not necessary to impose such a strict requirement.  We don't need to
demand that the computer *never* make a mistake.  We only need to require that
the computer not make a mistake when we run our program.  If, during the
program's execution, every abstract state of the ideal Turing machine can be
mapped on to a physical state of the system, we can say that the system is
computing the algorithm.  If it makes a mistake somewhere and breaks that
correspondence, then it stops being a computer for the time being, at least for
our purposes.

This definition of a computer as a mapping between the physical states of a
system and the abstract states of a Turing machine is powerful because it
abstracts away the internal mechanics of the computer.  The computer can use
transistors or vacuum tubes or something else entirely, and we can just focus
just on what the abstract Turing machine is doing.  Computer scientists don't
need to know anything about Kirchhoff's laws or semiconductor physics to
determine whether $$P = NP$$.

## Consciousness in a field of rocks

Since computation is independent of the physical mechanism it uses to transform
its states and produce outputs, we can imagine (impractical) computers that are
made out of things other than electronics.  We can create mechanical computers
out of [Legos][7] or [balls tumbling down a pegboard][4].  A wonderful cartoon
from [XKCD][5] imagined an individual who finds himself in a vast desert filled
with rocks.  To allay his boredom, he manipulates the rocks on the desert to
produce a computer, and in so doing, simulates the entire universe, instant by
instant.

Now, if consciousness were a consequence of pure computation, it would be
possible to write a clever computer program (let's call it `consciousness.exe`)
that, when executed on a big enough computer, produces a conscious being.  But
computation is independent from the physical substrate that the computation is
performed on.  So if a powerful supercomputer can produce consciousness by
running `consciousness.exe`, we should also be able to produce a conscious
being by running the same `consciousness.exe` program with enough Legos or by
manipulating enough rocks in a desert.

It already seems implausible to me that a vast desert of rocks being
manipulated into various patterns is conscious.  What exactly is conscious
here?  What happens if I accidentally kick a rock to the side --- have I killed
whatever ghostly being inhabits these rocks?  Nevertheless, I think we can do
better than simply asserting its implausibility.  Sure, it is hard to imagine
what it means for this vast desert of rocks to be conscious, but there are lots
of unintuitive things in this world.  We shouldn't let our prejudices as to
what substrate consciousness *should* exist in prevent us from accepting that
it could very well exist in a substrate which is unfamiliar to us. [[^5]]

## Does iron become conscious when it's hot?

So let's follow where this argument takes us.  Rather than manipulating rocks
in a desert, let's imagine a bar of iron heated past the Curie temperature.
Each atom in the bar has a magnetic moment which points either up or down, and
because the bar is so hot, the magnetic moment of each atom is randomly
flipping between up and down.  Moreover, by an ingenious detector, we have the
means to observe whether the magnetic moment of every atom in the bar is up or
down at any given time.

I want to determine if this bar of iron is conscious, so I examine its atoms to
see if it is running the `consciousness.exe` computer program.  I designate the
first $$P$$ atoms to be input bits, another $$N$$ atoms to be internal states
of the Turing machine, and then another $$Q$$ atoms to be outputs.  Then I look
at the magnetic moments of those atoms sampled at different time steps and see
if they correspond to the inputs, outputs, and intermediate states of the
corresponding Turing machine by designating a moment pointing up as a 1 and a
moment pointing down as a 0.  Naturally, there is no correspondence so I
conclude that the bar of iron is not conscious.

Simultaneously, however, my friend Alice performs the same observation.  But
rather than designating moments pointing up as a 1 and a moment pointing down
as a 0, she considers an atom pointing up to be a 1, unless it's the first atom
in the bar, in which case it's a 0.  Naturally, she, too, observes no
correspondence with `consciousness.exe` and concludes that the bar of iron is
not conscious.

But another friend of mine, Bob, makes the same observation, though using a
slightly different encoding.  He considers an atom pointing up to be a 1,
unless it's the second atom in the bar, in which case it's a 0.  Similarly Carl
performs the same observation, but in his encoding, an atom pointing up is a 1
unless it's the third atom, and so on.  Eventually we get to Ada, who encodes
an atom pointing up as a 1 unless it's the first or second in which case it's
a 0.  Then Barbara, who encodes an atom pointing up as a 1 unless it's the first
or third.

Continuing this, we can imagine an enormous crowd of observers staring at this
iron bar, each using a unique encoding of atomic states to bits.  With a
sufficiently large number of observers, the encodings of all possible Turing
machines of the given size are represented.  This means that one of these
observers will, by chance, happen to observe that the states of the atoms
correspond exactly to the bits of a Turing machine computing
`consciousness.exe`.  This observer will then conclude that the bar of iron is
a computer running `consciousness.exe` and is therefore conscious.

But!  If a single observer can correctly determine that the bar of iron is
conscious, we must conclude that the bar of iron is conscious for *everybody*,
because consciousness is observer independent.  If true, honest-to-God
consciousness is just a matter of running `consciousness.exe`, we have indeed
found someone who has correctly observed that the bar of iron is running
`consciousness.exe` and we must conclude that the bar of iron *really is
conscious*.

To go further, I have not specified what `consciousness.exe` is, and presumably
there are many possible `consciousness.exe` programs.  There is
`alices_consciousness.exe`, `bobs_consciousness.exe`, along with
`joes_consciousness.exe` and `your_consciousness.exe`, which are the programs
that generate Alice's, Bob's, my own, and your consciousnesses, respectively.
The bar of iron is running *all of them*.  So not only is the bar of iron
conscious, it contains my consciousness, your consciousness, and *all possible
consciousnesses*.

And of course there's nothing special about the iron itself.  We could make the
same argument with any system where we can map states to bits.  We could
imagine doing the same thing with the locations of molecules in a [pail of
water][19] or on the [wall of a room][20], or in a [brick][21].  In all cases
we are forced to conclude that a sufficiently large system contains all
possible consciousnesses.  So the proposition that consciousness is computation
leads quite inevitably to an extreme panpsychism.  Even if we could stomach a
traditional conception of panpsychism that posits that all things are conscious
in some primitive way, this goes far beyond that.  We are forced to conclude
that all things aren't just vaguely conscious, but they contain *all*
consciousnesses, including our own!

## (Some) computers could (possibly) still be conscious!

Now I want to be quite clear about this position.  By saying that consciousness
is not computation, I am *not* claiming that computers are not or never can be
conscious.  We could imagine a world in which consciousness is produced by
electric fields that fluctuate in the right patterns, for example.  Perhaps, in
such a world, my laptop running `consciousness.exe` produces the right patterns
just as the neurons in the brain do, and becomes conscious.

But in this world, consciousness is, at root, a *physical* phenomenon, not a
purely computational phenomenon.  Computation may be necessary to produce
consciousness, but it cannot be sufficient.  So in such a world I can run
`consciousness.exe` on a digital computer and produce a conscious being, but if
I run the same program on the "rocks in a desert" computer or the "hot iron
bar" computer, I will not.  In this case consciousness is hardware-dependent.
If we claim, for example, that a GPU running GPT-3 is conscious, we have to
explain what it is about this particular physical equipment that is generating
consciousness, and an argument that GPT-3 running on an NVIDIA GPU is
conscious would not necessarily generalize to that same neural network running
on an AMD GPU.

Furthermore, to be very clear, none of this is to say that computers cannot
behave in intelligent ways.  It is entirely possible that a computer running a
clever enough program could have an intelligent conversation with a human or
design a research protocol to cure cancer.  We could fairly say that such a
program is intelligent.  But it is still not conscious.

## Syntax is not semantics

The triviality argument can be reduced to its bare bones like this:

1. To say that a physical system is a computer requires an external observer to
   map the physical states of that system onto the abstract states of a Turing
   machine.
2. Consciousness does not require an external observer to exist.
3. Therefore, consciousness cannot be reduced to computation.

But if we were to sum up the argument even further into a single slogan it
would be this: syntax is not semantics.  All computers can do is shuffle lumps
of matter around by following the rules of an algorithm (a syntax), whether
that matter be rocks in a vast desert, or electrons on a silicon wafer.  But
these lumps of matter have no intrinsic meaning (no semantics).  The only
reason we call a box with a CPU in it a "computer" is because we happen to have
a simple mapping between the voltage levels across different parts of the CPU
to a set of bits we have defined, and when these voltages interact they do so
according to the rules of a set of logical operations which we have also
defined.  But there is no meaning to the physical system apart from what we, as
external observers, have imposed on it.

Of course it is simplest to build a computer where the high voltage states
correspond to 1s and the low voltages states 0s or vice versa.  But there is no
requirement that we build our computers that way.  We could build a perfectly
valid computer where the high voltage states of even valued registers
correspond to 1s and where they correspond to 0s in the odd valued registers,
or a computer where the mapping flips on every 13th clock cycle.  The system
only "computes" because of the way we have encoded information. [[^10]]

So computer simulations can never produce the entity they are simulating since
the "simulation" is not an independent system.  It is only defined in terms of
its relation to an external observer.  A simulation of a brain cannot produce
consciousness any more than a simulation of the weather can produce rain.

## Should this conclusion worry us?

This "triviality argument" has been presented by a number of philosophers,
among them Ian Hinckfuss, John Searle, Hilary Putnam, and David Chalmers.  But
as with any philosophical argument it is not universally accepted.  The
principal objection is that it assumes too loose a definition of computation.
The counterargument goes like this: Well *of course* if we assume an expansive
definition of computation, then everything from bricks to buckets of water
becomes a computer.  But shouldn't this be an indication that we ought to
reconsider what it means to be a computer?

Now, a major downside of tightening our definition of a computer is that it is
much less obvious what an appropriate definition is.  Our original definition
was that anything is a computer as long as we can make a mapping from physical
states to the abstract states of a Turing machine.  This definition has the
virtues of being precise and objective.  I can tell you my mapping and then you
can look at the system and say with certainty whether or not it is computing a
given Turing machine.  But if we try to tighten this definition by requiring,
for instance, that the mapping be "simple," then we will lose objectivity in
the definition, because there's no clear metric for what constitutes a simple
encoding.

Nevertheless, our original definition of a computer engenders another thorny
problem.  In this post I've been promoting the "anti-realist" position, namely
that computation is only defined in terms of its relation to us.  We happen to
call certain objects in this world "computers" because there is a convenient
and reliable mapping between their physical states and the abstract states of a
Turing machine (though in principle any mapping will do).  But without an
external observer present to call the object a computer, it's just a lump of
matter obeying the laws of physics, just like any other lump of matter in
universe.  So computation, in this definition, necessitates external observers.
Without an external observer to say "that box is a computer," computers don't
exist, and by extension, no computation occurs.

The problem is that surely the mind computes in some way.  When I do a
crossword, it feels like I am computing *something*.  But if that's so, what is
the "observer" that is making the mapping from physical states to abstract
states?  It can't be myself because my mind is not external to me, nor can it
be anyone else because I can still do a crossword when no one is around to
observe me.  You might say that there's no real problem here, one part of the
mind just observes another part of the mind computing.  But this is just the
[homunculus fallacy][22].  Can this "inner eye" compute as well?  If it can't
compute, it doesn't seem as though it can think. [[^11]]  But if it *can*
compute, what is the external observer that is interpreting *its* activity as a
computer?

Since there is no definition of computation without reference to an external
observer, a system in isolation just cannot compute, which suggests that a
conscious being cannot compute.  Maybe parts of the brain can compute with
respect to other parts, but no computation is possible in the mind taken as a
whole.  Unfortunately in arguing that consciousness is not computation, we end
up struggling to imagine how the mind can compute anything at all. 

## So what is consciousness then?

The idea that consciousness comes from computing a particular kind of program
is seductive because it lays out a clear path toward understanding where
consciousness comes from.  If only we could write a clever enough computer
program, we could figure it out.  But the triviality argument has convinced me
at least that a computational theory of consciousness is not the path forward.

But if consciousness is not computation, then what is it?  Of course that's the
hard question, and I don't claim to have a solution.  But there are a few
properties of consciousness that we have to explain if we want a good theory of
consciousness.

### Consciousness is in the brain

It hardly seems worth mentioning, but one thing we can be quite sure of is that
consciousness as we know it is very closely linked to the brain.  This had been
suspected since antiquity but modern neuroscience backs up our intuition.  My
consciousness does not fall off my body when I clip off a fingernail nor even
if I chop off my arm.  But if a neurosurgeon slices off a piece of my brain, or
severs some neural connections, my consciousness may radically alter.

The brain is a large mass of neurons, and when those neurons cease firing I die
and cease being conscious.  So clearly consciousness has something to do with
the activity of neurons.  But consciousness cannot be an inherent feature of
neurons in general because the cerebellum contains four or five times as many
neurons as the cerebral cortex but does not seem to be relevant for
consciousness.  On rare occasions people can be born [without a
cerebellum][15], and by all appearances seem to be conscious (and often lead
remarkably ordinary lives all things considering).

So any theory of consciousness needs to explain the connection between what is
going on in the cerebral cortex and sentience.   And additionally, it needs to
explain why the *rest* of the body (some of which is also made of neurons) is
apparently *not* conscious.  There is something special going on in the
cerebral cortex, and only the cerebral cortex, that seems to produce
consciousness (as far as we can tell).

### Consciousness is a unified, integrated whole

The second important property of consciousness that any theory needs to explain
is that consciousness is a single, cohesive experience.  My consciousness is of
my entire self.  It is not of half of myself, nor is it some superposition of
you and me.  Somehow, whatever is going on in my brain to produce my
consciousness contains all the neurons of my brain, not just a subset of them.
There are not multiple consciousnesses in my brain, it's just me in there.

Some individuals with severe epilepsy have to have their corpus callosum
severed, which separates their left and right hemispheres.  After this
procedure these individuals often seem to exhibit [*two* consciousnesses][18]
rather than one.  The right side of the brain seems to be surprised when the
left side of the brain decides to raise the right arm, and vice versa.  But
this is never the case in an individual with a connected corpus callosum.
Every time I decide to raise my arm (left or right), my arm goes up and it only
goes up when I decide to raise it.

This is important because any theory of consciousness needs to account for the
boundaries of consciousness.  Evidently consciousness includes *all* the
neurons in the cerebral cortex.  We might suppose that any tightly integrated
network of neurons will become conscious.  But if that's the case then why is
the cerebellum not conscious?  Evidently the topology of this network must be
relevant.

### New biology or new physics?

The "hard problem of consciousness" is that there appears to be what Chalmers
has called an "explanatory gap" between a purely physical description of the
universe and the subjective experience of qualia.  How do you go from the
motions of atoms in electromagnetic fields to sentience?  There seem to be no
scientific tools available to us to bridge this gap.  But maybe the answer to
these questions lies in currently undiscovered biological effects or even new
physics.

John Searle is one of the better known proponents of "[biological
naturalism][17]" and has argued that the only reason that we can't explain
consciousness is that we just don't know enough about the biology of the brain.
After all, vicious philosophical debates in the past have been resolved and
later quietly forgotten as scientists have come to a better understanding of
biology.  The origin of species was at one point a philosophical problem that
was ultimately solved by biology.  And in the late 1800s there were heated
philosophical debates about whether life required a mysterious "vital force" or
if it could be produced through ordinary physical interactions.  As biochemists
learned more about the chemistry of life they found that it was the latter and
before long everyone forgot that this was even a question that had ever been
debated.  Perhaps the same will be true of consciousness.  As we learn more
about neurobiology, maybe we will come to see that consciousness is just
generated as a biological process "in the same way that the stomach produces
digestion," in Searle's words.  Then these centuries of speculation about the
"hard problem of consciousness" will be viewed by our descendants to be as
quaint as the debates about vitalism.

But perhaps new biology is not enough.  Roger Penrose has argued that an
explanation of consciousness does not simply require new biology, but new
physics as well.  I have to confess that as far-fetched an idea as it is, I am
somewhat partial to the idea.  The concept of a quantum state has the useful
property that it is attached to physical objects but nevertheless extends
across a finite space as a cohesive unit, much like consciousness.

Furthermore, this idea has the advantage of providing a connection to one of
the more mysterious features of quantum mechanics --- the collapse of the
wavefunction.  This feature has always sat uncomfortably within the orthodox
Copenhagen interpretation because it is a little vague on what constitutes an
"observation" that triggers the collapse.  [Eugene Wigner][25], among others,
argued that it is only a conscious observer who can trigger the collapse of a
wavefunction.  It is an admittedly odd idea, but occasionally odd ideas turn
out to be true.

But I will concede that, intriguing though it is to speculate about, resorting
to quantum mechanics or new physics is the last refuge of scoundrels.  The
brain is a warm and noisy environment, and as far as we know a quantum state is
just too delicate to be maintained in the brain for any length of time.  

So where does this leave us?  I suspect that for the foreseeable future we will
be stuck with apophatic approaches to the hard problem of consciousness.  Just
as it's easier to say what God is *not* rather than what God is, we may not be
able to say much about what consciousness is, but we can at least learn
something by saying what it is *not*.  And here we can be confident in saying
that consciousness is not computation.

----

## Footnotes

[^1]:
    Strictly speaking, "qualia" refers to individual conscious experiences ---
    the sensation of hearing a bell, for example --- whereas consciousness is
    the unified collection of all qualia that a conscious being experiences. In
    fact this makes the problem of consciousness harder than qualia on its own,
    because a theory of consciousness needs to explain not only individual
    perception experiences, but how a collection of these experiences across
    space and time can be unified into single, coherent experience of being.

[^2]:
    The statement that this is true for all algorithms is known as the
    Church-Turing Thesis.  Some algorithms can be exponentially faster if they
    are run on a quantum computer than if they are run on a Turing machine,
    which is inherently classical.  Nevertheless, for our purposes the
    algorithmic efficiency isn't relevant.  As far as we know, anything that
    can be computed by a quantum computer can also be computed by a Turing
    machine, and it is only the question of computability that matters to us.

[^3]:
    This happens more frequently than you might think.  You can actually run an
    app on your smartphone that uses the camera as a cosmic ray detector.

[^4]:
    According to John Searle there is one exception.  No serious philosopher
    has defended solipsism, the idea that no other being in the universe
    besides oneself is conscious.  But then, if one were a true solipsist,
    there would be no point in spending any time convincing anyone else of your
    position since no one else exists.

[^5]:
    This is, in essence, the so-called "systems response" to John Searle's
    Chinese Room argument, though presented in an oblique way.  The argument is
    that while the rocks themselves might not be conscious, the whole *system*
    of the rocks being manipulated *is* conscious.  In Searle's thought
    experiment the computation being performed was an individual in a room
    manipulating symbols according to rules in a book rather than rocks in a
    desert, but the underlying idea is the same.

[^6]:
    The classic argument that qualia exists is due to Frank Jackson in the
    article "What Mary Didn't Know."  I encourage you to read the original
    article (and the Wikipedia article is quite good, too), but in brief, the
    argument proposes a thought experiment: Suppose there is a scientist named
    Mary.  Through extensive study, she has learned all there is to know about
    the physics of color, the physiology of the eye, and the neurology of the
    brain.  Given some stimulus like looking at a red rose, she knows exactly
    how the light impacts the eye, how the image forms on the retina, how this
    produces a signal along the optical nerve, and how the brain processes this
    signal.  However, Mary has lived her entire life within a black and white
    room and has never perceived color herself.  One day, she leaves the room
    and looks at a red rose.  Does she learn anything new from this experience?
    If she does, we are forced to conclude that qualia exists --- that an
    experience is distinct from perfect knowledge of how the brain reacts to
    the stimuli that produced that experience.

[^7]:
    The formal name for this theory is "[functionalism][26]," and the basic
    idea is that the physical constituents aren't relevant to a mental state
    --- all that matters is that the system functions appropriately.  In the
    case of a computer program, it doesn't matter what computer you run the
    program on, the important thing is the behavior of the program itself.
 
[^9]:
    It was for good reason that the authors of Numerical Recipes described
    random number generation as a "perverse" use of a computer.  A machine
    which is designed to be deterministic is not well suited to behaving
    randomly!

[^10]:
    An active field of research is [homomorphic encryption][14] in which
    computation is performed on encrypted data.  In this case the mapping
    between the physical states of the system and the abstract states of the
    Turing machine is not nearly so straightforward.  Sometimes high voltage
    states correspond to 1s and other times 0s.  Only with the appropriate key
    can you determine what the mapping is.  Nevertheless, the mapping exists,
    so you can claim that the system is computing.

[^11]:
    One risky way out, rejected by most philosophers, is epiphenomenalism.
    This is the notion that consciousness has no causal effects on the material
    world, but is just "along for the ride."  Our consciousness simply sits on
    top of the brain and passively watches it chug along.  Different neural
    activations produce different sensations of consciousness, but our
    conscious thought never changes our behavior.  Any belief we have that we
    are consciously making decisions is an illusion --- in reality the brain is
    blindly chugging along, and our consciousness is interpreting these neural
    states as the sensation of making decisions even no conscious decision
    making is happening.  I will admit to having some sympathy for
    epiphenomenalism, but it does pose challenges.  When I hit my thumb with a
    hammer and feel pain, why do I find that sensation unpleasant?  Why do I
    find the sensation of eating a freshly picked strawberry pleasant?  If
    epiphenomenalism is wrong and my conscious states can influence my actions
    there is a good explanation --- natural selection has evolved the sensation
    of pain so that I avoid things that will hurt me, and similarly it has
    evolved the sensation of pleasure so that I seek out things that help me to
    survive.  But in the epiphenomenalist picture there is no causal connection
    between the conscious perception and any physical actions.  It makes no
    difference how my consciousness perceives these things.  So why does there
    just so happen to be a tight correspondence between the conscious
    perception and my survival?
    
[1]: https://annakaharris.com/chalmers/

[2]: http://www.consc.net/notes/lloyd-comments.html

[3]: https://twitter.com/ilyasut/status/1491554478243258368

[4]: https://www.turingtumble.com/

[5]: https://xkcd.com/505/

[6]: https://ia801304.us.archive.org/22/items/FritjofCapraTheTurningPoint/Daniel%20C.%20Dennett%20-%20Quining%20Qualia.pdf

[7]: https://abakcus.com/video/lego-turing-machine/

[8]: https://www.youtube.com/watch?v=ARJ8cAGm6JE

[9]: https://www.youtube.com/watch?v=Z_OjTojCNm0

[10]: https://www.youtube.com/watch?v=KXzNo0vR_dU

[11]: https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)

[12]: https://en.wikipedia.org/wiki/AlphaGo

[13]: https://plato.stanford.edu/entries/chinese-room/

[14]: https://en.wikipedia.org/wiki/Homomorphic_encryption

[15]: https://academic.oup.com/brain/article/133/3/652/277518

[16]: https://marksprevak.com/publications/triviality-arguments-about-computational-implementation-2018/

[17]: https://en.wikipedia.org/wiki/Biological_naturalism

[18]: https://en.wikipedia.org/wiki/Split-brain

[19]: https://www.jstor.org/stable/2025395

[20]: http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.1068.2142&rep=rep1&type=pdf

[21]: https://www.google.com/books/edition/Representation_and_Reality/A0YJILtyCPEC?hl=en&gbpv=0

[22]: https://en.wikipedia.org/wiki/Homunculus_argument

[23]: https://www.washingtonpost.com/technology/2022/06/11/google-ai-lamda-blake-lemoine/?variant=95d42e19c24b03e7

[24]: https://blog.google/technology/ai/lamda/

[25]: https://en.wikipedia.org/wiki/Von_Neumann%E2%80%93Wigner_interpretation

[26]: https://en.wikipedia.org/wiki/Functionalism_(philosophy_of_mind)
