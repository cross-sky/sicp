from c2_3_4 import *

def generate_huffman_tree(pairs):
	return successive_merge(make_leaf_set(pairs))

def make_tree_set(pairs):
	if pairs == []:
		return []
	pair = car(pairs)
	return adjoin_set(pair, cdr(pairs))

@trace
def successive_merge(pairs):
	if len(pairs) == 1:
		return pairs
	s_a = car(pairs)
	s_b = cadr(pairs)
	if len(pairs) == 2:
		unpair = []
	else:
		unpair = pairs[2:]
	return successive_merge(make_tree_set([make_code_tree(s_a, s_b)] + unpair))

ta = [['A', 5], ['B', 2], ['C', 2], ['D', 1]]
