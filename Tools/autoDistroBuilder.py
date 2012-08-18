import sys

if len(sys.argv) == 2:
    # we're called as a shellscript
    # assume the path is the second argument
    testBuildFolder = sys.argv[1]
else:
    testBuildFolder = "/Users/erik/Develop/svn.robofab.com/randomOtherDifferentDirectory"
    

"""

    Build a robofab distro from SVN
    Store it in a new directory not in the robofab tree
    Write an html page.
    
"""

from buildRoboFabDistroFromSVN import buildProducts, buildDownloadPage

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

filenames = buildProducts(robofabProducts, buildFolder=testBuildFolder, deleteBuilds=True, verbose=False)

#print "writing html"
buildDownloadPage(testBuildFolder, new=filenames)

#print "filenames", filenames
#print "done"