# PluginTutorial

## Overview

We will develop our own simple plugin by modifying the most simple existing plugin (clone matrix).
In the end the plugin will allow you to extract a number of rows from the top of the matrix as specified
by a parameter.

Reading existing code and modifying it is the fastes way to learning plugin development.
This way we can not only understand how things work but also easily reuse existing functionality for our needs.

## Requirements

Download the latest version of [Visual Studio Community Edition](https://www.visualstudio.com/downloads/).
Select the `.Net Desktop Development` workflow in the installer to install everything required.

## Step by step

1. Go to [perseus-plugins](https://github.com/jurgencox/perseus-plugins) github repository. The code for the plugin API
(`PerseusApi`) and for a number of Perseus plugins (`PerseusPluginLib`) is hosted here.

2. Find the `CloneProcessing.cs` class which we will use as our template. Use the search or navigate to `/PerseusPluginLib/Basic`
and open [`CloneProcessing.cs`](https://github.com/JurgenCox/perseus-plugins/blob/master/PerseusPluginLib/Basic/CloneProcessing.cs)

3. Open Visual Studio and create a new project of type `Class Library (.Net Framework)`
and name it `PluginTutorial`. Rename the default `Class1.cs` to
`HeadProcessing.cs` remove all existing code in the file and copy the code from
`CloneProcessing.cs` into it.  You will see lots of errors which we will fix
momentarily.  The errors are due to missing dependencies. You can see from the
`using` statements at the top of the file that we require the Perseus plugin
API.

4. To add the dependencies right-click on your `PluginTutorial` solution and 
choose `Manage NuGet Packages for Solution...`. In the `Browse` tab search for
`PerseusApi` and install it for `PluginTutorial`. `PerseusApi` and its
dependency `BaseLibS` will now be added to your project.

5. There are only a few things left to do before we can try our new plugin.
Correct the namespace to `namespace PluginTutorial` and the class to `class
HeadProcessing`.  Set the `DisplayImage => null` and adjust all other strings
in the class.  Now you can build the solution. Use the Windows File Explorer to
navigate to the `PluginTutorial/bin/Debug` folder and copy the
`PluginTutorial.dll` to the Perseus folder.  Start Perseus, generate some
random data and try your plugin [commit `96ce38c2`].

6. Now we need to implement the actual functionality in the [`ProcessData(..)`]
method. We can look for inspiration in the [filter random
rows](https://github.com/JurgenCox/perseus-plugins/blob/master/PerseusPluginLib/Filter/FilterRandomRows.cs)
processing. We can see a call to
[`PerseusPluginUtils.FilterRows(...)`](https://github.com/JurgenCox/perseus-plugins/blob/master/PerseusPluginLib/Filter/FilterRandomRows.cs#L43)
which is turn uses
[`mdata.ExtractRows(rows)`](https://github.com/JurgenCox/perseus-plugins/blob/master/PerseusPluginLib/Utils/PerseusPluginUtils.cs#L50).
We can utilize the same function to implement our plugin!

	```csharp
	var numberOfRows = 10;
	var indices = Enumerable.Range(0, numberOfRows).ToArray();
	mdata.ExtractRows(indices);
	```
	Make sure to build your solution and try out your now functional plugin! [commit `3e3b020b`]

7. Manually copying the DLL after each build is very annoying and reduces productivity. We can
use Visual Studio to automatically copy the DLL after each build and launch Perseus in debug
mode. Right click the `PluginTutorial` project in the Solution Explorer and select `Properties`.
In the `Build Event` tab we can edit the post-build event. Let's add a copy statement.

	```batch
	copy $(TargetDir)\PluginTutorial.dll C:\Path\To\Perseus\bin\PluginTutorial.dll
	copy $(TargetDir)\PluginTutorial.pdb C:\Path\To\Perseus\bin\PluginTutorial.pdb
	```

The `$(TargetDir)` macro always points to the output directory of the build.
Now switch to the `Debug` tab and select `Start external Program`. Browse for,
or enter the path to the `Perseus\bin\PerseusGui.exe`. Now hit the green Start
button.

8. As a last step we should add a parameter to let us choose how many rows we would like to keep. Again we take inspiration from the same existing filter random rows plugin.
In its `GetParameters(...)` function it's initializing a [`IntParam`](https://github.com/JurgenCox/perseus-plugins/blob/master/PerseusPluginLib/Filter/FilterRandomRows.cs#L34).
To obtain its value it is extracting the parameter in the [`ProcessData`](https://github.com/JurgenCox/perseus-plugins/blob/master/PerseusPluginLib/Filter/FilterRandomRows.cs#L39) function.
We can again utilize this in our plugin by creating our parameter in our `GetParameters` function:
	```csharp
	return new Parameters(new IntParam("Number of rows", 10));
	```
	And using it in the `ProcessData` function:

	```csharp
	var numberOfRows = param.GetParam<int>("Number of rows").Value;
	var indices = Enumerable.Range(0, numberOfRows).ToArray();
	mdata.ExtractRows(indices);
	```
	Build your solution another time and check to see that the parameters are handled correctly!

## Next steps

### Error handling
Error handling can be implemented via the `ProcessInfo` object passed to both the `GetParameters` and the `ProcessData` functions.
[Here](https://github.com/JurgenCox/perseus-plugins/blob/master/PerseusPluginLib/Basic/DeHyphenateIds.cs#L32-L36) for example it is used to verify
that a parameter was assigned a valid value.
