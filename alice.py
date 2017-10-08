def cons(x, y):
	"""s = list([x]) + list([y])"""
	return [x] + list(y)

def car(x):
	return x[0]

def cdr(x):
	return x[1:]