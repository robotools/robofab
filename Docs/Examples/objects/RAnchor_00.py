# robofab manual
# Anchor object
# usage examples 

f = CurrentFont()

for g in f:
    if len(g.anchors) > 0:
        print g, g.anchors
