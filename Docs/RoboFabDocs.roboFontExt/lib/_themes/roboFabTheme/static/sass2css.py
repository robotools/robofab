# compile sass into css

import os
import subprocess

# sass (CSS extension language) compiler
# http://sass-lang.com/install

def compileSass(sassPath):
    """Compile a sass file (and dependencies) into a single css file."""
    cssPath = os.path.splitext(sassPath)[0] + ".css"
    subprocess.call(["sass", sassPath, cssPath])

baseFolder = os.path.dirname(__file__)

for file_ in os.listdir(baseFolder):
    name, extension = os.path.splitext(file_)
    cssFile = "%s.%s" % (name, extension)
    cssPath = os.path.join(baseFolder, cssFile)
    if extension == ".sass":
        sassPath = os.path.join(baseFolder, file_)
        compileSass(sassPath)
