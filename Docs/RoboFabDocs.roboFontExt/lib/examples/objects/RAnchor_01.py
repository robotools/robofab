# robofab manual
# Anchor object
# attribute examples

g = CurrentGlyph()

if len(g.anchors) > 0:
    for a in g.anchors:
        print a.position