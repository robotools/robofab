import os
import shutil
import unittest
import tempfile
from robofab.plistlib import readPlist
import robofab
from robofab.ufoLib import UFOReader, UFOWriter
from robofab.test.testSupport import fontInfoVersion2
from robofab.objects.objectsFL import NewFont, OpenFont

vfbPath = os.path.dirname(robofab.__file__)
vfbPath = os.path.dirname(vfbPath)
vfbPath = os.path.dirname(vfbPath)
vfbPath = os.path.join(vfbPath, "TestData", "TestFont1.vfb")

ufoPath = os.path.dirname(robofab.__file__)
ufoPath = os.path.dirname(ufoPath)
ufoPath = os.path.dirname(ufoPath)
ufoPath = os.path.join(ufoPath, "TestData", "TestFont1 (UFO2).ufo")

class ReadUFOTestCase(unittest.TestCase):

	def setUpFont(self, doInfo=False, doKerning=False, doGroups=False, doLib=False, doFeatures=False):
		self.font = NewFont()
		self.ufoPath = ufoPath
		self.font.readUFO(ufoPath, doInfo=doInfo, doKerning=doKerning, doGroups=doGroups, doLib=doLib, doFeatures=doFeatures)
		self.font.update()

	def tearDownFont(self):
		self.font.close()
		self.font = None

	def compareToUFO(self, doInfo=True, doKerning=True, doGroups=True, doLib=True, doFeatures=True):
		reader = UFOReader(self.ufoPath)
		results = {}
		if doInfo:
			infoMatches = True
			info = self.font.info
			for attr, expectedValue in fontInfoVersion2.items():
				# cheat by skipping attrs that aren't supported
				if info._ufoToFLAttrMapping[attr]["nakedAttribute"] is None:
					continue
				writtenValue = getattr(info, attr)
				if expectedValue != writtenValue:
					infoMatches = False
					break
			results["info"]= infoMatches
		if doKerning:
			kerning = self.font.kerning.asDict()
			expectedKerning = reader.readKerning()
			results["kerning"] = expectedKerning == kerning
		if doGroups:
			groups = dict(self.font.groups)
			expectedGroups = reader.readGroups()
			results["groups"] = expectedGroups == groups
		if doFeatures:
			features = self.font._openTypeFeatureText()
			expectedFeatures = reader.readFeatures()
			results["features"] = expectedFeatures == features
		if doLib:
			lib = dict(self.font.lib)
			expectedLib = reader.readLib()
			results["lib"] = expectedLib == lib
		return results

	def testFull(self):
		self.setUpFont(doInfo=True, doKerning=True, doGroups=True, doFeatures=True, doLib=True)
		otherResults = self.compareToUFO()
		self.assertEqual(otherResults["info"], True)
		self.assertEqual(otherResults["kerning"], True)
		self.assertEqual(otherResults["groups"], True)
		self.assertEqual(otherResults["features"], True)
		self.assertEqual(otherResults["lib"], True)
		self.tearDownFont()

	def testInfo(self):
		self.setUpFont(doInfo=True)
		otherResults = self.compareToUFO(doInfo=False)
		self.assertEqual(otherResults["kerning"], False)
		self.assertEqual(otherResults["groups"], False)
		self.assertEqual(otherResults["features"], False)
		self.assertEqual(otherResults["lib"], False)
		info = self.font.info
		for attr, expectedValue in fontInfoVersion2.items():
			# cheat by skipping attrs that aren't supported
			if info._ufoToFLAttrMapping[attr]["nakedAttribute"] is None:
				continue
			writtenValue = getattr(info, attr)
			self.assertEqual((attr, expectedValue), (attr, writtenValue))
		self.tearDownFont()

	def testFeatures(self):
		self.setUpFont(doFeatures=True)
		otherResults = self.compareToUFO()
		self.assertEqual(otherResults["info"], False)
		self.assertEqual(otherResults["kerning"], False)
		self.assertEqual(otherResults["groups"], False)
		self.assertEqual(otherResults["features"], True)
		self.assertEqual(otherResults["lib"], False)
		self.tearDownFont()

	def testKerning(self):
		self.setUpFont(doKerning=True)
		otherResults = self.compareToUFO()
		self.assertEqual(otherResults["info"], False)
		self.assertEqual(otherResults["kerning"], True)
		self.assertEqual(otherResults["groups"], False)
		self.assertEqual(otherResults["features"], False)
		self.assertEqual(otherResults["lib"], False)
		self.tearDownFont()

	def testGroups(self):
		self.setUpFont(doGroups=True)
		otherResults = self.compareToUFO()
		self.assertEqual(otherResults["info"], False)
		self.assertEqual(otherResults["kerning"], False)
		self.assertEqual(otherResults["groups"], True)
		self.assertEqual(otherResults["features"], False)
		self.assertEqual(otherResults["lib"], False)
		self.tearDownFont()

	def testLib(self):
		self.setUpFont(doLib=True)
		otherResults = self.compareToUFO()
		self.assertEqual(otherResults["info"], False)
		self.assertEqual(otherResults["kerning"], False)
		self.assertEqual(otherResults["groups"], False)
		self.assertEqual(otherResults["features"], False)
		self.assertEqual(otherResults["lib"], True)
		self.tearDownFont()

