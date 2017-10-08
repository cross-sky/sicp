from c2_3_3c import *

from ucb import trace

@trace
def tree_to_list_1(tree):
	if type(tree) == int:
		return [tree]
	elif len(tree) == 0:
		return []
	else:
		return tree_to_list_1(left_branch(tree)) + cons(entry(tree), tree_to_list_1(right_branch(tree)))

def tree_to_list_2(tree):
	def copy_to_list(tree, result):
		if type(tree) == int:
			return [tree] + result
		elif len(tree) == 0:
			return result
		else:
			return copy_to_list(left_branch(tree), cons(entry(tree), copy_to_list(right_branch(tree), result)))
	return copy_to_list(tree, [])

tree1 = make_tree(7, make_tree(3, 1, 5), make_tree(9, [], 11))

#tree_to_list_1(tree1)