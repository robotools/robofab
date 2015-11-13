# showing where the data lives in the RoboFab objects.
from robofab.world import CurrentFont

f = CurrentFont()

# these are pairs
print f.kerning.keys()

# get the value for this pair
print f.kerning[('MMK_L_baseserif', 'n')]