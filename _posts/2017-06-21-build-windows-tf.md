---
layout: post
title: Building a static Tensorflow C++ library on Windows
date: 2017-06-21
categories: machine-learning
image:
  feature: constellations3.jpg
---

Tensorflow was built first and foremost as a Python API in a Unix-like
environment.  But there are some projects where using Windows and C++ is
unavoidable.  This post will show how to write a simple C++ program in
Visual Studio 2015 that links to Tensorflow.  This build was done on Windows
8 without GPU support.

## Building Tensorflow in Visual Studio with CMake

The first step is to build Tensorflow into a static library that our program
can eventually link to.  Google generally builds their code using Bazel, but
Bazel support on Windows is experimental.  The Tensorflow group has also
provided a Windows [CMake build][1] with fairly detailed instructions (which
is also experimental).  I found the CMake build easier to work with than the
Bazel build.  The instructions in this section outline the more detailed
instructions provided by the Tensorflow team above, but with a few minor
modifications I had to make to get the build to work.

### Prerequisites

Make sure the following are installed:

* [CMake][2]
* [Git][3]
* [SWIG][4]

Additionally, make sure that the CMake and git executables are in your
`%PATH%`.  Then, prepare your environment by running

```
C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\bin\amd64\vcvars64.bat
```

Note that the Tensorflow group's instructions call for running
`vcvarsall.bat` instead, but this script doesn't exist on my system.
Running `vcvars64.bat` appears to have worked for me.

### Download the Tensorflow source

Decide where you want the Tensorflow repository to live.  Something like
`C:\Users\%USERNAME%\bin\` is good.  `cd` to this directory and download the
Tensorflow repository with

```
C:\...> git clone https://github.com/tensorflow/tensorflow.git
```

### Prepare the Visual Studio project files with CMake

All the Tensorflow libraries that we build will be inside the `cmake`
directory in the Tensorflow repository.  We'll make a separate `build`
directory in the `cmake` directory like so:

```
C:\...> cd tensorflow\tensorflow\contrib\cmake
C:\...> mkdir build
C:\...> cd build
```

Now run CMake as follows, making sure to set the build type as Release (the
Debug build is not currently supported).  Only Python 3.5 is supported ---
Python 3.6 is not yet supported, nor is Python 2.  If you run Python through
Anaconda this will not be a problem.  You may have to change the directories
to match wherever the SWIG and Python executables and libraries are on your
system.  (Note that I'm using backticks to continue the command in
PowerShell.  If using the command prompt, end each line with `^`.  Or just
type everything on one line.)

```
C:\...> cmake .. -A x64 -DCMAKE_BUILD_TYPE=Release `
>> -DSWIG_EXECUTABLE=C:\Users\%USERNAME%\bin\swig\swigwin-3.0.12\swig.exe `
>> -DPYTHON_EXECUTABLE=C:\Users\%USERNAME%\Anaconda3\python.exe `
>> -DPYTHON_LIBRARIES=C:\Users\%USERNAME%\Anaconda3\libs\python35.lib
>>
```

After a little while, CMake will have generated a number of Visual Studio
project files.

### Build Tensorflow in Visual Studio

Now in Visual Studio open the Tensorflow solution `tensorflow.sln` in
`tensorflow\tensorflow\contrib\cmake\build`.  The `ALL_BUILD` project should
be highlighted as the startup project.  Make sure that you have the 64-bit
build and Release version set in the Configuration Manager.  Then build
`ALL_BUILD`.  This should take some time (about two hours on my machine).
Note that if (like me) you're running Windows through Parallels, you may
have to substantially increase the memory of the virtual machine (I needed
to set the memory to more than 12 GB --- the default was 1 GB).  Otherwise
you may find that Visual Studio throws a Fatal Error C1060 "compiler is out
of heap space" after an hour and a half.

To check whether everything worked, there is a small program called
`tf_tutorials_example_trainer` which iteratively finds the largest
eigenvalue of a matrix:

```
C:\...> Release\tf_tutorials_example_trainer.exe
```

This should generate a bunch of lines that look something like this:

```
000000/000004 lambda = 2.000000 x = [0.894427 -0.447214] y = [1.788854 -0.894427]
```

[1]: https://github.com/tensorflow/tensorflow/tree/r0.12/tensorflow/contrib/cmake
[2]: https://cmake.org/
[3]: https://git-scm.com/downloads
[4]: http://www.swig.org/download.html
