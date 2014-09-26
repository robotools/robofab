""" These are the functions we want to use in FontLab."""

import sys, os, time, platform

def log(path, entry, verbose=True):
    """Write stuff into log files"""
    try:
        f = open(path, 'a')
    except IOError:
        print("Error writing to log.")
        print(entry)
        return
    from time import localtime, strftime
    t = strftime("%a, %d %b %Y %H:%M:%S", localtime())
    if type(entry) != str:
        entry = str(entry)
    f.write("\n"+t+" "+entry)
    f.close()
    if verbose:
        print(entry)

def findSitePackages():
    """Try to find the site-packages folder for the current python."""
    folderName = "site-packages"
    paths = {}
    for s in sys.path:
        if s.find(folderName)!=-1:
            root = os.path.join(s.split(folderName)[0], folderName)
            paths[root] = True
    return list(paths.keys())

def writePathFile(pathFilePath, modulePaths):
    """Write the *.pth file to site-packages."""
    print("writing the modulePaths path to", pathFilePath)
    try:
        f = open(pathFilePath, 'w')
        f.write("\n".join(modulePaths))
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

