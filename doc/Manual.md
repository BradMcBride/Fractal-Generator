# Fractal Visualizer User Manual

## Introduction
Welcome to the Fractal Visualizer! The Fractal Visualizer is a program that creates a picture of different fractals and fractal patterns. Assuming that you have a copy of all the necessary files of the fractal visualizer, this guide will help you to run the program and explain what you should expect.

## Getting Started
Within your terminal, make sure that you are in the project file location on your computer. You can do this via the ```$cd (DIRECTORY NAME)``` command.
Depending on where you downloaded this project and what you named it, these steps may very. For example, if the file name on your computer is ```cs1440-assn4```, you would run the command ```$cd cs1440-assn4``` to enter the directory.
Once inside the directory, you will then enter inside of the ```src/``` directory. This will enter into the directory of all the codes needed to run the program. Do this by running ```$cd src/``` on the terminal.

## Commands
To run the program, enter ```$python main.py```. If the program is properly installed on your computer it should output:
```
$ python main.py
Please provide the name of a fractal as an argument
        phoenix
        peacock
        monkey-knife-fight
        shrimp-cocktail
        elephants
        leaf
        mandelbrot
        mandelbrot-zoomed
        seahorse
        spiral0
        spiral1
        starfish
```
This will show you all the possible fractals you can choose from.
Once you choose which fractal you want to print out, you can type in the command ```$python main.py PATTERN``` and replace ```PATTERN``` with one of the above fractal arguments.
If everything is typed out correctly, you should be presented with a separate windows tab with a fractal that is generated top to bottom, line by line.
On the terminal, it will also output something similar to:
```
$ python main.py peacock
Rendering peacock fractal
[100% =================================]
Done in 10.995 seconds!
Saved image to file peacock.png
Close the image window to exit the program
```
Of course, this example has the chosen fractal as peacock, but you don't have to choose this one.
Also notice that the loading bar is constantly updating based on the percentage of the picture printed out.
It will then tell you the amount of time it took to create, (this time will vary based on computer and type of fractal chosen).
Finally, it will tell you that it saved the image and how to close the window and end the program.
Now you have a picture of the fractal you chose, congratulations! You can end the program by exiting out of the picture tab.

## Troubleshooting
If your program isn't running as expected, you can try a few things that may fix your problem.
First, **check your spelling**! This program is not only case-sensitive (meaning the fractal must be in all lowercase), but it also must be spelled perfectly.
If the spelling isn't correct, it will print out the information asking to provide a fractal argument (same output as running ```$python main.py```). Simply change the command and try running it again.

Next, if you try inputting more than one fractal, it will only print out the first fractal argument and ignore the rest of the arguments given. 
For example, if you input ```$python main.py peacock leaf```, it will only print out the ```peacock``` fractal and ignore the ```leaf``` command.

Finally, if you still run into any issues, try checking that the python version on your computer is up-to-date and triple check that the command you typed in is correct.

## Conclusion
Thank you for using the Fractal Visualizer! I hope that everything you enjoy exploring the intricate and mesmerizing patterns of the different fractal set.
Please enjoy any further updates to this program and be on the lookout for any new updated manuals for new functionalities.

