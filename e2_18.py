from ucb import trace
def branch(input_list):
	return input_list[1:]
def last(input_list):
	return not branch(input_list)
def leaf(input_list):
	return [input_list[0]]

def reverse2(input_list):
	if last(input_list):
		return leaf(input_list)
	else:
		return reverse2(branch(input_list)) + leaf(input_list)

@trace
def reverse(input_list):
	@trace
	def iter(src, dst):
		if last(src):
			return leaf(src) + dst
		else:
			return iter(branch(src),  leaf(src) + dst)
	return iter(input_list, [])

