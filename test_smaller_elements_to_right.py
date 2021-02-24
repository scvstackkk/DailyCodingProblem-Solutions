import unittest
from smaller_elements_to_right import num_of_smaller_elements_to_right as nser

class TestNumberOfSmallerElementsToRight(unittest.TestCase):
	"""Test the *nser* algorithm."""

	def test_book_example(self):
		"""Test case from book."""
		test_data = [3, 4, 9, 6, 1]
		solution = [1, 1, 2, 1, 0]
		result = nser(test_data)
		self.assertEqual(result, solution)

	def test_empty_case(self):
		"""Test case for empty list."""
		test_data = []
		solution = []
		result = nser(test_data)
		self.assertEqual(result, solution)

	def test_single_element_case(self):
		"""Test case for single element list."""
		test_data = [4]
		solution = [0]
		result = nser(test_data)
		self.assertEqual(result, solution)

	def test_equal_elements_case(self):
		"""Test case for list of equal elements."""
		test_data = [1, 1, 1, 1, 1]
		solution = [0, 0, 0, 0, 0]
		result = nser(test_data)
		self.assertEqual(result, solution)

	def test_repeat_values_case(self):
		"""Test case for list with repeated values. This case is important for ensuring 
		that larger values are correctly placed in the list of sorted seen elements."""
		test_data = [3, 4, 9, 6, 1, 3, 9, 9]
		solution = [1, 2, 3, 2, 0, 0, 0, 0]
		result = nser(test_data)
		self.assertEqual(result, solution)

unittest.main()
