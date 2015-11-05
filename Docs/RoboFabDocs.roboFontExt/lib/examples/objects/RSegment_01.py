# robofab manual
# Segment object
# attribute examples

f = OpenFont()

for g in f:
    for contour in g:
        for segment in contour:
            print len(segment)
            print segment.type
            print segment.smooth
            print segment.points
            print segment.onCurve
            print segment.offCurve
            print segment.selected
