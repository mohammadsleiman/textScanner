import unittest
from textMatch import *

class Test(unittest.TestCase):
	def test_wordWithMatch(self):
		stringMatchCount = getStringMatchCount("sampletext.txt","hi" )
		self.assertEqual(stringMatchCount, 3, "incorrect count for word: 'hi'")
	
	def test_wordNoMatch(self):
		stringMatchCount = getStringMatchCount("sampletext.txt","Esoteric")
		self.assertEqual(stringMatchCount, 0, "non zero count for non existent word: 'Esoteric'")
	
	def test_sentence(self):
		stringMatchCount = getStringMatchCount("sampletext.txt","The quick brown fox jumps over the lazy dog")
		self.assertEqual(stringMatchCount, 2, "incorrect count for sentence: 'The quick brown fox jumps over the lazy dog'")
	
	def test_sentenceNoMatch(self):
		stringMatchCount = getStringMatchCount("sampletext.txt","The brick crowned crocs jumps over the hazy fog")
		self.assertEqual(stringMatchCount, 0, "incorrect count for sentence: 'The brick crowned crocs jumped over the hazy fog'")
	
	def test_emptySpace(self):
		stringMatchCount = getStringMatchCount("sampletext.txt"," ")
		self.assertEqual(stringMatchCount, 194, "incorrect count for ' '")
	
	def test_wordInEmptyFile(self):
		stringMatchCount = getStringMatchCount("emptytext.txt","hi")
		self.assertEqual(stringMatchCount, 0, "incorrect count for word: 'hi'")

	def test_InvalidFileName(self):
		stringMatchCount = getStringMatchCount("nonexistentfile.txt", "hi")
		self.assertEqual(stringMatchCount, -1, "incorrect handling of invalid file name")

if __name__ == '__main__':
	unittest.main()





