def zero():
	return lambda f: lambda x: x

def add_1(n):
	return lambda f: lambda x: f(n(f)(x))

def one():
	return lambda f: lambda x: f(x)

def two():
	return lambda f: lambda x: f(f(x))

"""
add_1(zero)
-->lambda f: lambda x: f((lambda f: lambda x:x)(f)(x))
-->lambda f: lambda x: f((lambda x:x)(x))
-->lambda f: lambda x: f(x)

what's the meaning of it
"""