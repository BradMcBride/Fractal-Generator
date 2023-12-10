from tkinter import Tk, Canvas, PhotoImage, mainloop
from time import time
import sys

def main(fractal, palette, fracInfo):
    print("Rendering {} fractal".format(fracInfo['type']), file=sys.stderr)
    before = time()
    window = Tk()
    img = PhotoImage(width=fracInfo['pixels'], height=fracInfo['pixels'])
    paint(fracInfo, img, window, palette, fractal)

    after = time()
    print(f"\nDone in {after - before:.3f} seconds!", file=sys.stderr)
    img.write(f"{fracInfo['type']}.png")
    print(f"Saved image to file {fracInfo['type']}.png", file=sys.stderr)
    print("Close the image window to exit the program", file=sys.stderr)
    mainloop()

def paint(fracInfo, img, window, palette, fractal):
    canvas = Canvas(window, width=fracInfo['pixels'] - 2, height=fracInfo['pixels'] - 2, bg='#000000')
    canvas.pack()
    canvas.create_image((fracInfo['pixels']/2, fracInfo['pixels']/2), image=img, state="normal")

    for row in range(fracInfo['pixels'], 0, -1):
        cc = []
        for col in range(fracInfo['pixels']):
            x = fracInfo['min']['x'] + col * (abs(fracInfo['max']['x'] - fracInfo['min']['x']) / fracInfo['pixels'])
            y = fracInfo['min']['y'] + row * (abs(fracInfo['max']['x'] - fracInfo['min']['x']) / fracInfo['pixels'])
            number = fractal.count(complex(x, y), fracInfo['iterations'])
            color = palette.getColor(number)
            cc.append(color)
        img.put('{' + ' '.join(cc) + '}', to=(0, fracInfo['pixels'] - row))
        window.update()

        print(pixelsWrittenSoFar(row, fracInfo), end='\r', file=sys.stderr)  # the '\r' returns the cursor to the leftmost column

def pixelsWrittenSoFar(rows, fracInfo):
    status_bar_width = 34
    portion = (fracInfo['pixels'] - rows) / fracInfo['pixels']
    status_percent = '{:>4.0%}'.format(portion)
    status_bar = '=' * int(status_bar_width * portion)
    status_bar = '{:<33}'.format(status_bar)
    return ''.join(list(['[', status_percent, ' ', status_bar, ']']))