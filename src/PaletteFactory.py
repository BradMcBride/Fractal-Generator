import sys
from GradientPalette import GradientPalette

def make_colorPallete(palette="gradient", iteration=100):
    if palette == "gradient":
        pal = GradientPalette(iteration=int(iteration))
    elif palette == "TBD":
        pal = GradientPalette(iteration=int(iteration))
    else:
        sys.exit(1)
    return pal