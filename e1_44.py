dx = 0.0001

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

def averag(f1, f2, f3):
	return (f1 + f2 + f3) / 3

def smooth(f):
	return lambda x: averag(f(x - dx), f(x), f(x + dx))

def n_smooth(f, n):
	r = repeate3(smooth, n)
	return r(f)