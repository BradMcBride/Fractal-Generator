import sys
from GradientPalette import GradientPalette
from RandomPalette import RandomPalette
from IntergalacticPalette import IntergalacticPalette

defaultIter = {'iterations': 100}
def make_colorPallete(palette="gradient", dict=defaultIter):
    if palette == "gradient":
        pal = GradientPalette(iteration=dict['iterations'])
    elif palette == "random":
        pal = RandomPalette(iteration=dict['iterations'])
    elif palette == "intergalactic":
        pal = IntergalacticPalette(iteration=dict['iterations'])
    else:
        sys.exit(1)
    return pal