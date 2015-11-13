# see if "A" and "B" can interpolate
# and find out what's wrong if you can
from robofab.world import CurrentFont
f = CurrentFont()
a = f["a"]
print a.isCompatible(f["b"], True)
