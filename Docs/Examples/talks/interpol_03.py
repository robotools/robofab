# see if "A" and "B" can interpolate
from robofab.world import CurrentFont
f = CurrentFont()
a = f["a"]
print a.isCompatible(f["b"], False)
