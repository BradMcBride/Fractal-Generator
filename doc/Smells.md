# CS 1440 Assignment 4.0: Refactoring - Code Smells Report

## Instructions

Edit this file and include it in your submission.

For each code smell found in the starter code:

*	Note where you found it (filename + relative information to locate the smell)
    *   You do not need to list code smells in any particular order
*	Describe the smell and why it is a problem
*	Paste up to 10 lines of offensive code between a triple-backtick fence `` ``` ``
    *   If the block of bad code is longer than 10 lines, paste a brief, representative snippet
*	Describe how you can fix it
    *   We will follow up on these notes to make sure it was really fixed!
*   At least *one instance* of each smell is required for full marks
    *   Reporting one smell multiple times does not make up for not reporting another smell
    *   Ex: reporting two global variables does not make it okay to leave spaghetti code blank



## 10 Code Smells

If you find a code smell that is not on this list, please add it to your report.

0.  **Magic** numbers
    *   These are literal values used in critical places without any context or meaning
    *   "Does the `256` right here have anything to do with the `256` over there?"
1.  **Global** variables
    *   Used to avoid passing a parameter into a function
    *   Used to return an extra value from a function
    *   There are better ways to meet both of these needs!
    *   *Note, this does not apply to global `CONSTANTS`!*
2.  **Poorly-named** identifiers
    *   Variable names should strike a good balance between brevity and descriptiveness
    *   Short variable names are okay in some situations:
        *   `i` or `j` as a counter in a brief `for` loop
        *   Variables from well-known math formulae should match the textbook (i.e. `a`, `b` and `c` are familiar in a quadratic or Pythagorean formula)
        *   Otherwise, short names should be avoided
    *   Variables with really, really long names make code harder to read
    *   Variables that override or "shadow" other identifiers
        *   Builtin Python functions such as `input`, `len`, `list`, `max`, `min` and `sum` are especially susceptible to this
3.  **Bad** Comments
    *   Comments are condiments for code; a small amount can enhance a meal, but too much ruins it
    *   Strive to write clear, self-documenting code that speaks for itself; when a line needs an explanatory comment to be understood, it indicates that identifier names were poorly chosen
    *   Delete obsolete remarks that no longer accurately describe the situation
    *   The same goes for blocks of commented-out code that serve no purpose and clutter up the file
    *   Programmers sometimes vent their frustration with snarky or vulgar comments; these add no value, are unprofessional and embarrassing, and only serve to demoralize maintainers
4.  **Too many** arguments
    *   Seen when more than a handful of parameters are passed to a function/method
    *   Parameters that are passed in but never used
5.  Function/Method that is **too long**
    *   Too many lines of code typically happens because the function/method has too many different responsibilities
    *   Generally, a method longer than a dozen lines should make you ask yourself these questions
        *   "Does one function really need to do all of this work?"
        *   "Could I split this into smaller, more focused pieces?"
6.  **Redundant** code
    *   A repeated statement which doesn't have an effect the second time
    *   Ask yourself whether it makes any difference to be run more than once
    *   ```python
        i = 7
        print(i)
        i = 7
        ```
7.  Decision tree that is **too complex**
    *   Too long or deeply nested trees of `if/elif/else`
    *   Are all of the branches truly necessary?
    *   Can all branches even be reached?
    *   Has every branch been tested?
8.  **Spaghetti** code
    *   Heaps of meandering code without a clear goal
    *   Functions/objects used in inconsistent ways
    *   Many variables are used to keep track of
    *   Conditional statements with long, confusing Boolean expressions
    *   Boolean expressions expressing double negatives; ex. `if not undone: ...`
    *   Code that makes you say "It would be easier to rewrite this than to understand it"
9.  **Dead** code
    *   Modules that are imported but not used
    *   Variables that are declared but not used
    *   Lines that are *never* run because they are placed in an impossible-to-reach location
        *   Code that appears after a `return` statement
            *   ```python
                return value
                value += 1
                ```
        *   Blocks of code guarded by an impossible-to-satisfy logical test
            *   ```python
                two_bee = True
                if two_bee and not two_bee:
                    print("If can you see this message, it is time to get a new CPU")
                ```
            *   ```python
                counter = 100
                while counter < 0:
                    print(f"T minus {counter}...")
                    counter -= 1
                ```
    *   Functions that are defined but never called *may* or *may not* be dead code
        *   In **Code Libraries** it is normal to define functions that are not meant to be used in the library itself
            *   It is okay to keep these functions
        *   As an **Application** evolves, calls to some of its functions may be removed until only the function's definition remains
            *   Some programmers may keep these functions "just in case" they are needed again
            *   We don't do this at DuckieCorp because we have Git; if we ever need to recover that function, we can find it in the repo's history


### Template

0.  Smell at `file` [lines xx-yy or general location]
    *   [Brief description of smell]
    *   [Code Snippet between triple-backquotes `` ``` ``]
    *   [How to resolve]


### Example

0.  Redundant Code at `src/main.py` [lines 28, 30]
    *   The import statement `import mbrot_fractal` occurs twice.  A second occurrence doesn't do it better than the first
    *   ```python
        import mbrot_fractal
        import phoenix_fractal as phoenix
        import mbrot_fractal
        ```
    *   Remove the second `import` statement



## Code Smells Report

