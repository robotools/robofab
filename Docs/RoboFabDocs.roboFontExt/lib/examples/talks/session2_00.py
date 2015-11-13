# robothon 2009
# set basic attributes in a glyph
 
from robofab.world import CurrentFont
 
font = CurrentFont()
glyph = font['A']

print glyph.name
print glyph.width
print glyph.leftMargin
print glyph.rightMargin
print glyph.box
print glyph.unicode

glyph.update()