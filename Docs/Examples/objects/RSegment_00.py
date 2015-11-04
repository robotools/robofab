# robofab manual
# Segment object
# usage examples

f = OpenFont()

for g in f:
    for contour in g:
        for segment in contour:
            print segment
