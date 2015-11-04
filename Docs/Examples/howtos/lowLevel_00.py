from robofab.world import CurrentFont
f = CurrentFont()
# this is the high level RoboFab object
print f
# this is the low level FontLab object, not a part of RoboFab
print f.naked()
