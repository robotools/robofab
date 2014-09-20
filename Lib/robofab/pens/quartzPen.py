from fontTools.pens.basePen import BasePen

class QuartzPen(BasePen):

	"""Pen to draw onto a Quartz drawing context (Carbon.CG)."""

	def __init__(self, glyphSet, quartzContext):
		BasePen.__init__(self, glyphSet)
		self._context = quartzContext

	def _moveTo(self, xxx_todo_changeme):
		(x, y) = xxx_todo_changeme
		self._context.CGContextMoveToPoint(x, y)

	def _lineTo(self, xxx_todo_changeme1):
		(x, y) = xxx_todo_changeme1
		self._context.CGContextAddLineToPoint(x, y)

	def _curveToOne(self, xxx_todo_changeme2, xxx_todo_changeme3, xxx_todo_changeme4):
		(x1, y1) = xxx_todo_changeme2
		(x2, y2) = xxx_todo_changeme3
		(x3, y3) = xxx_todo_changeme4
		self._context.CGContextAddCurveToPoint(x1, y1, x2, y2, x3, y3)

	def _closePath(self):
		self._context.closePath()
