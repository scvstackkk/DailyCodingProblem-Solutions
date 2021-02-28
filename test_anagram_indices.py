import unittest
from anagram_indices import find_anagram_indices as fai
class TestAnagramIndices(unittest.TestCase):
	"""Unit tests for anagram problem."""

	def test_emptyString(self):
		"""Test for the empty string case."""
		word = "ab"
		string = ""
		result = []
		self.assertEqual(result, fai(word, string))
	def test_emptyWord(self):
		"""Test for the empty word case."""

unittest.main()
