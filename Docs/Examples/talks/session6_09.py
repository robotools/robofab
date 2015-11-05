# show the objects from the fontlab layer

from robofab.world import CurrentFont

f = CurrentFont()
print f.naked()

g =  f["A"]
print g.naked()
