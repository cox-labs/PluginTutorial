# PluginTutorial

MQ Summer School tutorial for Perseus plugin development.

## Overview

We will develop our own simple plugin by modifying the most simple existing plugin (clone matrix).

## Step by step

1. Go to (https://github.com/jurgencox/perseus-plugins)[perseus-plugins] github repository. The code for the plugin API
(`PerseusApi`) and for a number of Perseus plugins (`PerseusPluginLib`) is hosted here.

2. Find the `CloneProcessing.cs` class which we will use as our template. Use the search or navigate to `/PerseusPluginLib/Basic`
and open (https://github.com/JurgenCox/perseus-plugins/blob/master/PerseusPluginLib/Basic/CloneProcessing.cs)[`CloneProcessing.cs`]

3. Copy the code into `HeadProcessing.cs`. You will see lots of errors which we will fix momentarily. The errors are due to
missing dependencies. As you can see from the `using` statements at the top of the file we require the Perseus plugin API.

4. Add dependencies: Right-click on your solution and choose `Manage NuGet Packages for Solution...`. In the `Browse` tab search for `PerseusApi`
and install it for `PluginTutorial`

5. There are only a few things left to do before we can try our new plugin. Correct the namespace to `namespace PluginTutorial` and the class to `class HeadProcessing`.
Set the `DisplayImage => null` and adjust all other strings in the class.
Now you can build the solution. Navigate to the `/bin/Debug` folder and copy the `PluginTutorial.dll` to the Perseus folder. Run perseus and try the plugin.