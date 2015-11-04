import os
from mojo.UI import HelpWindow

lib_path = os.path.dirname(__file__)
extension_html = os.path.join(os.path.dirname(lib_path), "Docs/build/html/index.html")
print extension_html, os.path.exists
# HelpWindow(extension_html, title="RoboFab Docs", developer=None, developerURL=None)
