# example of accessing the postscript blues
# data using the font.info attributes.

from robofab.world import CurrentFont

f = CurrentFont()

print f.info.postscriptBlueValues
print f.info.postscriptOtherBlues
print f.info.postscriptFamilyBlues
print f.info.postscriptFamilyOtherBlues
