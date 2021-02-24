def num_of_smaller_elements_to_right(arr):
	"""Given a list *arr*, return a list that represents the number of smaller elements
	to the right of each element in the original list *arr*.
	(i.e. [3, 4, 9, 6, 1] -> [1, 1, 2, 1, 0]). Main loop O(n) * Inner sorting O(lg n) = O(nlgn)"""

	# if list is empty, return an empty list
	if len(arr) == 0:
		return []

	# create the list of seen elements
	seen = []

	# no elements to the right of the last one
	seen.append(arr[-1])
	solution = [0]


	for i in range(len(arr) - 2, -1, -1): # loop backwards through the list
		current_element = arr[i]
		seen.append(current_element)
		seen.sort()
		location = seen.index(current_element) # returns the first occurence of the given element in the seen list (in case of duplicate values i.e. [0, 0, *1*, 1, 5, 7, ...]
		if location == 0: # no elements smaller to the right in *arr*
			solution.insert(0, 0)
		else:
			num_smaller = location
			solution.insert(0, num_smaller)
	return solution


