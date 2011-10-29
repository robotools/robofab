"""

	Attempt at a build script for an installer

	1. copy stuff from the svn dirs to  here
	2. get the version number
	3. tell the installer to build
	
	
	
"""

import os
from robofabDistroPaths import *

# copy the stuff from the svn dirs

def updateFontTools():
	pwd = os.getcwd()
	os.chdir(fontToolsPath)
	print os.system("svn up")
	d = os.popen("svnversion")
	revision = d.read()
	os.chdir(pwd)
	return revision.strip()

def updateRobofab():
	pwd = os.getcwd()
	os.chdir(roboFabPath)
	print os.system("svn up")
	d = os.popen("svnversion")
	revision = d.read()
	os.chdir(pwd)
	return revision.strip()

def updateDialogKit():
	pwd = os.getcwd()
	os.chdir(roboFabPath)
	print os.system("svn up")
	d = os.popen("svnversion")
	revision = d.read()
	os.chdir(pwd)
	return revision.strip()

def copyStuffToBuildFolder(revision=None, distroRoot=None, only=None, makeZipName=None):
	# robofab
	
	# make the target folder relative to this script
	if distroRoot is None:
		distroRoot = os.getcwd()
	if not os.path.exists(distroRoot):
		os.makedirs(distroRoot)
	
	if only is None:
		only = ['fonttools', 'robofab', 'fonttools', 'dialogkit', 'vanilla']

	if "scripts" in only:
		srcDir = os.path.normpath(roboFabScriptsPath)
		dstDir = os.path.normpath(os.path.join(distroRoot, "Scripts"))
		cmd = 'rm -rf "%s"'%(dstDir)
		os.popen(cmd)
		copyStuff(srcDir, dstDir)
	
	if "robofab" in only:
		srcDir = os.path.normpath(roboFabPath)
		dstDir = os.path.normpath(os.path.join(distroRoot, "RoboFab"))
		cmd = 'rm -rf "%s"'%(dstDir)
		os.popen(cmd)
		copyStuff(srcDir, dstDir)
	
	if "fonttools" in only:
		# fontTools to the robofab distro build
		srcDir = os.path.normpath(fontToolsPath)
		dstDir = os.path.normpath(os.path.join(distroRoot, "FontTools"))
		copyStuff(srcDir, dstDir)

	if "dialogkit" in only:
		# dialogKit to the robofab distro build
		srcDir = os.path.normpath(dialogKitPath)
		dstDir = os.path.normpath(os.path.join(distroRoot, "DialogKit"))
		cmd = 'rm -rf "%s"'%(dstDir)
		os.popen(cmd)
		copyStuff(srcDir, dstDir)

	if "vanilla" in only:
		# vanilla to the robofab distro build
		srcDir = os.path.normpath(vanillaPath)
		dstDir = os.path.normpath(os.path.join(distroRoot, "Vanilla"))
		cmd = 'rm -rf "%s"'%(dstDir)
		os.popen(cmd)
		copyStuff(srcDir, dstDir)

	if revision is not None:
		notePath = os.path.join(roboFabPath, "svnRevision.txt")
		print "notePath", notePath
		f = open(notePath, 'w')
		f.write(revision)
		f.close()

	if makeZipName:
		os.chdir(distroRoot)
		print "0000 distroRoot", distroRoot
		archiveName = makeZipName%revision.strip()
		#cmd = "zip -r %s RoboFab/"%archiveName
		cmd = "zip -r \"%s\" *"%archiveName
		print "--", cmd
		d = os.popen(cmd)
		print d.read()

		cmd = "mv \"%s\" \"../\""%archiveName
		print "--", cmd
		d = os.popen(cmd)
		print d.read()

		cmd = "rm -rf \"%s\""%distroRoot
		print "--", cmd
		d = os.popen(cmd)
		print d.read()


def copyStuff(src, dst):
	print "copyStuff src", src
	print "copyStuff dst", dst
	notCopy = ['.DS_Store', '.svn', ".pyc", "CVS", 'build', "build", "tags", "branches"]
	for n in os.listdir(src):
		if n in notCopy:
			continue
		if os.path.splitext(n)[-1] in notCopy:
			continue
		p = os.path.join(src, n)
		d = os.path.join(dst, n)
		if os.path.isdir(p):
			if not os.path.exists(d):
				os.makedirs(d)
			copyStuff(p, d)
			continue
		cmd = 'cp "%s" "%s"'%(p, os.path.dirname(d))
		print os.popen(cmd)

