# Building on Linux

We can build `mmSolver` on Linux quite easily. We have provided a
CMake build script which is easily usable, configurable and readable.

On Linux we have tested three different library dependency combinations:
1. With `levmar` only.
2. With `levmar` and `ATLAS` for improved speed and robustness.
3. Or, With `levmar` and `Intel MKL` for improved speed and robustness.

# Edit the Build Scripts

The build scripts (`build_with_*.sh`) will assume a default Maya 2017
install directory. You will need to edit the build script with your
custom Maya include and library directories.

For example you will need to set the following variables in the `.sh`
file:

| Variable           | Description                            | Example                          |
| ------------       | -----------                            | -----------                      |
| MAYA_VERSION       | Maya version to build for.             | `2017`                           |
| MAYA_INCLUDE_PATH  | Location for Maya header (.h) files.   | `/usr/autodesk/maya2017/include` |
| MAYA_LIB_PATH      | Location for Maya library (.so) files. | `/usr/autodesk/maya2017/lib`     |
| INSTALL_MODULE_DIR | Directory to install the Maya module.  | `~/maya/2017/modules`            |

# Build with levmar

After the build script variables are set, you can now run the build
script.

To build without any third-party dependencies other than `levmar`, run
these commands:
```commandline
$ cd <project root>
$ bash external/download_all_archives.sh
$ build_with_levmar.sh
```

NOTE: Replace ``<project root>`` as required.

Using the `build_with_levmar.sh` script will combine `levmar`
into the shared library `mmSolver.so`. This means you only need one
plug-in file, and do not need to worry about setting
`LD_LIBRARY_PATH` paths.

Following the steps above you should have the Maya plug-in compiled,
and installed into your
`~/maya/MAYA_VERSION/modules` directory.

For the next steps, see
[BUILD.md]([[https://github.com/david-cattermole/mayaMatchMoveSolver/blob/master/BUILD.md]])
 for more details.

# Build with levmar and ATLAS

After the build script variables are set, you can now run the build
script.

This section is for compiling with the free and open-source library
`ATLAS`.

This method will use the `levmar` algorithm, and `Automatically Tuned
Linear Algebra Software (ATLAS)` for performance computation and
stability. `ATLAS` is Free Open Source Software, Using a third-party
maths library is recommended by the `levmar` project.

This will assume `atlas` is installed via yum on CentOS 7.x. If you
wish to build your own custom `atlas` library it is an undocumented
exercise for the user. On CentOS 7.x you may install `atlas` with the
following command (as `root` user):

```commandline
$ yum install atlas.x86_64 atlas-devel.x86_64
$ yum install lapack64.x86_64 lapack64-devel.x86_64
```

After ATLAS has been installed, you may build `mmSolver`
with ATLAS using these commands:
```commandline
$ cd <project root>
$ bash external/download_all_archives.sh  # Download archives (only required once)
$ bash build_with_atlas.sh
```

NOTE: Replace ``<project root>`` as required.

Following the steps above you should have the Maya plug-in compiled,
and installed into your
`~/maya/MAYA_VERSION/modules` directory.

For the next steps, see
[BUILD.md]([[https://github.com/david-cattermole/mayaMatchMoveSolver/blob/master/BUILD.md]])
 for more details.

# Build with levmar and Intel MKL

After the build script variables are set, you can now run the build
script.

This method will use both the `levmar` algorithm, as well as
highly-optimised libraries for computation; `Intel Math Kernel
Libraries (Intel MKL)`. `Intel MKL` is proprietary closed-source
software. Using a third-party maths library is recommended by the
`levmar` project.

Intel MKL must be installed manually, this build script will not
install it for you. You will need to sign up, download and install
from the [Intel MKL website](https://software.intel.com/en-us/mkl).

The instructions below assume Intel MKL is installed under
`/opt/intel/mkl`, you will need to modify the scripts if this location
is not correct on your system.

To build with `Intel MKL`, run these command:
```commandline
$ cd <project root>
$ bash external/download_all_archives.sh  # Download archives (only required once)
$ bash build_with_intel_mkl.sh
```

NOTE: Replace ``<project root>`` as required.

Following the steps above you should have the Maya plug-in compiled,
and installed into your
`~/maya/MAYA_VERSION/modules` directory.

For the next steps, see
[BUILD.md]([[https://github.com/david-cattermole/mayaMatchMoveSolver/blob/master/BUILD.md]])
 for more details.

# CMake Build Script

For those needing or wanting to compile the ``mmSolver`` Maya plug-in
manually you can do it easily using the following commands.

```commandline
$ cd <project root>
$ mkdir build
$ cd build
$ cmake -DCMAKE_BUILD_TYPE=Release \
        -DCMAKE_INSTALL_PREFIX=~/maya/2017/modules \
        -DMAYA_VERSION=2017 \
        -DMAYA_INCLUDE_PATH=/usr/autodesk/maya2017/include \
        -DMAYA_LIB_PATH=/usr/autodesk/maya2017/lib \
        -DLEVMAR_INCLUDE_PATH=${PROJECT_ROOT}/external/include \
        -DLEVMAR_LIB_PATH=${PROJECT_ROOT}/external/lib \
        -DUSE_ATLAS=0 \
        -DUSE_MKL=0 \
        -DATLAS_LIB_PATH=${PROJECT_ROOT}/external/lib \
        -DMKL_LIB_PATH=/opt/intel/mkl/lib/intel64 \
        ..
$ make -j4
# Install 
$ make install
$ make package
```

| CMake Option         | Description                                 |
| -------------------- | ------------------------------------------- |
| CMAKE_BUILD_TYPE     | The type of build (`Release`, `Debug`, etc) |
| CMAKE_INSTALL_PREFIX | Location to install the Maya module.        |
| MAYA_VERSION         | Maya version to build for.                  |
| MAYA_INCLUDE_PATH    | Directory to the Maya header include files  |
| MAYA_LIB_PATH        | Directory to the Maya library files         |
| LEVMAR_INCLUDE_PATH  | Directory to levmar header includes         |
| LEVMAR_LIB_PATH      | Directory to levmar library                 |
| USE_ATLAS            | Use ATLAS libraries?                        |
| USE_MKL              | Use Intel MKL libraries?                    |
| ATLAS_LIB_PATH       | Directory to ATLAS libraries                |
| MKL_LIB_PATH         | Directory to Intel MKL libraries            |

Setting ``USE_ATLAS`` and ``USE_MKL`` to ``1`` is an error, both
libraries provide the same functionality and both are not needed,
only one. If `ATLAS` and `Intel MKL` are not required you may set both
``USE_ATLAS`` and ``USE_MKL`` to ``0``.

You can read any of the build scripts to find out how they work.
The build scripts can be found in `<project root>/build_with_*.sh`
and `<project root>/external/*.sh`.

# Building Packages

For developers wanting to produce a pre-compiled archive "package",
simply add the following line, after `make install` in the
`build_with_*.sh` build script:

```cmd
make package
```

And re-run the `build_with_*.sh` script. This will re-compile the
project, then copy all scripts and plug-ins into a `.tar.gz` file,
ready for distribution to users.
