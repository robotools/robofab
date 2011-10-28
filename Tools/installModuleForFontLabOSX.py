#!/usr/bin/python

"""
    
    Installer for RoboFab for FontLabs on OSX
    
    Operation:
        1.  This script builds a .flw with the right paths hardwired.
        2.  Then calls all of the FontLab applications it can find to run the .flw script.
            This ensures the paths are written to exactly the right Pythons. 
        3.  The .flw finds out which site-packages can be used to install in.
        4.  Then it places a *.pth file pointing to the current location of the
                robofab/trunk/Lib folder
            This means the setup is a bit more fragile, for instance if you
            move or rename the folder that contains robofab. But it also makes
            it possible for multiple fontlabs to point to a single install of robofab. 
        5.  Logs are kept.
        6.  SAVE YOUR WORK IN RUNNING FONTLAB APPLICATIONS BEFORE RUNNING.
            This script will instruct FontLab to quit at the end of the installation.
            Unsaved work will be lost.
            
    Usage:
        cd <folder where this file is>
        sudo python installModuleForFontLabOSX.py
            
    
    Notes
        In its current form OSX might have permission restrictions for writing in site-packages.
        This does not download or install dependencies such as FontTools.

    This script assumes is here:
        robofab/
            trunk/
                Tools/
                    installModuleForMacFontLab.py
                # and the robofab package is here:
                Lib/
                    robofab/
                        __init__.py
                        #etc
                        
    Future functionality could include:
        - FontLab windows version
        - sniff for other useful modules, link those too
        - run this script as part of a .pkg
        
    
"""

import os
import platform
from time import localtime, strftime, sleep

longTimeStamp = strftime("%a, %d %b %Y %H:%M:%S", localtime())
shortTimeStamp = strftime("%d_%b_%Y_%H_%M_%S", localtime())
scriptVersion = "1.0"

import tempfile
from AppKit import *


installerCode = """# This is a automatically generated installer script for FontLab
# Generated on %(timeStamp)s
# scriptVersion: %(scriptVersion)s

import sys, os, time, platform

def log(entry, verbose=True):
    \"\"\"Write stuff into log files\"\"\"
    path = "%(appLogPath)s"
    try:
        f = open(path, 'a')
    except IOError:
        print "Error writing to log."
        print entry
        return
    if type(entry) != str:
        entry = str(entry)
    f.write("\\n"+entry)
    f.close()
    if verbose:
        print entry

def findSitePackages():
    \"\"\"Try to find the site-packages folder for the current python.\"\"\"
    folderName = "site-packages"
    paths = {}
    for s in sys.path:
        if s.find(folderName)!=-1:
            root = os.path.join(s.split(folderName)[0], folderName)
            paths[root] = True
    safe = []
    return paths.keys()

def writePathFile(pathFilePath, modulePaths):
    \"\"\"Write the *.pth file to site-packages.\"\"\"
    print "writing the modulePaths path to", pathFilePath
    try:
        f = open(pathFilePath, 'w')
        f.write(\"\\n\".join(modulePaths))
        f.close()
    except IOError:
        import traceback
        cla, exc, trbk = sys.exc_info()
        excName = cla.__name__
        try:
         excArgs = exc.__dict__["args"]
        except KeyError:
         excArgs = "<no args>"
        excTb = traceback.format_tb(trbk, 2)
        log(excName)
        #log(excArgs)
        log(excTb)

def makePTHFileName():
    name = "%(moduleName)s_for_%(safeAppName)s" + ".pth"
    return name

log("-" * 50)
log("hello, this is application: %(appName)s")
log("Running script version: %(scriptVersion)s")
log("Platform:"+platform.platform())
print "I will log to", "%(appLogPath)s"
from FL import *
log("FontLab version "+fl.version)
log("I have a path for the new module %(modulePaths)s")

installedAlready = False
try:
    import robofab
    log("Hey, I can already load robofab, I'm going to stop. ")
    log("robofab.__file__ :" + robofab.__file__.encode('ascii'))
    log("Stopped installing.")
    installedAlready = True
except ImportError:
    log("I can't load robofab, good thing we're installing it.")
    
sp = findSitePackages()
print "And my sitepackages is here", sp
if len(sp)==1:
    # we're probably good
    log("we have found one site-packages at " + sp[0])
    pathFilePath = os.path.join(sp[0], makePTHFileName())
    log("pathFilePath: " + pathFilePath)
    if os.path.exists(pathFilePath)==True:
        log("\tAlready .pth at this location!")
    else:
        if installedAlready:
            log("\tSo we've already been installed some other way?")
    if not installedAlready:
        writePathFile(pathFilePath, %(modulePaths)s)
        # if there's nothing else we can quit.
        log("Finished installing. Quitting.")
    else:
        log("Skipping the actual install. Quitting.")
    sys.exit(0)
else:
    # trouble - print detailed debug info
    # leave the app open. 
    log("we have trouble finding site-packages. Please check your installation.")
    for s in sp:
        log(s)
    log("Stopped installing.")
    # leave the app open after problem?

"""

