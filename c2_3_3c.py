from alice import *

def entry(tree):
	return car(tree)

def left_branch(tree):
	return cadr(tree)

def right_branch(tree):
	return caddr(tree)

def make_tree(entry, left, right):
	return list([entry, left, right])
	#return list(list([entry]), list([left]), list([right]))
	#return [[entry], left, right]

def element_of_set(x, set):
	if len(set) == 0:
		return False
	if entry(set) == x:
		return True
	elif entry(set) < x:
		return element_of_set(x, right_branch(set))
	else:
		return element_of_set(x, left_branch(set))

def adjoin_set(x, set):
	if len(set) == 0:
		return make_tree(x, [], [])
	if entry(set) == x:
		return set
	elif entry(set) > x:
		return make_tree(entry, adjoin_set(x, left_branch(set), right_branch(set)))
	else:
		return make_tree(entry, left_branch(set), adjoin_set(x, right_branch(set)))

