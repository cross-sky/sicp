def cons(x, y):
	"""s = list([x]) + list([y])"""
	return [x] + list(y)

def car(x):
	return x[0]

def cdr(x):
	return x[1:]

def cadr(x):
	return x[1]

def caddr(x):
	return x[2]

def cadddr(x):
	return x[3]