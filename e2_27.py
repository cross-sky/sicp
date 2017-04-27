from e2_18 import reverse2

def fringe(tree):
	return reverse2([reverse2(b) for b in tree])
"""

def fringe2(tree):
	for b in tree:
		reverse2(b)

		"""