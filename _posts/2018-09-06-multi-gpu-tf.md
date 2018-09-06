---
layout: post
title: Multi-GPU training with Tensorflow Estimators
date: 2018-09-06
categories: machine-learning
image:
  feature: constellations3.jpg
---

Tensorflow Estimators handle much of the boilerplate of training a neural network like saving
checkpoints and summaries, running the training loop, periodically evaluating on the validation set,
and so on.  If you're already using Estimators, it's easy to move from training on a single GPU to
synchronous multi-GPU training with only three new lines of code.

First, wrap your `model_fn` with `tf.contrib.estimator.replicate_model_fn`:

```
nn = tf.estimator.Estimator(
    model_fn=tf.contrib.estimator.replicate_model_fn(my_model_fn),
    run_config=run_config,
)
```

Second, wrap your optimizer with `TowerOptimizer` in your `model_fn`:

```
optimizer = tf.train.GradientDescentOptimizer(learning_rate=params['learning_rate'])
optimizer = tf.contrib.estimator.TowerOptimizer(optimizer)
```

Unfortunately there's one additional (undocumented) step that you have to take to get the code to
work.  If you only use the two lines above, you'll see an error that will look something like this:

```
ValueError: Variable does not exist, or was not created with tf.get_variable(). Did you mean to set reuse=tf.AUTO_REUSE in VarScope?
```

To fix this, you need to wrap the definition of your model with a `variable_scope` that has `reuse`
set to `tf.AUTO_REUSE`:

```
def model_fn(features, labels, mode, params):
  with tf.variable_scope('my_model', reuse=tf.AUTO_REUSE):
    net = tf.identity(features, 'input')
    net = tf.layers.dense(net, 1024, activation=tf.nn.relu)
    ...
```

The reason for this is that behind the scenes, `replicate_model_fn` will try to put all the
variables in your net on each GPU.  However, you want to share the variables across all the GPUs.
This means that the variables need to be created with `reuse=True` for all but one of the GPUs.
(One of the GPUs needs to have `reuse=False` so that the variables can be created --- you can't
reuse what doesn't exist in the first place!)  Setting `reuse=tf.AUTO_REUSE` takes care of this
variable management for you.

Note that `replicate_model_fn` is now deprecated, although its proposed replacement,
`MirroredStrategy` doesn't seem to be ready to use quite yet (at least I haven't been able to get it
to work).
