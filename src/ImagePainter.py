from tkinter import Tk, Canvas, PhotoImage, mainloop
from time import time
import sys
import Mandelbrot, Palette

IMAGE_SIZE = 512
def mbrot_main(fractalSettup, fractalName):
    global img
    print("Rendering {} fractal".format(fractalName), file=sys.stderr)
    before = time()
    window = Tk()
    img = PhotoImage(width=IMAGE_SIZE, height=IMAGE_SIZE)
    paint(fractalSettup, img, window)

    after = time()
    print(f"\nDone in {after - before:.3f} seconds!", file=sys.stderr)
    img.write(f"{fractalName}.png")
    print(f"Saved image to file {fractalName}.png", file=sys.stderr)
    print("Close the image window to exit the program", file=sys.stderr)
    mainloop()

def paint(fractalSettup, img, window):
    minx = fractalSettup['centerX'] - (fractalSettup['axisLen'] / 2.0)
    maxx = fractalSettup['centerX'] + (fractalSettup['axisLen'] / 2.0)
    miny = fractalSettup['centerY'] - (fractalSettup['axisLen'] / 2.0)
    maxy = fractalSettup['centerY'] + (fractalSettup['axisLen'] / 2.0)

    canvas = Canvas(window, width=IMAGE_SIZE, height=IMAGE_SIZE, bg='#000000')
    canvas.pack()
    canvas.create_image((IMAGE_SIZE/2, IMAGE_SIZE/2), image=img, state="normal")

    pixelsize = abs(maxx - minx) / IMAGE_SIZE

    for row in range(IMAGE_SIZE, 0, -1):
        cc = []
        for col in range(IMAGE_SIZE):
            x = minx + col * pixelsize
            y = miny + row * pixelsize
            iteration = Mandelbrot.PixelColor(complex(x, y), len(Palette.MbrotPalette))
            color = Palette.MbrotPalette[iteration]
            cc.append(color)

        img.put('{' + ' '.join(cc) + '}', to=(0, IMAGE_SIZE-row))
        window.update()

        print(pixelsWrittenSoFar(row), end='\r', file=sys.stderr)  # the '\r' returns the cursor to the leftmost column

def pixelsWrittenSoFar(rows):
    status_bar_width = 34
    portion = (IMAGE_SIZE - rows) / IMAGE_SIZE
    status_percent = '{:>4.0%}'.format(portion)
    status_bar = '=' * int(status_bar_width * portion)
    status_bar = '{:<33}'.format(status_bar)
    return ''.join(list(['[', status_percent, ' ', status_bar, ']']))