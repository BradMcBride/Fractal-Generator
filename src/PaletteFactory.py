import sys
from GradientPalette import GradientPalette

defaultIter = {'iterations': 100}
def make_colorPallete(palette="gradient", dict=defaultIter):
    if palette == "gradient":
        pal = GradientPalette(iteration=dict['iterations'])
    elif palette == "TBD":
        pal = GradientPalette(iteration=dict['iterations'])
    else:
        sys.exit(1)
    return pal