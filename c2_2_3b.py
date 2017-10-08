from alice import *
from operator import add, mul, truediv
from ucb import trace
#@trace
def accumulate(op, initial, sequence):
	if len(sequence) < 1:
		return initial
	return op(car(sequence), accumulate(op, initial, cdr(sequence)))

def enumerate(low, high):
	if low > high:
		return []
	else:
		return cons(low, enumerate(low + 1, high))

def tree_leaf(tree):
	if type(tree) == int:
		return [tree]
	if len(tree) < 1:
		return []
	else:
		return tree_leaf(car(tree)) + tree_leaf(cdr(tree))
#@trace
def maps(proc, items):
	if len(items) < 1:
		return []
	else:
		return cons(proc(car(items)), maps(proc, cdr(items)))