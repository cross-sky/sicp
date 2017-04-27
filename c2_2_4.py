from c2_2_2 import *
from ucb import trace

"""fail"""
@trace
def scale_tree(tree, fractor):
	if is_leaf(tree):
		return root(tree) * fractor
	else:
		count = [scale_tree(b, fractor) for b in branches(tree)]
		return sum(count)
