from alice import *
from ucb import trace
def scale_tree(tree, factor):
	if len(tree) < 1:
		return []
	if is_leaf(tree):
		return tree[0] * factor
	else:
		return cons(scale_tree(car(tree), factor), scale_tree(cdr(tree), factor))

def is_leaf(tree):
	return not tree[1:]

@trace
def scale_tree1(tree, factor):
	if type(tree) == int:
		return [tree * factor]
	if len(tree) < 1:
		return []
	else:
		return cons(scale_tree1(car(tree), factor), scale_tree1(cdr(tree), factor))


