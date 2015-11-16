import os
import shutil
import subprocess

baseFolder = os.path.dirname(__file__)
sourceFolder = os.path.join(baseFolder, 'source')
buildFolder = os.path.join(baseFolder, '_build')
logFile = os.path.join(baseFolder, 'sphinx-log.txt')
doctreesFolder = os.path.join(buildFolder, 'doctrees')
htmlFolder = os.path.join(buildFolder, 'html')

# delete build folder
if os.path.exists(buildFolder):
    shutil.rmtree(buildFolder)

# options
# http://sphinx-doc.org/man/sphinx-build.html
# or in Terminal: sphinx-build -h
commands = [
    '/usr/local/bin/sphinx-build',
    '-a', # build all files (not just new and changed)
    '-b', 'html', # builder: html / pdf / epub / text / etc.
    '-Q', # suppress console warnings and errors
    '-d', doctreesFolder,
    '-w', logFile, # write warnings and errors to file
    sourceFolder,
    htmlFolder
]

# build docs
p = subprocess.Popen(commands)
stdout, stderr = p.communicate()

# rewrite html for object map
objectMapHtmlPath = os.path.join(os.path.join(htmlFolder, 'objects'), 'model.html')
objectMapHtmlFile = open(objectMapHtmlPath, 'r')
objectMapHtml = objectMapHtmlFile.read()

findHtml = '<img src="../_images/ObjectModel.svg" />'
replaceHtml = '<object type="image/svg+xml" data="../_images/ObjectModel.svg"></object>'

objectMapHtml = objectMapHtml.replace(findHtml, replaceHtml)
objectMapHtmlFile = open(objectMapHtmlPath, 'w')
objectMapHtmlFile.write(objectMapHtml)