0. Magic Numbers at ```mbrot_fractal.py``` [lines 237 and more]
    * The number 512 is used many times throughout the paint method. There are, however, no mentions of what this number is.
   * ```python
        canvas = Canvas(window, width=512, height=512, bg='#000000') 
     ```
   * This fix would be as simple as naming the variable 512 to whatever it represents. From my understanding, this is the number of pixels in the canvas length. 
   Since the picture is going to be a square, you could rename the variable to ```canvasLength``` or ```canvasSize```, but if you wanted to (in the future) change the default canvas size, you could break it into two separate variables.
1. Global Variable at ```mbrot_fractal.py``` [lines 224]
    * The global variable ```palette``` is used to not have to pass in a ```palette``` variable in the paint function.
    ```python
   def paint(fractals, imagename, window):
        global palette
   ```
   * The fix would be to simply pass in the ```palette``` variable into the method's parameters and remove the global variable. You would also have to change any calls to this method to include the palette.
2. Poorly-named identifiers at ```phoenix_fractal.py``` [lines 128]
    *   Too many variables declared with unclear purpose and poorly named.
   ```python
    def makePictureOfFractal(f, i, e, w, g, p, W, a, b, s):
    ```
   * First only five of the parameters are used so you could remove those. Regardless, to fix it you should rename the variables to reflect their purpose. For example, 
   ```
     f => fractalType
     w => window
     p => photoImage
     W => color
     s => canvasLength or size
    ``` 
3. Bad Comments at ```mbrot_fractal.py``` [line 247]
    * Bad comment that serves no purpose. 
    ```
   # loop
   ```
   * There were a lot of bad comments, but this one made me chuckle. It doesn't serve any purpose because we can see that it is a loop and don't need a comment to see that. The fix would be to simply remove it.
4. Too many arguments at ```phoenix_fractal.py``` [line 128]
    * Too many arguments which some have no purpose at all.
   ```python
    def makePictureOfFractal(f, i, e, w, g, p, W, a, b, s):
    ```
   * Parameters ```i, e, g, a, b``` are never used. Remove them.
5. Function/Method that is too long at ```pheonix_fractal.py``` [lines 128-214]
   * Way too many lines of code for one function. Doing to much for one thing.
   ```python
      min = ((f['centerX'] - (f['axisLength'] / 2.0)),
               (f['centerY'] - (f['axisLength'] / 2.0)))
     max = ((f['centerX'] + (f['axisLength'] / 2.0)),
               (f['centerY'] + (f['axisLength'] / 2.0)))
    ...
    tk_Interface_PhotoImage_canvas_pixel_object.create_image((s/2, s/2), image=p, state="normal")
    tk_Interface_PhotoImage_canvas_pixel_object.pack()
    ...
        while r in range(s, 0, -1):
            cs = []
            for c in range(s):
                X = min[0] + c * size
                Y = 0
                cp = getColorFromPalette(complex(X, Y))
                Y = min[1] + r * size
    ...
    ```
   * This function is trying to do too many things in one function. It may be beneficial to break it up into a basic fractal information and the printing of the fractal and status bar.
6. Redundant Code at ```main.py``` [lines 98-99]
    * Redundant and unnecessary code.
    ```python
   i=0
   i=0
   ```
   * Remove one of these i's
7. Decision tree that is too complex at ```main.py``` [lines 157-165]
   * Too many if/elif branches, which some are not even accessible.
   ```python
    if PHOENX.count(sys.argv[1])>0: phoenix.phoenix_main(sys.argv[1])
    elif sys.argv[1] in MBROTS and len(sys.argv) > 1 and 2 <= len(sys.argv[0]):
        fractal = sys.argv[1]
        mbrot_fractal.mbrot_main(fratcal)
    elif len(sys.argv) != 0 and fratcal in PHOENX and len(sys.argv) != 1:
        phoenix.phoenix_main(fractal)
    else: print("The fractal given on the command line",
                fractal,
                "was not found in the command line")
    ```
   First, the third and forth branch can't even be accessed. Second, there is a way easier way to do this. Simply check if the arguments is greater than one, and if ```sys.argv[1]``` is in either ```PHOENX``` or ```MBROTS```, run the command.
8. Spagetti code at ```main.py``` [lines 68-118]
    * A lot of unclear code, unclear variables, double negatives, and more.
   ```python
   ...
    exit = None          ############################## (c) 2023 #############
    i = 0                 ##############   #####################################
    i = 0                   ##########     ####################################
    fractal = ''            #    ## #       ####################################
    while not exit:                          ################################
        print("\t" + MBROTS[i])               #  ############################
        if PHOENX[iter] =='shrimp-cocktail':    ######################### ####
            if MBROTS[i]  == 'starfish':       ### #  ## ##############   #
                i = i + 1                                  #######
                exit = PHOENX[iter] =='shrimp-cocktail'    #######
                i -= 1 #need to back off, else index error   ###
                exit = exit and MBROTS[i]  == 'starfish'
    ```
   * This is just one snippet of the spaghetti code. The fix is to get rid of all the necessary variables, fix the double negative functions/just use primitive datasets, and clear the functions' logic so it's less convoluted.
9. Dead code at ```main.py``` [lines 113-114]
    * Code is never used because it is followed by a exit statement.
    ```python
    sys.exit(1)
    print("Those are all of the choices")`
    ```
    * Simply remove the line after the system exit.