"""

    These are some tools that can help installing FontLab
    in various places. It started out as a single script
    but that turned out to be not vary practical. 
    So here they are.
    

"""


import tempfile
import shutil
import os, time
from time import strftime, localtime

scriptVersion = "1.1"
# 

class FontLabInstaller(object):

    installerFunctionsFileName = "installerFunctions.py"
    installerScriptFileName = "installerScript.py"
    maxWaitTime = 20

    def __init__(self, root, moduleData):
        self.longTimeStamp = strftime("%a, %d %b %Y %H:%M:%S", localtime())
        self.shortTimeStamp = strftime("%d_%b_%Y_%H_%M_%S", localtime())
        self.root = os.path.join(root, "fontLabInstallerData")
        self.moduleData = moduleData
        self.appCandidates = []
        self.appScripts = []            # list of paths and application names
        self.expectedResults = []      # list of paths we could see with results
        self.foundResults = {}          # list of stuff we found
        self.startWaitTime = None
        if os.path.exists(self.root):
            # clear old results before running
            shutil.rmtree(self.root)
        # make a folder for all our files
        os.makedirs(self.root)
        # place for the logs
        self.logFolder = os.path.join(self.root,"logs")
        os.makedirs(self.logFolder)
        self.logPath = os.path.join(self.logFolder, 'mainLog.txt')
        # place for the fontlab scripts
        self.scriptsFolder = os.path.join(self.root, "scripts")
        os.makedirs(self.scriptsFolder)
        # place for results
        self.resultsFolder = os.path.join(self.root, "results")
        os.makedirs(self.resultsFolder)
            

    def findFontLabCandidatesOSX(self):
        """ This tries to catch all applications that can open a .vfb file.
            That should include a good number of FontLab applications.
            In order to find out, we need LaunchServices. Should LaunchServices
            itself not be available, return the 2 most common FontLab.app names
            and hope for the best.
        
        """
        from AppKit import NSURL
        self.log("findFontLabCandidatesOSX start")
        try:
            from LaunchServices import LSCopyApplicationURLsForURL, kLSRolesEditor
            canLaunch = True
            self.log("LaunchServices available.")
        except ImportError:
            canLaunch = False
            self.log("LaunchServices unavailable.")
            
        if not canLaunch:
            return ["FontLab Studio 5 OSX.app", "FontLab Studio.app"]
        # make a bogus VFB
        dummyPath = tempfile.mkstemp(suffix=".vfb")[1]
        # find VFB editors
        url  = NSURL.fileURLWithPath_(dummyPath)
        fontLabs = []
        for url in LSCopyApplicationURLsForURL(url, kLSRolesEditor):
           path = url.path()
           name = os.path.basename(path)
           if name not in fontLabs:
               self.log("Candidate: %s at %s"%(name, path))
               fontLabs.append(name)
        # remove the bogus VFB
        os.remove(dummyPath)
        self.log("findFontLabCandidatesOSX end")
        self.appCandidates = fontLabs
        return fontLabs

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
    
    def runInspectorScripts(self, run=True):
        """Build the inspector scripts for each FontLab we found. Then use NSWorkspace to run each script with each app."""
        for appName in self.findFontLabCandidatesOSX():
            self._buildInspectorScript(appName)
        if run:
            self.expectedResults = []
            from AppKit import NSWorkspace
            for flInstallerPath, resultsPath, appName in self.appScripts:
                try:
                    ws = NSWorkspace.sharedWorkspace().openFile_withApplication_(flInstallerPath, appName)
                    self.expectedResults.append(resultsPath)
                except:
                    # something went wrong
                    self.log("Failed to open %s"%appName)
            print("expectingResults", self.expectedResults)
        if self.expectedResults:
            self.log("We're expecting results. Starting polling.")
            self.poll()
    
    def poll(self):
        """Now that the inspector scripts have been deployed, see if we can find results
        at the expected place. Keep track of the start time and do a polite time out
        if nothing happens.
        """
        if self.startWaitTime is None:
            # first time we're called
            self.startWaitTime = time.time()
        newResults = []
        self.log("tick")
        for path in self.expectedResults:
            if os.path.exists(path):
                # hey! found one!
                newResults.append(path)
        for new in newResults:
            self.log("I have a result for"+new)
            self.expectedResults.remove(new)
            f = open(new, 'r')
            self.foundResults[new] = f.read()
            f.close()
        
        if len(self.expectedResults) == 0:
            self.finish()
            return

        if (time.time()-self.startWaitTime) > self.maxWaitTime:
            # time out, one or more results did not come through.
            print("time out while waiting for", self.expectedResults)
            self.finish()
            return

        time.sleep(1)
        print("tick")
        self.poll()
            
    def finish(self):
        self.log("finish!")
        for k, v in list(self.foundResults.items()):
            print(k, v)
        
    def _buildInspectorScript(self, appName):
        problem = None
        f = open(self.installerFunctionsFileName, 'r')
        installerCode = f.read()
        f.close()
        f = open(self.installerScriptFileName, 'r')
        installerScript = f.read()
        f.close()

        self.log("------")
        appBootTimeStamp = strftime("%a, %d %b %Y %H:%M:%S", localtime())
        self.log(appBootTimeStamp)
    
        self.log("calling application: "+appName)
        safeAppName = os.path.splitext(appName)[0].replace(" ", "").encode("ascii")
        self.log("safe AppName: "+safeAppName)
        flInstallerPath = os.path.join(self.scriptsFolder, "fontLabInspector_for_%s.flw"%safeAppName)
        resultsPath = os.path.join(self.resultsFolder, "fontLabInspectorResults_for_%s.txt"%safeAppName)
        appLogPath = os.path.join(self.logFolder, "%s_log_%s.txt"%(safeAppName, self.shortTimeStamp))
        self.log("applications will log to: "+appLogPath)
        self.log("script: "+flInstallerPath)

        # prepare the program
        values = {
            'appName':appName,
            #'modulePaths':modulePaths,
            #'moduleName':moduleName,
            'timeStamp': self.longTimeStamp,
            'appLogPath': appLogPath,
            'safeAppName': safeAppName,
            'scriptVersion': scriptVersion,
            'resultsPath': resultsPath,
            'moduleData': str(self.moduleData),
            }
    
        code = installerCode + installerScript%values
        print("writing script at", flInstallerPath)
        f = open(flInstallerPath, 'wb')
        f.write(code)
        f.close()
        self.appScripts.append((flInstallerPath, resultsPath, appName))


        
if __name__ == "__main__":
    
    # data about the modules we would like to install
    # we want to find out: available or not, which version and where.
    pathModule1 = os.path.join(os.getcwd(), "testData", "dummyModules", "testModule1", "Lib")
    pathModule2 = os.path.join(os.getcwd(), "testData", "dummyModules", "testModule2", "Lib")

    moduleData = {
        "testModule1":      {'path':pathModule1, 'installType': "make_path"},
        "testModule2":      {'path':pathModule2, 'installType': "make_path"},
        "robofab":          {'path':"somewhere", 'installType': "make_path"},
    }

    import os
    root = os.getcwd()
    fli = FontLabInstaller(root, moduleData)
    fli.log('This is a test, it will try to load testModule1 and testModule2.')
    fli.runInspectorScripts()
