"""
From the text:
2.2 Generate palindrome pairs

Given a list of words, find all pairs of unique indices such that the
concatenation of the two words is a palindrome.

For example, given the list ["code", "edoc", "da", "d"], return
[(0, 1), (1, 0), (2, 3)].
"""

# Most of this solution was ripped from the text as this problem is not really about brute force building palindromes (as the naive approach solves it)
# but rather the focus is understanding how to build all potential complementary words that form palindromes and looking for those in the given list.
# I had started on the right path in my head (looking at the beginning/prefix and ending/suffix of words and using those characters to rule out a potential palindrome pair),
# but I faltered in that I was comparing those prefixes/suffixes with all existing words, essentially doubling the memory requirement without lowering the runtime.
def is_palindrome(word):
	return word == word[::-1]

# O(n^2 * k), k = length of longest word
def generate_palindrome_pairs_slow(words):
	result = []
	for w1_index, w1 in enumerate(words):
		for w2_index, w2 in enumerate(words):
			if w1_index == w2_index:
				continue
			if is_palindrome(w1 + w2):
				result.append((w1_index, w2_index))
	return result

# O(n * k^2), k = length of longest word
def generate_palindrome_pairs_fast(words):
	result = []
	word_dict = {}
	for index, word in enumerate(words):
		word_dict[word] = index
	for index, word in enumerate(words):
		for i in range(len(word)):
		# We want to find prefix & reversed suffix pairings as these will form potential palindromes, in addition to suffix & reversed prefix pairings
			prefix_word = word[:i]
			suffix_word = word[i:]
			reversed_prefix_word = prefix_word[::-1]
			reversed_suffix_word = suffix_word[::-1]
			# check for pairings
			# prefix & reversed suffix
			if (is_palindrome(prefix_word) and reversed_suffix_word in word_dict.keys()):
				if word_dict[reversed_suffix_word] != index:
					result.append((word_dict[reversed_suffix_word], index))
			# suffix & reversed prefix
			if (is_palindrome(suffix_word) and reversed_prefix_word in word_dict.keys()):
				if word_dict[reversed_prefix_word] != index:
					result.append((index, word_dict[reversed_prefix_word]))
	return result
