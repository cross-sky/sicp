
def square(x):
	return x * x

def compose(f, g):
	return lambda x:f(g(x))

def inc(x):
	return x + 1