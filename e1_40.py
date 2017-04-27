from c1_3_3b import *

def deriv(g):
	return lambda x: (g(x + dx) - g(x)) / dx

def cube(x):
	return x * x * x

dx = 0.001

def newton_transform(g):
	return lambda x: x - g(x) / deriv(g)(x)

def newton_method(g, guess):
	return fixed_point(newton_transform(g), guess)

def squre(x):
	return x * x

def sqrts(x):
	return newton_method(lambda y: squre(y) - x, 1.0 )

def fpt(g, transform, guess):
	return fixed_point(transform(g), guess)

def cube(x):
	return x * x * x
def cubic(a, b, c):
	return lambda x: cube(x) + a * squre(x) + b * x + c

