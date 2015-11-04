# example of accessing the hint data,
# using the font.psHints object.

from robofab.world import CurrentFont

f = CurrentFont()
print f.psHints.asDict()
