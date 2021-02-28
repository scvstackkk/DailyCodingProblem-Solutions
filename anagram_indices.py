

def find_anagram_indices(w, s):
	"""Given a word *w* and a string *s*, find all indices in *s* which are the starting
	locations of anagrams of *w*. Example w="ab" and s="abxaba", return [0, 3, 4]. Runs in O(n) with O(k) storage where k = length of arg *w*."""

	# --Notes--
	# Anagram defintion - the ability to rearrange a sequence of characters to form different words.
	# Each character is to be used only once and the pool of characters must be sequential (contiguous). Traverse left to right
	# Strings are immutable in python

	# Approach: this can be done faster than n^2 as you can create copies of *w* (a list of the characters, not a copy of *w*) and pop matching characters as you traverse *s*
	# the only trade-off being O(n) storage.
	# if the copy of *w* reaches '', all characters have been found and so has an anagram.
	# if extra repeats of matching characters are found before the copy of *w* reaches '', reset the match (can't exclude characters as anagrams must be contiguous)
	# ex. w="ab" and s = "aabxbba" -> return [1, 5]
	# shared matches are allowed between two contiguous anagrams (see first example in docstring where the second "b" is reused)

	anagram_indices = []
	anagram_index = 0
	current_index = 0
	anagram = [character for character in w]
	anagram_copy = anagram.copy()

	for character in s:
		if not(character in anagram_copy):
			if character in anagram: # repeat character -> reset the copy and pop this character from it
				anagram_copy = anagram.copy()
				anagram_copy.remove(character)
				anagram_index = current_index
				current_index += 1
			else: # character is not in original anagram -> reset copy
				anagram_copy = anagram.copy()
				current_index += 1
				anagram_index = current_index
		else:
			anagram_copy.remove(character)
			if len(anagram_copy) == 0: # anagram found
				anagram_indices.append(anagram_index)
				anagram_copy = anagram.copy()
				anagram_copy.remove(character)
				anagram_index = current_index
				current_index += 1
			else: # characters remain -> move index and continue
				current_index += 1

	return anagram_indices

