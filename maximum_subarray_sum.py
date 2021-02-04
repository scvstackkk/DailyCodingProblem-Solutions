def maximum_subarray_sum(items):
	"""Given a list of integers, return the maximum sum within a contiguous portion of the array"""
	max_sum = 0
	running_sum = 0
	for item in items:
		if item > 0 and max_sum == 0:
			max_sum = item
			running_sum += item
		elif item > 0 and max_sum != 0:
			running_sum += item
			if running_sum > max_sum:
				max_sum = running_sum
		elif item < 0 and running_sum > 0:
			running_sum += item
			if running_sum < 0:
				running_sum = 0
	return max_sum