verbose = True

def writeFLW(path, code):
    f = open(path, 'wb')
    f.write(code)
    f.close()

def findFontLabCandidates():
    """ This tries to catch all applications that can open a .vfb file.
        That should include a good number of FontLab applications.
        In order to find out, we need LaunchServices. Should LaunchServices
        itself not be available, return the 2 most common FontLab.app names
        and hope for the best.
        
    """
    try:
        from LaunchServices import LSCopyApplicationURLsForURL, kLSRolesEditor
        canLaunch = True
        log(logMainPath, "LaunchServices available.")
    except ImportError:
        canLaunch = False
        log(logMainPath, "LaunchServices unavailable.")
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
           fontLabs.append(name)
    # remove the bogus VFB
    os.remove(dummyPath)
    return fontLabs

def log(path, entry, verbose=True):
    """Write stuff into log files"""
    try:
        f = open(path, 'a')
    except IOError:
        print "Error writing to log."
        print entry
        return
    if type(entry) != str:
        entry = str(entry)
    f.write("\n"+entry)
    f.close()
    if verbose:
        print entry


# build the installer program for FontLab
root = os.path.abspath(os.path.dirname(__file__))


# folder for logs
logRootPath = os.path.join(root, "installation logs")
if not os.path.exists(logRootPath):
    os.makedirs(logRootPath)
# path for log for this script
logMainPath = os.path.join(logRootPath, "installer_log_%s.txt"%shortTimeStamp)
    
log(logMainPath, "Start install")
log(logMainPath, longTimeStamp)
log(logMainPath, "Running script version: %s"%scriptVersion)
log(logMainPath, "Platform: "+platform.platform())
log(logMainPath, "root: "+root)


modulePaths = []
modulePaths.append(os.path.join(os.path.dirname(root), "Lib"))
moduleName = "RoboFab"

# find as many FontLab.app names as wel can
fontLabNames = findFontLabCandidates()

for appName in fontLabNames:
    problem = None
    try:
        print
        log(logMainPath, "------")
        appBootTimeStamp = strftime("%a, %d %b %Y %H:%M:%S", localtime())
        log(logMainPath, appBootTimeStamp)
        
        log(logMainPath, "calling application: "+appName)
        safeAppName = os.path.splitext(appName)[0].replace(" ", "").encode("ascii")
        log(logMainPath, "safe AppName: "+safeAppName)
        flInstallerPath = os.path.join(root, "temp_FontLab_TestInstaller_for_%s.flw"%safeAppName)
        appLogPath = os.path.join(logRootPath, "%s_log_%s.txt"%(safeAppName, shortTimeStamp))
        log(logMainPath, "applications will log to: "+appLogPath)
        log(logMainPath, "modulePaths: "+str(modulePaths))
        log(logMainPath, "script: "+flInstallerPath)
    
        # prepare the program
        values = {'appName':appName, 'modulePaths':modulePaths,
            'moduleName':moduleName,
            'timeStamp': longTimeStamp,
            'appLogPath': appLogPath,
            'safeAppName': safeAppName,
            'scriptVersion': scriptVersion,
            }
        code = installerCode%values
        writeFLW(flInstallerPath, code)
        # run the program
        ws = NSWorkspace.sharedWorkspace().openFile_withApplication_(flInstallerPath, appName)
    except:
        problem = True
    finally:
        if problem:
            log(logMainPath, "Looks like we had a problem.")
            
# cleanup
if not verbose:
    os.remove(flInstallerPath)

log(logMainPath, "done install")
# done.