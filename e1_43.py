
def square(x):
	return x * x

def compose(f, g):
	return lambda x:f(g(x))

def repeate2(f, n):
	if n == 1:
		return f
	else:
		return compose(f, repeate2(f, n - 1))

def repeate3(f, n):
	def iter(i, result_f):
		if i == 1:
			return result_f
		else:
			return iter(i - 1, compose(f, result_f))
	return iter(n, f)

def repeated(f, n):
	def inner(x):
		return rp(n, f(x))
	def rp(n, result):
		if n == 1:
			return result
		else:
			return rp(n - 1, f(result))

	return inner