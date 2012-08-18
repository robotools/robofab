"""


     Build the zipped robofab + dependency distros for RoboFab.
     Check out fresh copies of the code from SVN.
     Compile into zips.
     Write optional html page.
    

"""

import os, glob, time

def getRevision(url):
    """ Ask svn for the revision."""
    cmd = "svn info \"%s\""%url
    d = os.popen(cmd)
    data = d.read()
    lines = data.split("\n")
    for l in lines:
        if l.find("Revision:")==0:
            rev = l.split(' ')[-1]
            #print "svn rev:", rev
            return rev
    return "svn: no revision found"
    
def checkoutPackage(url, stagingFolder, verbose=True):
    """ checkoutPackage"""
    cwd = os.getcwd()
    if not os.path.exists(stagingFolder):
        os.makedirs(stagingFolder)
    os.chdir(stagingFolder)
    cmd = "svn export \"%s\" . --force"%(url)
    d = os.popen(cmd)
    if verbose:
        print d.read()
    else:
        d.read()
    d.close()
    #d = os.popen("svnversion")
    #revision = d.read()
    #os.chdir(cwd)
    #return revision.strip()

def buildProducts(products, buildFolder=None, deleteBuilds=False, verbose=True):
    """ Build the different distro products.
        - checkout a clean version from svn
        - add svn revision number to folder
        - zip folder
    """
    versions = {}
    cleanup = []
    filenames = []  # collect filenames of the new zips
    if buildFolder is None:
        buildFolder = os.path.join(os.path.dirname(__file__), "build")
        if verbose:
            print "\tNo build folder specified, using", buildFolder
        
    for productName, packages in products.items():
        cwd = os.getcwd()
        if verbose:
            print "cwd", cwd
        stagingFolder = os.path.join(buildFolder, productName%"temp")
        for url, name in packages:
            checkoutPackage(url, os.path.join(stagingFolder, name), verbose)
            versions[name] = getRevision(url)
        finalFolder = os.path.join(buildFolder, productName%versions.get('RoboFab', "?"))
        filenames.append(os.path.basename(finalFolder))
        d = os.popen("mv \"%s\" \"%s\""%(stagingFolder, finalFolder))
        if verbose:
            print d.read()
        else:
            d.read()
        os.chdir(finalFolder)
        d = os.popen("zip -r \"%s\" *"%finalFolder)
        if verbose:
            print d.read()
        else:
            d.read()
        cleanup.append(finalFolder)
        d.close()

    if deleteBuilds:
        for path in cleanup:
            if verbose:
                print "cleaning", path
            d = os.popen("rm -r \"%s\""%(path))
            if verbose:
                print d.read()
            else:
                d.read()
    return filenames
            
downloadPageTemplate = """<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN"
"http://www.w3.org/TR/html4/strict.dtd">

<html lang="en">
<head>
<link href="http://robofab.com/default.css" type="text/css" rel="stylesheet" />
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<title>RoboFab Downloads</title>
<meta name="generator" content="TextMate http://macromates.com/">
<meta name="author" content="Erik van Blokland">
<!-- Date: 2012-08-18 -->
</head>
<body>
<div id="modellogo">
	<img src="http://robofab.com/img/drawmodel_header.jpg" width="595" height="112" />
</div>
<div class="content">
<h1>Download RoboFab</h1>
<p>This page lists the current and (some) older distributions of RoboFab. These distributions contain packages from other developers. License info for these packages is contained in the distribution.</p>
<p><a href="http://code.robofab.com">The code.robofac.com Trac site</a></p>
<p><a href="http://robofab.com">Back to the RoboFab site</a></p>

<h2>Current distribution</h2>
<ul>%s</ul>

<h2>Old distributions</h2>
<ul>%s</ul>


<p>This page was generated on %s</p>

</div>
</body>
</html>
"""

def buildDownloadPage(folder, new=None):
    """ Build a new download page for the zips available in folder/."""
    if new is None:
        new = []
    htmlPath = os.path.join(folder, "index.html")
    timeStamp = str(time.asctime(time.localtime(time.time())))
    # collect .zip names
    newZips = []
    oldZips = []
    for n in glob.glob(os.path.join(folder, "*.zip")):
        name = os.path.basename(n)
        isNew = False
        for testName in new:
            if name.find(testName)==0:
                isNew = True
                break
        if isNew:
            newZips.append(name)
        else:
            oldZips.append(name)
    newLinks = "\n\t".join(["<li><a href=\"%s\">%s</a></li>"%(n,n) for n in newZips])
    oldLinks = "\n\t".join(["<li><a href=\"%s\">%s</a></li>"%(n,n) for n in oldZips])
    html = downloadPageTemplate%(newLinks, oldLinks, timeStamp)
    
    f = open(htmlPath, 'w')
    f.write(html)
    f.close()
    
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
    
    