# use a point pen

from robofab.world import CurrentFont
from robofab.pens.pointPen import PrintingPointPen

font = CurrentFont()
glyph = font['A']

pen = PrintingPointPen()
glyph.drawPoints(pen)
