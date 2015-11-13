from robofab.world import CurrentGlyph
from robofab.pens.filterPen import spikeGlyph
segmentLength = 20
spikeLength = 100
spikeGlyph(CurrentGlyph(), segmentLength, spikeLength)
