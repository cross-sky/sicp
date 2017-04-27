from e2_2_2 import *
def fringe(x):
	if is_leaf(x):
		return [x]
	else:
		leaf = [fringe(b) for b in x]
		return leaf