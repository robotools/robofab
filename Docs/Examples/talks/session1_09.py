# iteration through alphabetically sorted glyphnames

from robofab.world import CurrentFont

font = CurrentFont()
print "font has %d glyphs" % len(font)

# names is now a list of strings, the names of the glyphs
# not the glyphs themselves!
names = font.keys()

# the list of names is sorted
names.sort()

# now we iterate through the list of names
for glyphName in names:
    # now we ask for the glyph with glyphName
    print font[glyphName]
