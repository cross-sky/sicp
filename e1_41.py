from ucb import trace
@trace
def double(f):
	return lambda x: f(f(x))

def inc(x):
	return x + 1