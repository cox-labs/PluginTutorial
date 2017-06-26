# Script based plugin programming

[PluginInterop](https://github.com/jdrudolph/PluginInterop/) provides facilities
for using and programming light-weight plugins for Perseus by using external
scripting languages such as R or Python.

We developed packages in the R and Python languages which allow them to easily
process Perseus data structures. Please refer to their websites for more information.

* **R**: [PerseusR](https://github.com/jdrudolph/perseusr).
* **Python**: [perseuspy](https://github.com/jdrudolph/perseuspy).

## Requirements / Installation

In order to run external scripts from within Perseus we need to install (i)
`PluginInterop`, (ii) the scripting language we want to use, and (iii) the
interop package for each language.

First follow the [`Plugin Interop` installation instructions](https://github.com/jdrudolph/PluginInterop/)
and add `PluginInterop.dll` to your Perseus installation. The next steps
depend on the scriting language you intend to use.

### Python

We recommend installing the [Anaconda Python distribution](https://www.continuum.io/downloads)
(Python 3.X 64bit). In the installer make sure to enable the option to add Python to your
`PATH`.

Next you should install the `perseuspy` module.
If `python` is in your `PATH` you should be able to open a Command Prompt (search for `cmd.exe`) and
type-in the installation instructions from the [`perseuspy` website](https://github.com/jdrudolph/perseuspy).

### R

First install the latest version of [R](https://cran.rstudio.com/bin/windows/base/). We recommend
to additionally install [R Studio Desktop](https://www.rstudio.com/products/rstudio/download/).

Next, install the `PerseusR` package. First open R Studio and then,
enter the instructions on the [website](https://github.com/jdrudolph/perseusr) into the running `R` session.

## Usage: Step by step

1. Write a script file in your language of choice. For examples check the `/scripts`
folder and the package websites.

2. Open Perseus and create a random data matrix. In the `External` menu you
will find processing activities for both `R` and `Python`.

