---
layout: post
title: Building a standalone C++ Tensorflow program on Windows
date: 2017-06-21
categories: machine-learning
image:
  feature: constellations3.jpg
---

In the [last post][1] we built a static C++ Tensorflow library on Windows.
Here we'll write a small Tensorflow program in Visual Studio independent
from the Tensorflow repository and link to the Tensorflow library.  The
tutorials I have been able to find about writing a new Tensorflow C++
program all seem to require that the new C++ project live within the
Tensorflow repository itself.  But this is not practical for many projects,
nor does it turn out to be necessary.  If you haven't built a static
Tensorflow library, [do that first][1].

This program will simply read some data that has been hard-coded into
memory, and then feed it into a graph that just multiplies it by another
hard-coded matrix.

## A simple C++ Tensorflow program

Create a new solution with the following code:

```
// matmul.cpp

#include <vector>
#include <eigen/Dense>

#include "matmul.h"
#include "tensorflow/core/public/session.h"
#include "tensorflow/cc/ops/standard_ops.h"

using namespace tensorflow;

// Build a computation graph that takes a tensor of shape [?, 2] and
// multiplies it by a hard-coded matrix.
GraphDef CreateGraphDef()
{
  Scope root = Scope::NewRootScope();

  auto X = ops::Placeholder(root.WithOpName("x"), DT_FLOAT, 
                            ops::Placeholder::Shape({ -1, 2 }));
  auto A = ops::Const(root, { { 3.f, 2.f },{ -1.f, 0.f } });

  auto Y = ops::MatMul(root.WithOpName("y"), A, X, 
                       ops::MatMul::TransposeB(true));

  GraphDef def;
  TF_CHECK_OK(root.ToGraphDef(&def));

  return def;
}

int main()
{
  GraphDef graph_def = CreateGraphDef();

  // Start up the session
  SessionOptions options;
  std::unique_ptr<Session> session(NewSession(options));
  TF_CHECK_OK(session->Create(graph_def));

  // Define some data.  This needs to be converted to an Eigen Tensor to be
  // fed into the placeholder.  Note that this will be broken up into two
  // separate vectors of length 2: [1, 2] and [3, 4], which will separately
  // be multiplied by the matrix.

  std::vector<float> data = { 1, 2, 3, 4 };
  auto mapped_X_ = Eigen::TensorMap<Eigen::Tensor<float, 2, Eigen::RowMajor>>
                     (&data[0], 2, 2);
  auto eigen_X_ = Eigen::Tensor<float, 2, Eigen::RowMajor>(mapped_X_);

  Tensor X_(DT_FLOAT, TensorShape({ 2, 2 }));
  X_.tensor<float, 2>() = eigen_X_;

  std::vector<Tensor> outputs;
  TF_CHECK_OK(session->Run({ { "x", X_ } }, { "y" }, {}, &outputs));

  // Get the result and print it out
  Tensor Y_ = outputs[0];
  std::cout << Y_.tensor<float, 2>() << std::endl;
  
  session->Close();
}
```

As a digression, I would write something a little fancier, but the C++ API
is fairly limited relative to the Python API, and seems to be designed with
inference in mind more than training.  It is fairly straightforward to load
a computation graph that has already been built in Python, but building a
new graph from scratch in C++ is harder.  In particular, in Python it is
easy add training operations to the graph --- the `minimize` method of the
`Optimizer` class will automatically add gradient Ops that will use backprop
to calculate the gradient for every Op in the graph.  The C++ API does not
yet have this functionality.  In theory one could go through the graph and
add these gradients oneself, but at that point it would probably be best
just to write an `Optimizer` class in C++.  (This is currently an [open
issue][2].)  This will probably change as the C++ API improves, but it's
(justifiably) probably not a high priority for the Tensorflow team.  For the
time being it is probably best to build the graphs in Python and then load
them in C++.

Next, in the header file, put the following:

```
// matmul.h

#pragma once

#define COMPILER_MSVC
#define NOMINMAX
```

If you omit the `COMPILER_MSVC` definition, you will run into an error
saying "You must define `TF_LIB_GTL_ALIGNED_CHAR_ARRAY` for your compiler."
If you omit the `NOMINMAX` definition, you will run into a number of errors
saying "'(': illegal token on right side of '::'".  (The reason for this is
that `<Windows.h>` gets included somewhere, and Windows has macros that
redefine `min` and `max`.  These macros are disabled with `NOMINMAX`.)

## Setting the project properties

The main trick to linking to the C++ Tensorflow library is getting all the
project properties right.  The following settings assume that you downloaded
the Tensorflow repository to `C:\Users\%USERNAME%\bin\tensorflow`.  If you
put it somewhere else substitute it wherever you see that path.  And
naturally, substitute your own username for `%USERNAME%`.

### Include Directories

First, the compiler needs to find all the appropriate Tensorflow header
files.  In your Additional Include Directories, add:

