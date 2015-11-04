# bpoints
c = CurrentGlyph()
for aPt in c[0].bPoints:
    print aPt.anchor
    print aPt.bcpIn
    print aPt.bcpOut
    print aPt.type
