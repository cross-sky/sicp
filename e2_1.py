def make_rat(n, d):
	if d < 0:
		return cons(-n, -d)
	else:
		return cons(n, d)

def cons(x, y):
	def dispatch(m):
		if m == 0:
			return x
		if m == 1:
			return y
		else:
			assert(0),"argument not 0 or 1"
	return dispatch

def car(z):
	return z(0)

def cdr(z):
	return z(1)

