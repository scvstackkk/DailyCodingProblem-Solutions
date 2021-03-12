import unittest
from print_zig_zag import print_zig_zag as pzz

class TestPrintZigZag(unittest.TestCase):

	def test_empty_sentence_zero_lines(self):
		result = ""
		output = pzz("", 0)
		self.assertEqual(result, output)

	def test_empty_sentence_with_lines(self):
		result = ""
		output = pzz("", 20)
		self.assertEqual(result, output)

	def test_sentence_with_zero_lines(self):
		result = ""
		output = pzz("thisisazigzag", 0)
		self.assertEqual(result, output)

	def test_flat_sentence(self):
		result = "thisisazigzag"
		output = pzz("thisisazigzag", 1)
		self.assertEqual(result, output)

	def test_book_example(self):
		result =  "t     a     g" + "\n" + " h   s z   a " + "\n" + "  i i   i z  " + "\n" + "   s     g   "
		output = pzz("thisisazigzag", 4)
		self.assertEqual(result, output)

	def test_half_zig_zag(self):
		result = "h    " + "\n" + " e   " + "\n" + "  l  " + "\n" + "   l " + "\n" + "    o"
		output = pzz("hello", 5)
		self.assertEqual(result, output)

unittest.main()
