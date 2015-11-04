# Getting to feature data in a FontLab 
from robofab.world import CurrentFont

f = CurrentFont()

print f.naked().features

# these are raw FontLab feature objects.