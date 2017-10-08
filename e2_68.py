from e2_67 import *

def encode(message, tree):
	if message == []:
		return []
	else:
		return encode_symbol(car(message), tree) + encode(cdr(message), tree)

def encode_symbol(symbo, tree):
	@trace
	def encode_l(symbo, tree, result):
		if leaf(tree):
			return result
		if tree == []:
			return ["eeee"]
		if symbol_in_tree(symbo, left_branch(tree)):
			return encode_l(symbo, left_branch(tree), result + [0])
		elif symbol_in_tree(symbo, right_branch(tree)):
			return encode_l(symbo, right_branch(tree), result + [1])
		else:
			raise NameError("symbol not exit") 
	return encode_l(symbo, tree, [])


"""		else:
			next_branch = left_branch(tree)
			if leaf(next_branch):
				if symbo == symbol_leaf(next_branch):
					return result + [0]
			if leaf(right_branch(tree)):
				if symbo == symbol_leaf(right_branch(tree)):
					return result + [1]
			return encode_l(symbo, right_branch(tree), result + [1])"""

def symbol_in_tree(symbo, tree):
	if symbo in symbol(tree):
		return True
	else:
		return False

t = ['A', 'D', 'A', 'B', 'B', 'C', 'A']