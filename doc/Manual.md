# Fractal Visualizer User Manual

## Introduction
Welcome to the Fractal Visualizer! The Fractal Visualizer is a program that creates a picture of different fractals and fractal patterns. Assuming that you have a copy of all the necessary files of the fractal visualizer, this guide will help you to run the program and explain what you should expect.

## Getting Started
Within your terminal, make sure that you are in the project file location on your computer. You can do this via the ```$cd (DIRECTORY NAME)``` command.
Depending on where you downloaded this project and what you named it, these steps may very. For example, if the file name on your computer is ```cs1440-assn4```, you would run the command ```$cd cs1440-assn4``` to enter the directory.

## Commands

To run the program, enter ```$python src/main.py```.
If everything is typed out correctly, you should be presented with a separate windows tab with a fractal that is generated top to bottom, line by line.
On the terminal, it should also output:
```
$ python src/main.py
FractalFactory: Creating default fractal
PaletteFactory: Creating default color palette
[100% =================================]
Done in 1.266 seconds!
Saved image to file mandelbrot.png
Close the image window to exit the program
```

As you can see, a picture of the default fractal will be printed out on your screen.
This is cool enough, but this program is able to do so much more! For one, you can choose which fractal you want to print!
Once you decide which fractal you want to print out, you can type in the command ```$python src/main.py data/FRACTAL_FILE``` and replace ```FRACTAL_FILE``` with one of the fractal files downloaded on your computer.
Be aware, not all the fractal types are implemented yet, but just check the type of fractal your fractal file is and the currently implemented ones.
On the terminal, it will also output something similar to:
```
$ python src/main.py data/phoenix.frac
Rendering phoenix fractal
PaletteFactory: Creating default color palette
[100% =================================]
Done in 10.995 seconds!
Saved image to file peacock.png
Close the image window to exit the program
```
Of course, this example has the chosen fractal as phoenix, but you don't have to choose this one.
The line that says "PaletteFactory: Creating default color palette" means that no custom color palette was given, so it simply uses a default color palette.
Also notice that the loading bar is constantly updating based on the percentage of the picture printed out.
It will then tell you the amount of time it took to create, (this time will vary based on computer and type of fractal chosen).
Finally, it will tell you that it saved the image and how to close the window and end the program.
Now you have a picture of the fractal you chose, congratulations! You can end the program by exiting out of the picture tab.

One more thing though! You can also choose from different pre-made color palettes to make the fractals have different colors.
When running this program with non-default values, it should follow the same pattern:

```$ python src/main.py [FRACTAL_FILE [PALETTE_NAME]]```

If you give the program a non-existent/non-accessible file, or the color palette name doesn't exist, it won't work.

## All Available Fractals and Palettes
Any fractals with the type: ```mandelbrot```, ```phoenix```, ```mandelbrot3```, or ```spider```

Default Fractal Type: ```mandelbrot```

Color Palette: ```gradient``` (Smooth gradient between grey and pink)

Color Palette: ```intergalactic``` (Spaced themed gradient with purple fractals and black background)

Color Palette: ```random``` (Creates a gradient between three random colors)

Default Color Palette: ```gradient```

## Troubleshooting
If your program isn't running as expected, you can try a few things that may fix your problem.
**Check your spelling**! Make sure that the location of the fractal is spelled correctly and that the file is there. Also check the spelling of the unique color palette (if applicable).
Another thing that you can check to see is if the fractal file you are trying to use uses a not implemented fractal. Check the list above for all the available gradients and fractals.
If you still run into any issues, try checking that the python version on your computer is up-to-date and triple check that the command you typed in is correct.

## Conclusion
Thank you for using the Fractal Visualizer! I hope that everything you enjoy exploring the intricate and mesmerizing patterns of the different fractal set.
Please enjoy any further updates to this program and be on the lookout for any new updated manuals for new functionalities.

