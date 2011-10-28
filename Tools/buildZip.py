"""

	Attempt at a build script for an installer

	1. copy stuff from the svn dirs to  here
	2. get the version number
	3. tell the installer to build
	
	
	
"""

from distroBuilder import *

if __name__ == "__main__":
	rev = updateRobofab()
	distroRoot = os.path.join(os.getcwd(), "build", "Zip installer")
	copyStuffToBuildFolder(rev, distroRoot, makeZipName="RoboFab%s_plusDependencies.zip")