```
C:\Users\%USERNAME%\bin\tensorflow
C:\Users\%USERNAME%\bin\tensorflow\tensorflow\contrib\cmake\build
C:\Users\%USERNAME%\bin\tensorflow\tensorflow\contrib\cmake\build\external\eigen_archive
C:\Users\%USERNAME%\bin\tensorflow\third_party\eigen3
C:\Users\%USERNAME%\bin\tensorflow\tensorflow\contrib\cmake\build\protobuf\src\protobuf\src
```

It is important to put the `eigen_archive` directory above the `eigen3`
directory --- otherwise you'll get the C1014 "too many include files"
error.

### Linker Settings

Next, in your Additional Dependencies setting, add the following:

```
zlib\install\lib\zlibstatic.lib
gif\install\lib\giflib.lib
png\install\lib\libpng12_static.lib
jpeg\install\lib\libjpeg.lib
lmdb\install\lib\lmdb.lib
jsoncpp\src\jsoncpp\src\lib_json\$(Configuration)\jsoncpp.lib
farmhash\install\lib\farmhash.lib
fft2d\\src\lib\fft2d.lib
highwayhash\install\lib\highwayhash.lib
libprotobuf.lib
tf_protos_cc.lib
tf_cc.lib
tf_cc_ops.lib
tf_cc_framework.lib
tf_core_cpu.lib
tf_core_direct_session.lib
tf_core_framework.lib
tf_core_kernels.lib
tf_core_lib.lib
tf_core_ops.lib
```

Without any of these you will get "unresolved external symbol" errors.  Of
course, the compiler has to be able to find all these libraries, so add the
following to your Additional Library Directories:

```
C:\Users\%USERNAME%\bin\tensorflow\tensorflow\contrib\cmake\build\protobuf\src\protobuf\Release
C:\Users\%USERNAME%\bin\tensorflow\tensorflow\contrib\cmake\build\tf_cc.dir\Release
C:\Users\%USERNAME%\bin\tensorflow\tensorflow\contrib\cmake\build\tf_cc_ops.dir\Release
C:\Users\%USERNAME%\bin\tensorflow\tensorflow\contrib\cmake\build\tf_cc_framework.dir\Release
C:\Users\%USERNAME%\bin\tensorflow\tensorflow\contrib\cmake\build\tf_core_cpu.dir\Release
C:\Users\%USERNAME%\bin\tensorflow\tensorflow\contrib\cmake\build\tf_core_direct_session.dir\Release
C:\Users\%USERNAME%\bin\tensorflow\tensorflow\contrib\cmake\build\tf_core_framework.dir\Release
C:\Users\%USERNAME%\bin\tensorflow\tensorflow\contrib\cmake\build\tf_core_kernels.dir\Release
C:\Users\%USERNAME%\bin\tensorflow\tensorflow\contrib\cmake\build\tf_core_lib.dir\Release
C:\Users\%USERNAME%\bin\tensorflow\tensorflow\contrib\cmake\build\tf_core_ops.dir\Release
C:\Users\%USERNAME%\bin\tensorflow\tensorflow\contrib\cmake\build\Release
C:\Users\%USERNAME%\bin\tensorflow\tensorflow\contrib\cmake\build
```

### Additional Command Line Options

At this point your code will successfully compile, but if you try to run it,
you will get the following error when you try to create the scope:
"Non-OK-status: status status: Not found: Op type not registered 'NoOp' in
binary running on MACBOOK. Make sure the Op and Kernel are registered in the
binary running in this process."

The issue here (as I understand it) is that Visual Studio will by default
only link to the objects that it thinks it needs in the libraries that it
has been given.  Tensorflow ends up using more of these objects internally,
however, so all objects in the library need to be explicitly linked with the
`/WHOLEARCHIVE` option.  Unfortunately, you cannot simply use the
`/WHOLEARCHIVE` option on its own because you will get linker error LNK1000:
"Internal error during CImplib::EmitThunk", so you have to explicitly call
`/WHOLEARCHIVE` only on the tensorflow libraries that you want.

To do this, add the following to your command line options:

```
/machine:x64 
/ignore:4049 /ignore:4197 /ignore:4217 /ignore:4221
/WHOLEARCHIVE:tf_cc.lib 
/WHOLEARCHIVE:tf_cc_framework.lib
/WHOLEARCHIVE:tf_cc_ops.lib 
/WHOLEARCHIVE:tf_core_cpu.lib
/WHOLEARCHIVE:tf_core_direct_session.lib 
/WHOLEARCHIVE:tf_core_framework.lib
/WHOLEARCHIVE:tf_core_kernels.lib 
/WHOLEARCHIVE:tf_core_lib.lib
/WHOLEARCHIVE:tf_core_ops.lib   
/WHOLEARCHIVE:tf_stream_executor.lib
/WHOLEARCHIVE:libjpeg.lib   
```

The `/ignore` and `/machine` options are not strictly necessary, but just a
good idea.

### Running the program

At this point everything should compile correctly, and you will have an
executable called `matmul.exe` that will use Tensorflow to perform a matrix
multiplication.  On my system this program compiles to about 35 MB.  The
output should look like:

```
 7 17
-1 -3
```

[1]: ../../machine-learning/build-windows-tf
[2]: https://github.com/tensorflow/tensorflow/issues/9837
