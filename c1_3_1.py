def sum(term, a, next, b):
	if a > b:
		return 0
	else:
		return term(a) + sum(term, next(a), next, b)

def pi_sum(a, b):
	def pi_term(x):
		return 1/(x * (x + 2))
	def pi_next(x):
		return x + 4
	return sum(pi_term, a, pi_next, b)

def integral(f, a, b, dx):
	def add_dx(x):
		return x + dx
	return sum(f, (a + dx / 2), add_dx, b) * dx

