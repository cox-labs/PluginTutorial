# Plugin Tutorial

MQ Summer School tutorial for Perseus plugin development.
The plugin development tutorial consists of two parts. Make sure
to have all the requirements installed.

## MaxQuant summer school plugin programming bootcamp

[![YouTube](http://img.youtube.com/vi/-3oq9e_92lc/0.jpg)](http://www.youtube.com/watch?v=-3oq9e_92lc)

## C# plugin API

Most functionality in Perseus is implemented in C#, by following the plugin API
([see online](https://github.com/jurgencox/perseus-plugins)).
We will develop our own simple plugin by modifying the most simple existing plugin (clone matrix).
In the end the plugin will allow us to extract a number of rows from the top of the matrix as specified
by a parameter.

Navigate to the [`/PluginTutorial`](PluginTutorial) folder for more information.

### Requirements

See in [`PluginTutorial` README](PluginTutorial#requirements).

### Example plugins

Besides the plugin in this repository you can check out:

* [PluginUpperCase](https://github.com/cox-labs/PluginUpperCase) is a simple plugin to change all strings to upper case.

## Script plugins using PluginInterop

Recently we have started to develop a light-weight approach to plugin programming.
We aim to enable you to use popular scripting languages such as R and Python
from within Perseus. We will see, how to implement the same functionality as before
in R and Python instead of C#.

Navigate to the [`/scripts`](scripts) folder for more information.

### Requirements

See in [`scripts` README](/scripts#requirements--installation).

#### Python

We recommend installing the [Anaconda Python distribution](https://www.continuum.io/downloads)
(Python 3.X 64bit). In the installer make sure to enable the option to add Python to your
`PATH`.

Next you should install the `perseuspy` module.
If `python` is in your `PATH` you should be able to open a Command Prompt (search for `cmd.exe`) and
type in the installation instructions from the [`perseuspy` website](https://github.com/cox-labs/perseuspy).

#### R

First install the latest version of [R](https://cran.rstudio.com/bin/windows/base/). We recommend
to additionally install [R Studio Desktop](https://www.rstudio.com/products/rstudio/download/).

Next install the `PerseusR` package. Open R Studio and enter the instructions on the [website](https://github.com/cox-labs/perseusr) into the running `R` session.

### Example plugins

Besides the plugin scripts in this repository you can check out:

* [PluginDependentPeptides](https://github.com/cox-labs/PluginDependentPeptides) is a plugin for reading the dependent peptide search
  results into Perseus. This plugin is a hybrid of C# code for parameter passing and a Python script for the actual processing.
