"""
From the book:

2.3 Print zigzag form

Given a string and a number of lines k, print the string in zigzag form.
In zigzag, characters are printed out diagonally from top left to bottom right until reaching
the k-th line, then back up to top right, and so on.

For example, given the sentence "thisisazigzag" and k = 4, you should print:

t     a     g
 h   s z   a
  i i   i z
   s     g
"""
# Runtime = O(n * k) where n = length of sentence
def print_zig_zag(sentence, k):
	if k == 0:
		return ""
	elif k == 1 or sentence == "":
		return sentence
	lines = {}
	current_line = 0
	while current_line != k:
		lines[current_line] = ""
		current_line += 1
	line_cursor = (0, "UP")
	for c in sentence:
		for i in range(k):
			if i == line_cursor[0]:
				lines[i] += c
			else:
				lines[i] += " "
		line_cursor = update_cursor(line_cursor[0], k, line_cursor[1])
	output = ""
	for i in range(k):
		if i == k - 1:
			output += lines[i]
		else:
			output += lines[i]
			output += "\n"
	return output

def update_cursor(counter, limit, direction):
	if (direction == "UP" and counter < limit - 1):
		counter += 1
		return (counter, direction)
	elif (direction == "UP" and counter == limit - 1):
		direction = "DOWN"
		counter -= 1
		return (counter, direction)
	elif (direction == "DOWN" and counter > 0):
		counter -= 1
		return (counter, direction)
	else:
		direction = "UP"
		counter += 1
		return (counter, direction)

