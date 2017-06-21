# Script based plugin programming

[PluginInterop](https://github.com/jdrudolph/PluginInterop/) provides facilities
for using and programming light-weight plugins for Perseus by using external
scripting languages such as R or Python.

We developed packages in the R and Python languages which allow them to easily
process Perseus data structures. Please make sure
to have these packages installed on your machine by following the instructions
given on their websites.

* **R**: [PerseusR](https://github.com/jdrudolph/perseusr).
* **Python**: [perseuspy](https://github.com/jdrudolph/perseuspy).

## Step by step

1. Copy `PluginInterop.dll` to your Perseus installation.

2. Write a script file in your language of choice. For examples check the `/scripts`
folder and the package websites.

3. Open Perseus and create a random data matrix. In the `External` menu you
will find processing activities for both `R` and `Python`.

