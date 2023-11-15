from tkinter import Tk, Canvas, PhotoImage, mainloop
from time import time
import sys
import Mandelbrot
import Palette
IMAGE_SIZE = 512
def mbrot_main(fractalSettup, fractalName):
    global img
    print("Rendering {} fractal".format(fractalName), file=sys.stderr)
    before = time()
    window = Tk()
    img = PhotoImage(width=IMAGE_SIZE, height=IMAGE_SIZE)
    paint(fractalSettup, fractalName, window)

    # Save the image as a PNG
    after = time()
    print(f"\nDone in {after - before:.3f} seconds!", file=sys.stderr)
    img.write(f"{fractalName}.png")
    print(f"Saved image to file {fractalName}.png", file=sys.stderr)

    # Call tkinter.mainloop so the GUI remains open
    print("Close the image window to exit the program", file=sys.stderr)
    mainloop()

def paint(fractalSettup, imagename, window):
    """Paint a Fractal image into the TKinter PhotoImage canvas.
    This code creates an image which is 640x640 pixels in size."""

    global img
    print(fractalSettup)
    fractal = fractalSettup

    # Figure out how the boundaries of the PhotoImage relate to coordinates on
    # the imaginary plane.
    minx = fractal['centerX'] - (fractal['axisLen'] / 2.0)
    maxx = fractal['centerX'] + (fractal['axisLen'] / 2.0)
    miny = fractal['centerY'] - (fractal['axisLen'] / 2.0)
    maxy = fractal['centerY'] + (fractal['axisLen'] / 2.0)

    # Display the image on the screen
    canvas = Canvas(window, width=IMAGE_SIZE, height=IMAGE_SIZE, bg='#000000')
    canvas.pack()
    canvas.create_image((256, 256), image=img, state="normal")

    # At this scale, how much length and height on the imaginary plane does one
    # pixel take?
    pixelsize = abs(maxx - minx) / 512

    portion = 0
    total_pixels = 512 * 512  # 262144
    # loop
    for row in range(512, 0, -1):
        cc = []
        for col in range(512):
            x = minx + col * pixelsize
            y = miny + row * pixelsize
            # "Leaf" is the only well-behaved fractal - all of the others crash
            #
            # if imagename in [ 'leaf', ]:
            #     idx = Mandelbrot.PixelColor(complex(x, y), palette)
            #     color = palette[idx]
            # The rest of the fractals
            # else:
            iteration = Mandelbrot.PixelColor(complex(x, y))
            color = Palette.MbrotPalette[iteration]
            cc.append(color)
            y = miny + row * pixelsize # prepare for next loop
            x = minx + col * pixelsize # prepare for next loop

        img.put('{' + ' '.join(cc) + '}', to=(0, 512-row))
        window.update()  # display a row of pixels

        print(pixelsWrittenSoFar(row), end='\r', file=sys.stderr)  # the '\r' returns the cursor to the leftmost column

def pixelsWrittenSoFar(rows):
    portion = (512 - rows) / 512
    status_percent = '{:>4.0%}'.format(portion)
    status_bar_width = 34
    status_bar = '=' * int(status_bar_width * portion)
    status_bar = '{:<33}'.format(status_bar)
    return ''.join(list(['[', status_percent, ' ', status_bar, ']']))