from ucb import trace

@trace
def cons(x, y):
	return lambda m: m(x, y)

@trace
def car(z):
	return z(lambda p, q: p)

@trace
def cdr(z):
	return z(lambda p, q: q)

"""
car (cons(x, y))
-->car(lambda m: m(x, y))
-->(lambda m: m(x, y))(lambda p, q: p)
-->(lambda p, q: p)(x, y)
-->(lambda x, y: x)
-->x

-->lambda x, y: x
-->(lambda p, q: p)(x, y)
-->(lambda m: m(x, y))(lambda p, q: p)
-->
-->f(lambda p, q: p)
-->car(z)
	return z(lambda p, q: p)
-->cons(x, y)
	return lambda m:(x, y)
-->car(cons(x, y))

"""