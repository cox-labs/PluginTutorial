# Plugin Tutorial

MQ Summer School tutorial for Perseus plugin development.
The plugin development tutorial consists of two parts.

# C# plugin API

Most functionality in Perseus is implemented in C#, by following the plugin API
([see online](https://github.com/jurgencox/perseus-plugins)).
We will develop our own simple plugin by modifying the most simple existing plugin (clone matrix).
In the end the plugin will allow us to extract a number of rows from the top of the matrix as specified
by a parameter.

Navigate to the [`/PluginTutorial`](PluginTutorial) folder for more information.

# Script plugins using PluginInterop

Recently we have started to develop a light-weight approach to plugin programming.
We aim to enable you to use popular scripting languages such as R and Python
from within Perseus. We will see, how to implement the same functionality as before
in R and Python instead of C#.

Navigate to the [`/scripts`](scripts) folder for more information.
