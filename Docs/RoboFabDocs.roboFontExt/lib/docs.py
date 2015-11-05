# open a help window with RoboFab docs

import os
from mojo.UI import HelpWindow

dirLib   = os.path.dirname(__file__)
dirBuild = os.path.join(dirLib, "_build")
dirHtml  = os.path.join(dirBuild, "html")
htmlPath = os.path.join(dirHtml, "index.html")
print 'hello world'

if os.path.exists(htmlPath):
    HelpWindow(htmlPath,
        title="RoboFab Docs",
        developer="RoboFab Developers",
        developerURL="http://robofab.org/"
    )
