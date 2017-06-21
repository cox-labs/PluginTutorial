# PluginTutorial

MQ Summer School tutorial for Perseus plugin development.

## Overview

We will develop our own simple plugin by modifying the most simple existing plugin (clone matrix).

## Step by step

1. Go to [perseus-plugins](https://github.com/jurgencox/perseus-plugins) github repository. The code for the plugin API
(`PerseusApi`) and for a number of Perseus plugins (`PerseusPluginLib`) is hosted here.

2. Find the `CloneProcessing.cs` class which we will use as our template. Use the search or navigate to `/PerseusPluginLib/Basic`
and open [`CloneProcessing.cs`](https://github.com/JurgenCox/perseus-plugins/blob/master/PerseusPluginLib/Basic/CloneProcessing.cs)

3. Copy the code into `HeadProcessing.cs`. You will see lots of errors which we will fix momentarily. The errors are due to
missing dependencies. As you can see from the `using` statements at the top of the file we require the Perseus plugin API.

4. Add dependencies: Right-click on your solution and choose `Manage NuGet Packages for Solution...`. In the `Browse` tab search for `PerseusApi`
and install it for `PluginTutorial`

5. There are only a few things left to do before we can try our new plugin. Correct the namespace to `namespace PluginTutorial` and the class to `class HeadProcessing`.
Set the `DisplayImage => null` and adjust all other strings in the class.
Now you can build the solution. Navigate to the `/bin/Debug` folder and copy the `PluginTutorial.dll` to the Perseus folder. Run perseus, generate
some random data and try the plugin. [commit `96ce38c2`]

6. Now we need to implement the functionality we need. We can look for inspiration in the [filter random rows](https://github.com/JurgenCox/perseus-plugins/blob/master/PerseusPluginLib/Filter/FilterRandomRows.cs)
processing. We can see a call to [`PerseusPluginUtils.FilterRows(...)`](https://github.com/JurgenCox/perseus-plugins/blob/master/PerseusPluginLib/Filter/FilterRandomRows.cs#L43)
which is turn uses [`mdata.ExtractRows(rows)`](https://github.com/JurgenCox/perseus-plugins/blob/master/PerseusPluginLib/Utils/PerseusPluginUtils.cs#L50).
We can utilize the same function to implement our plugin! [commit `3e3b020b`]

	```csharp
	var numberOfRows = 10;
	var indices = Enumerable.Range(0, numberOfRows).ToArray();
	mdata.ExtractRows(indices);
	```

7. Next we should add a parameter to let us choose how many rows we would like to keep. Again we take inspiration from the same existing filter random rows plugin.
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

