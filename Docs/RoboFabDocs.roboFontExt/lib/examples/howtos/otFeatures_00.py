# Getting to feature data in a UFO.

from robofab.world import OpenFont

path = "A/path/to/font.ufo"

f = OpenFont(path)

print f.lib.keys()
print f.lib["com.robofab.features"]
print f.lib["com.robofab.features"]['liga']
print f.lib["com.robofab.featureorder"]
