"""


     Build the zipped robofab + dependency distros for RoboFab.
     Check out fresh copies of the code from SVN.
     Compile into zips.
    

"""

import os

def checkoutPackage(url, stagingFolder):
    cwd = os.getcwd()
    if not os.path.exists(stagingFolder):
        os.makedirs(stagingFolder)
    os.chdir(stagingFolder)
    cmd = "svn co \"%s\" ."%(url)
    d = os.popen(cmd)
    print d.read()
    d.close()
    d = os.popen("svnversion")
    revision = d.read()
    os.chdir(cwd)
    return revision.strip()

def buildProducts(products):
    versions = {}
    buildFolder = os.path.join(os.path.dirname(__file__), "build")
    for productName, packages in products.items():
        cwd = os.getcwd()
        stagingFolder = os.path.join(buildFolder, productName%"temp")
        for url, name in packages:
            version = checkoutPackage(url, os.path.join(stagingFolder, name))
            versions[name] = version
        finalFolder = os.path.join(buildFolder, productName%versions.get('RoboFab', "?"))
        d = os.popen("mv \"%s\" \"%s\""%(stagingFolder, finalFolder))
        print d.read()
        os.chdir(finalFolder)
        d = os.popen("zip -r \"%s\" *"%finalFolder)
        print d.read()
        os.chdir(cwd)
        d = os.popen
    
if __name__ == "__main__":
    robofabProducts = {
        'RoboFab_%s_plusAllDependencies':[
            ("http://svn.robofab.com/trunk", "RoboFab"),
            ("http://svn.typesupply.com/packages/vanilla/trunk", "Vanilla"),
            ("http://svn.typesupply.com/packages/dialogKit/trunk", "DialogKit"),
            ("https://fonttools.svn.sourceforge.net/svnroot/fonttools/trunk/", "FontTools")
        ],
        'RoboFab_%s_plusFontTools':[
            ("http://svn.robofab.com/trunk", "RoboFab"),
            ("https://fonttools.svn.sourceforge.net/svnroot/fonttools/trunk/", "FontTools")
        ],
        'RoboFab_%s_only':[
            ("http://svn.robofab.com/trunk", "RoboFab"),
        ],
    }
    buildProducts(robofabProducts)
    
    