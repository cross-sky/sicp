from e2_38 import *
def reverse(sequence):
	"""attention cons(x, y), not simple change position"""
	return fold_right(lambda x, y: list(y) + [x], [], sequence)

def reverse_l(sequence):
	return fold_left(lambda x, y: cons(y, x), [], sequence)

