import os
import shutil
import unittest
import tempfile
from robofab.plistlib import readPlist
import robofab
from robofab.test.testSupport import fontInfoVersion2
from robofab.objects.objectsRF import NewFont, OpenFont
from robofab.ufoLib import UFOReader

ufoPath = os.path.dirname(robofab.__file__)
ufoPath = os.path.dirname(ufoPath)
ufoPath = os.path.dirname(ufoPath)
ufoPath = os.path.join(ufoPath, "TestData", "TestFont1 (UFO2).ufo")

class ReadUFOTestCase(unittest.TestCase):

	def setUpFont(self):
		self.font = OpenFont(ufoPath)
		self.font.update()

	def tearDownFont(self):
		self.font.close()
		self.font = None

	def compareToUFO(self, doInfo=True):
		reader = UFOReader(ufoPath)
		results = {}
		# info
		infoMatches = True
		info = self.font.info
		for attr, expectedValue in fontInfoVersion2.items():
			writtenValue = getattr(info, attr)
			if expectedValue != writtenValue:
				infoMatches = False
				break
		results["info"]= infoMatches
		# kerning
		kerning = self.font.kerning.asDict()
		expectedKerning = reader.readKerning()
		results["kerning"] = expectedKerning == kerning
		# groups
		groups = dict(self.font.groups)
		expectedGroups = reader.readGroups()
		results["groups"] = expectedGroups == groups
		# features
		features = self.font.features
		expectedFeatures = reader.readFeatures()
		results["features"] = expectedFeatures == features
		# lib
		lib = dict(self.font.lib)
		expectedLib = reader.readLib()
		results["lib"] = expectedLib == lib
		return results

	def testFull(self):
		self.setUpFont()
		otherResults = self.compareToUFO()
		self.assertEqual(otherResults["info"], True)
		self.assertEqual(otherResults["kerning"], True)
		self.assertEqual(otherResults["groups"], True)
		self.assertEqual(otherResults["features"], True)
		self.assertEqual(otherResults["lib"], True)
		self.tearDownFont()

	def testInfo(self):
		self.setUpFont()
		info = self.font.info
		for attr, expectedValue in fontInfoVersion2.items():
			writtenValue = getattr(info, attr)
			self.assertEqual((attr, expectedValue), (attr, writtenValue))
		self.tearDownFont()


class WriteUFOTestCase(unittest.TestCase):

	def setUpFont(self):
		self.dstDir = tempfile.mktemp()
		os.mkdir(self.dstDir)
		self.font = OpenFont(ufoPath)
		self.font.save(self.dstDir)

	def tearDownFont(self):
		shutil.rmtree(self.dstDir)

	def compareToUFO(self):
		readerExpected = UFOReader(ufoPath)
		readerWritten = UFOReader(self.dstDir)
		results = {}
		# info
		matches = True
		expectedPath = os.path.join(ufoPath, "fontinfo.plist")
		writtenPath = os.path.join(self.dstDir, "fontinfo.plist")
		if not os.path.exists(writtenPath):
			matches = False
		else:
			expected = readPlist(expectedPath)
			written = readPlist(writtenPath)
			for attr, expectedValue in expected.items():
				if expectedValue != written[attr]:
					matches = False
					break
		results["info"] = matches
		# kerning
		matches = True
		expectedPath = os.path.join(ufoPath, "kerning.plist")
		writtenPath = os.path.join(self.dstDir, "kerning.plist")
		if not os.path.exists(writtenPath):
			matches = False
		else:
			matches = readPlist(expectedPath) == readPlist(writtenPath)
		results["kerning"] = matches
		# groups
		matches = True
		expectedPath = os.path.join(ufoPath, "groups.plist")
		writtenPath = os.path.join(self.dstDir, "groups.plist")
		if not os.path.exists(writtenPath):
			matches = False
		else:
			matches = readPlist(expectedPath) == readPlist(writtenPath)
		results["groups"] = matches
		# features
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
		# lib
		matches = True
		expectedPath = os.path.join(ufoPath, "lib.plist")
		writtenPath = os.path.join(self.dstDir, "lib.plist")
		if not os.path.exists(writtenPath):
			matches = False
		else:
			writtenLib = readPlist(writtenPath)
			matches = readPlist(expectedPath) == writtenLib
		results["lib"] = matches
		return results

	def testFull(self):
		self.setUpFont()
		otherResults = self.compareToUFO()
		self.assertEqual(otherResults["info"], True)
		self.assertEqual(otherResults["kerning"], True)
		self.assertEqual(otherResults["groups"], True)
		self.assertEqual(otherResults["features"], True)
		self.assertEqual(otherResults["lib"], True)
		self.tearDownFont()


if __name__ == "__main__":
	from robofab.test.testSupport import runTests
	runTests()
