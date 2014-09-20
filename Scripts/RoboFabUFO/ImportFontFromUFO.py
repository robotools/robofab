#FLM: Import .ufo File into FontLab

from robofab.world import NewFont
from robofab.interface.all.dialogs import GetFileOrFolder

path = GetFileOrFolder("Please select a .ufo")
if path is not None:
	font = NewFont()
	font.readUFO(path, doProgress=True)
	font.update()
	print('DONE!')
