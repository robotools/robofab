import os


import tempfile
import shutil
import os, time
from time import strftime, localtime


class PathDropper(object):

    loadSortPrefix = "zz"
    
    def __init__(self, installerName, root, moduleData, targetPaths):
        self.installerName = installerName
        self.targetPaths = targetPaths
        self.moduleData = moduleData

        self.root = os.path.join(root, "fontLabInstallerData")

        if os.path.exists(self.root):
            # clear old results before running
            shutil.rmtree(self.root)
        # make a folder for all our files
        os.makedirs(self.root)
        # place for the logs
        self.logFolder = os.path.join(self.root,"logs")
        os.makedirs(self.logFolder)
        self.logPath = os.path.join(self.logFolder, 'mainLog.txt')
        self.log("Installing these modules:")
        for name in list(self.moduleData.keys()):
            self.log("\t"+name)
    
    def scan(self):
        for p in self.targetPaths:
            if os.path.exists(p):
                if os.access(p, os.W_OK):
                    self.log("\tWritable: "+p)
                    self.revealFolder(p)
                    self.writePaths(p)
            else:
                self.log("\tNot found:"+p)
    
    def revealFolder(self, path):
        import subprocess
        subprocess.call(["open", "-R", path])
        
    def writePaths(self, sitePackagesPath):
        """Actually write the damn thing."""
        self.log("Write in"+ sitePackagesPath)
        for name, data in list(self.moduleData.items()):
            print(name, data)
            if data['installType'] == "make_path":
                # make a link to the code folder
                self.log("\t%s wants to be linked to"%name)
                fileName = "%s_link_to_%s_for_%s.pth"%(self.loadSortPrefix, name, self.installerName)
                filePath = os.path.join(sitePackagesPath, fileName)
                if os.path.exists(filePath):
                    self.log("This file is already present.")
                f = open(filePath, 'w')
                f.write(data['path'])
                f.close()
                print(filePath)
                print(fileName)
            else:
                # try to run the setup.py of the package
                self.log("\t%s wants to be installed."%name)
                
    def log(self, entry, verbose=True):
        """Write stuff into log files"""
        try:
            f = open(self.logPath, 'a')
        except IOError:
            print("Error writing to log.")
            print(entry)
            return
        from time import localtime, strftime
        t = strftime("%a, %d %b %Y %H:%M:%S", localtime())
        if type(entry) != str:
            entry = str(entry)
        f.write("\n%s %s"%(t,entry))
        f.close()
        if verbose:
            print(entry)

        

if __name__ == "__main__":

    targetPaths = [
    	#5.0.4.0
    	"C:\Python24\lib\site-packages",

    	#5.0.4.0
    	"C:\Programme\Python24\lib\site-packages",

    	#5.0.4/Mac(Build 2741),
    	#5.0.2/Mac(Build 2298),
    	"/System/Library/Frameworks/Python.framework/Versions/2.3/lib/python2.3/site-packages",

    	#5.1/Mac(Build 4311),
    	#5.1/Mac(Build 4309),
    	"/Library/Python/2.7/site-packages",

    	#5.1/Mac(Build 4311),
    	#5.1/Mac(Build 4309),
    	"/Library/Python/2.6/site-packages",

    	#5.1/Mac(Build 4311),
    	#5.1/Mac(Build 4269),
    	"/Library/Python/2.5/site-packages",

    ]

    # data about the modules we would like to install
    # we want to find out: available or not, which version and where.
    pathModule1 = os.path.join(os.getcwd(), "testData", "dummyModules", "testModule1", "Lib")
    pathModule2 = os.path.join(os.getcwd(), "testData", "dummyModules", "testModule2", "Lib")

    moduleData = {
        "testModule1":      {'path':pathModule1, 'installType': "make_path"},
        "testModule2":      {'path':pathModule2, 'installType': "make_path"},
    }

    installName = "FontLabInstallerTest"

    root = os.getcwd()
    fli = PathDropper(installName, root, moduleData, targetPaths)
    fli.log('This is a test, it will try to load testModule1 and testModule2.')
    fli.scan()
        