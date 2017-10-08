from alice import *
from ucb import trace
def make_leaf(symbol, weight):
	return ["leaf", symbol, weight]

def leaf(object):
	return car(object) == "leaf"

def symbol_leaf(x):
	return cadr(x)

def weight_leaf(x):
	return caddr(x)

@trace
def make_code_tree(left, right):
	ls = symbol(left) + symbol(right)
	return [left, right] + [ls] +[weight(left) + weight(right)]
	#return [left, right] + [symbol(left), symbol(right)] +[weight(left) + weight(right)]

def left_branch(tree):
	return car(tree)

def right_branch(tree):
	return cadr(tree)

def symbol(tree):
	if leaf(tree):
		return [symbol_leaf(tree)]
	else:
		return caddr(tree)

def weight(tree):
	if leaf(tree):
		return weight_leaf(tree)
	else:
		return cadddr(tree)

def decode(bits, tree):
	@trace
	def decode_l(bits, current_branch):
		if bits == []:
			return []
		else:
			next_branch = choose_branch(car(bits), current_branch)
			if leaf(next_branch):
				return cons(symbol_leaf(next_branch), decode_l(cdr(bits), tree))
			else:
				return decode_l(cdr(bits), next_branch)
	return decode_l(bits, tree)

def choose_branch(bit, branch):
	if bit == 0:
		return left_branch(branch)
	elif bit == 1:
		return right_branch(branch)
	else:
		return 'mmmmmm'

@trace
def adjoin_set(x, set):
	if set == []:
		return [x]
	elif weight(x) <= weight(car(set)):
		return cons(x, set)
	else:
		return cons(car(set), adjoin_set(x, cdr(set)))

@trace
def make_leaf_set(pairs):
	#[['A', 4], ['B', 1], ['C', 2], ['D', 1]]
	if pairs == []:
		return []
	pair = car(pairs)
	return adjoin_set(make_leaf(car(pair), cadr(pair)), make_leaf_set(cdr(pairs)))