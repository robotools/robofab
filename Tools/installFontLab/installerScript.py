# This is a automatically generated installer script for FontLab
# Generated on %(timeStamp)s
# scriptVersion: %(scriptVersion)s

p = "%(appLogPath)s"
log(p,"-" * 50)
log(p,"hello, this is application: %(appName)s")
log(p,"Running script version: %(scriptVersion)s")
log(p,"Platform:"+platform.platform())
resultData = []
resultData.append("application:\t%(appName)s")
print "I will log to", "%(appLogPath)s"
print "I will save my results to", "%(resultsPath)s"
print "I will test for these modules:", "%(moduleData)s"
from FL import *
log(p,"FontLab version "+fl.version)
resultData.append("version:\t"+fl.version)

installedAlready = False

for moduleName, data in %(moduleData)s.items():
    print "---", moduleName, data
    try:
        print "---", __import__(moduleName, globals(), locals(), [], -1)
        resultData.append("found:\t"+,moduleName)
    except ImportError:
        resultData.append("mustLoad:\t"+moduleName)

sitePackagesCandidates = findSitePackages()
for candidate in findSitePackages():
    resultData.append("path:\t"+candidate)
    log(p,"site-packages found at: "+candidate)

f = open("%(resultsPath)s", 'wb')
f.write("\n".join(resultData))
f.close()
log(p,'done!')