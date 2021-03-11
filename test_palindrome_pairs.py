import unittest
import time
from palindrome_pairs import generate_palindrome_pairs_slow as gpps
from palindrome_pairs import generate_palindrome_pairs_fast as gppf

class TestPalindromePairs(unittest.TestCase):

	def test_empty_list(self):
		words = []
		result = []

		time_start = time.perf_counter()
		self.assertCountEqual(result, gpps(words))
		time_stop = time.perf_counter()
		gpps_runtime = time_stop - time_start

		time_start = time.perf_counter()
		self.assertCountEqual(result, gppf(words))
		time_stop = time.perf_counter()
		gppf_runtime = time_stop - time_start

		print("gpps runtime: " + str(gpps_runtime))
		print("gppf runtime: " + str(gppf_runtime))

	def test_book_example(self):
		words = ["code", "edoc", "da", "d"]
		result = [(0, 1), (1, 0), (2, 3)]

		time_start = time.perf_counter()
		self.assertCountEqual(result, gpps(words))
		time_stop = time.perf_counter()
		gpps_runtime = time_stop - time_start

		time_start = time.perf_counter()
		self.assertCountEqual(result, gppf(words))
		time_stop = time.perf_counter()
		gppf_runtime = time_stop - time_start

		print("gpps runtime: " + str(gpps_runtime))
		print("gppf runtime: " + str(gppf_runtime))

	def test_no_palindromes(self):
		words = ["frank", "mike", "john"]
		result = []

		time_start = time.perf_counter()
		self.assertCountEqual(result, gpps(words))
		time_stop = time.perf_counter()
		gpps_runtime = time_stop - time_start

		time_start = time.perf_counter()
		self.assertCountEqual(result, gppf(words))
		time_stop = time.perf_counter()
		gppf_runtime = time_stop - time_start

		print("gpps runtime: " + str(gpps_runtime))
		print("gppf runtime: " + str(gppf_runtime))

unittest.main()
