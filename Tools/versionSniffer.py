"""
    
    This script can be run as a FontLab macro.
    It prints version numbers of the application, python,
    and the contents of the relevant site-packages folder.
    Can be useful in finding out what you have installed where.
    
    erik@letterror.com 10_2011
    v 1.1   # removes assert

"""

try:
    print("\n", "-"*40)
    from FL import*
    print("fontlab version", fl.version)
except ImportError:
    print("probably not in FontLab.")

print("\n", "-"*40)
import sys, os
print("python version", sys.version)

def findSitePackages():
    folderName = "site-packages"
    paths = {}
    for s in sys.path:
        if s.find(folderName)!=-1:
            root = os.path.join(s.split(folderName)[0], folderName)
            paths[root] = True
    safe = []
    return list(paths.keys())

def dumpSitePackages(root):
    for n in os.listdir(root):
        if os.path.splitext(n)[-1] == ".pth":
            linkPath = os.path.join(root, n)
            print("\n", "-"*40)
            print("\t", n.encode('ascii'))
            print("\t", linkPath.encode('ascii'))

            f = open(linkPath, 'r')
            d = f.read()
            f.close()
            print("\tcontents:")
            for l in d.split("\n"):
                print("\t\t", l.encode("ascii"))
        
for sp in findSitePackages():
    print("\n", "-"*40)
    print("site-packages is at", sp)

    dumpSitePackages(sp)


