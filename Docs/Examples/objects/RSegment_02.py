# robofab manual
# Segment object
# method examples

f = OpenFont()

for g in f:
    for contour in g:
        for segment in contour:
            segment.move((50, 25))
