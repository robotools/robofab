#FLM: Export Selected or Current Glyph to UFO


"""
	Dump the selected glyph to a .glif as part of a UFO.
	It saves the .glif through a GlyphSet and updates the contents.plist.
	
	Updated for UFO2
"""


from robofab.glifLib import GlyphSet
from robofab.world import CurrentFont, CurrentGlyph
from robofab.interface.all.dialogs import Message
import os


f = CurrentFont()
g = CurrentGlyph()

ufoPath = f.path.replace(".vfb", ".ufo")
if not os.path.exists(ufoPath):
	Message("No UFO found for this font. I'm looking for \"%s\"."%(os.path.basename(ufoPath) ))

if g is not None:
	todo = [g.name]
else:
	todo = f.selection
	
if todo:
	Message("Exporting %s to \"%s\"."%(", ".join(todo), os.path.basename(ufoPath) ))
	f.writeUFO(doHints=False, doInfo=False, doKerning=False,
		doGroups=False, doLib=False, doFeatures=False, glyphs=todo)
		
else:
	Message("No glyphs selected for export.")
	
print 'done'