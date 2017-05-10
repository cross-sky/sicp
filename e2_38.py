from c2_2_3b import *
def fold_left(op, initial, sequence):
	def iter(result, rest):
		if len(rest) < 1:
			return result
		else:
			return iter(op(result, car(rest)), cdr(rest))
	return iter(initial, sequence)

def fold_right(op, initial, sequence):
	return accumulate(op, initial, sequence)
