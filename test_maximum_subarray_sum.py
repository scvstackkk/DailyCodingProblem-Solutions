import unittest
import maximum_subarray_sum as mss

class TestMaxSubarraySum(unittest.TestCase):
	"""Test the solution to the maximum subarray sum problem."""

	def test_ZeroSumCase(self):
		test_data = [-5, -1, -8, -9]
		max = mss.maximum_subarray_sum(test_data)
		self.assertEqual(0, max)

	def test_example1SumCase(self):
		test_data = [34, -50, 42, 14, -5, 86]
		max = mss.maximum_subarray_sum(test_data)
		self.assertEqual(137, max)

	def test_example2SumCase(self):
		test_data = [-20, -10, 60, 20, 10, -20, -30]
		max = mss.maximum_subarray_sum(test_data)
		self.assertEqual(90, max)
unittest.main()
