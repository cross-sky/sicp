def tree(root, branches = []):
	for branch in branches:
		assert is_tree(branch), 'branches must be a tree'
	return [root] + list(branches)

def is_tree(tree):
	if type(tree) != list or len(tree) < 1:
		return False
	for branch in branches(tree):
		if not is_tree(branch):
			return False
	return True

def branches(tree):
	return tree[1:]

def root(tree):
	return tree[0]

def is_leaf(tree):
	return not branches(tree)

def count_leaves(tree):
	if is_leaf(tree):
		return 1
	else:
		count = [count_leaves(b) for b in branches(tree)]
		return sum(count)