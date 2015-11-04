# [h] build RoboFont Extension

import os
from mojo.extensions import ExtensionBundle

lib_path = os.path.dirname(__file__)
extension_file = 'RoboFabDocs.roboFontExt'
extension_path = os.path.join(lib_path, extension_file)
extension_html = os.path.join(os.path.dirname(lib_path), "Docs/build/html/")

print 'building extension...',

B = ExtensionBundle()
B.name = "RoboFabDocs"
B.developer = 'RoboFab Developers'
B.developerURL = 'http://robofab.org/'
B.version = "0.1"
B.mainScript = ""
B.launchAtStartUp = 0
B.addToMenu = [{'path' : 'docs.py', 'preferredName' : 'RoboFab Docs', 'shortKey' : ''}]
B.requiresVersionMajor = '1'
B.requiresVersionMinor = '5'
B.infoDictionary["html"] = 0
B.save(extension_path, libPath=lib_path, resourcesPath=None, pycOnly=False)

print 'done.'