class WriteUFOTestCase(unittest.TestCase):

	def setUpFont(self, doInfo=False, doKerning=False, doGroups=False, doLib=False, doFeatures=False):
		#self.dstDir = tempfile.mktemp()
		#os.mkdir(self.dstDir)
		d = "/Users/tal/Desktop/crap"
		number = len(os.listdir(d))
		self.dstDir = os.path.join(d, str(number) + ".ufo")
		self.font = OpenFont(vfbPath)
		self.font.writeUFO(self.dstDir, doInfo=doInfo, doKerning=doKerning, doGroups=doGroups, doLib=doLib, doFeatures=doFeatures)
		self.font.close()

	def tearDownFont(self):
		shutil.rmtree(self.dstDir)

	def compareToUFO(self, doInfo=True, doKerning=True, doGroups=True, doLib=True, doFeatures=True):
		readerExpected = UFOReader(ufoPath)
		readerWritten = UFOReader(self.dstDir)
		results = {}
		if doInfo:
			matches = True
			expectedPath = os.path.join(ufoPath, "fontinfo.plist")
			writtenPath = os.path.join(self.dstDir, "fontinfo.plist")
			if not os.path.exists(writtenPath):
				matches = False
			else:
				dummyFont = NewFont()
				_ufoToFLAttrMapping = dict(dummyFont.info._ufoToFLAttrMapping)
				dummyFont.close()
				expected = readPlist(expectedPath)
				written = readPlist(writtenPath)
				for attr, expectedValue in expected.items():
					# cheat by skipping attrs that aren't supported
					if _ufoToFLAttrMapping[attr]["nakedAttribute"] is None:
						continue
					if expectedValue != written[attr]:
						matches = False
						break
			results["info"] = matches
		if doKerning:
			matches = True
			expectedPath = os.path.join(ufoPath, "kerning.plist")
			writtenPath = os.path.join(self.dstDir, "kerning.plist")
			if not os.path.exists(writtenPath):
				matches = False
			else:
				matches = readPlist(expectedPath) == readPlist(writtenPath)
			results["kerning"] = matches
		if doGroups:
			matches = True
			expectedPath = os.path.join(ufoPath, "groups.plist")
			writtenPath = os.path.join(self.dstDir, "groups.plist")
			if not os.path.exists(writtenPath):
				matches = False
			else:
				matches = readPlist(expectedPath) == readPlist(writtenPath)
			results["groups"] = matches
		if doFeatures:
			matches = True
			expectedPath = os.path.join(ufoPath, "features.fea")
			writtenPath = os.path.join(self.dstDir, "features.fea")
			if not os.path.exists(writtenPath):
				matches = False
			else:
				f = open(expectedPath, "r")
				expectedText = f.read()
				f.close()
				f = open(writtenPath, "r")
				writtenText = f.read()
				f.close()
				# FontLab likes to add lines to the features, so skip blank lines.
				expectedText = [line for line in expectedText.splitlines() if line]
				writtenText = [line for line in writtenText.splitlines() if line]
				matches = "\n".join(expectedText) == "\n".join(writtenText)
			results["features"] = matches
		if doLib:
			matches = True
			expectedPath = os.path.join(ufoPath, "lib.plist")
			writtenPath = os.path.join(self.dstDir, "lib.plist")
			if not os.path.exists(writtenPath):
				matches = False
			else:
				# the test file doesn't have the glyph order
				# so purge it from the written
				writtenLib = readPlist(writtenPath)
				del writtenLib["org.robofab.glyphOrder"]
				matches = readPlist(expectedPath) == writtenLib
			results["lib"] = matches
		return results

	def testFull(self):
		self.setUpFont(doInfo=True, doKerning=True, doGroups=True, doFeatures=True, doLib=True)
		otherResults = self.compareToUFO()
		self.assertEqual(otherResults["info"], True)
		self.assertEqual(otherResults["kerning"], True)
		self.assertEqual(otherResults["groups"], True)
		self.assertEqual(otherResults["features"], True)
		self.assertEqual(otherResults["lib"], True)
		self.tearDownFont()

	def testInfo(self):
		self.setUpFont(doInfo=True)
		otherResults = self.compareToUFO(doInfo=False)
		self.assertEqual(otherResults["kerning"], False)
		self.assertEqual(otherResults["groups"], False)
		self.assertEqual(otherResults["features"], False)
		self.assertEqual(otherResults["lib"], False)
		expectedPath = os.path.join(ufoPath, "fontinfo.plist")
		writtenPath = os.path.join(self.dstDir, "fontinfo.plist")
		expected = readPlist(expectedPath)
		written = readPlist(writtenPath)
		dummyFont = NewFont()
		_ufoToFLAttrMapping = dict(dummyFont.info._ufoToFLAttrMapping)
		dummyFont.close()
		for attr, expectedValue in expected.items():
			# cheat by skipping attrs that aren't supported
			if _ufoToFLAttrMapping[attr]["nakedAttribute"] is None:
				continue
			self.assertEqual((attr, expectedValue), (attr, written[attr]))
		self.tearDownFont()

	def testFeatures(self):
		self.setUpFont(doFeatures=True)
		otherResults = self.compareToUFO()
		self.assertEqual(otherResults["info"], False)
		self.assertEqual(otherResults["kerning"], False)
		self.assertEqual(otherResults["groups"], False)
		self.assertEqual(otherResults["features"], True)
		self.assertEqual(otherResults["lib"], False)
		self.tearDownFont()

	def testKerning(self):
		self.setUpFont(doKerning=True)
		otherResults = self.compareToUFO()
		self.assertEqual(otherResults["info"], False)
		self.assertEqual(otherResults["kerning"], True)
		self.assertEqual(otherResults["groups"], False)
		self.assertEqual(otherResults["features"], False)
		self.assertEqual(otherResults["lib"], False)
		self.tearDownFont()

	def testGroups(self):
		self.setUpFont(doGroups=True)
		otherResults = self.compareToUFO()
		self.assertEqual(otherResults["info"], False)
		self.assertEqual(otherResults["kerning"], False)
		self.assertEqual(otherResults["groups"], True)
		self.assertEqual(otherResults["features"], False)
		self.assertEqual(otherResults["lib"], False)
		self.tearDownFont()

	def testLib(self):
		self.setUpFont(doLib=True)
		otherResults = self.compareToUFO()
		self.assertEqual(otherResults["info"], False)
		self.assertEqual(otherResults["kerning"], False)
		self.assertEqual(otherResults["groups"], False)
		self.assertEqual(otherResults["features"], False)
		self.assertEqual(otherResults["lib"], True)
		self.tearDownFont()


if __name__ == "__main__":
	from robofab.test.testSupport import runTests
	runTests()
