from e2_33 import *
def accumulate_n(op, init, sequence):
	"""
	s = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
	>>> accumulate_n(add, 0, s)
	>>> [22, 26, 30]
	"""
	if len(car(sequence)) < 1:
		return []
	else:
		return cons(accumulate(add, 0, map(car, sequence)),
			accumulate_n(op, init, map(cdr, sequence)))