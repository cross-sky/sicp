import sys
sys.setrecursionlimit(10000)
from ucb import trace
from operator import mul

def product_recu(term, a, next, b):
	if a > b:
		return 1
	else:
		return term(a) * product_recu(term, next(a), next, b)
def square(x):
	return x * x

def product_iter(term, a, next, b):
	def iter(a, result):
		if a > b:
			return result
		else:
			return iter(next(a), term(a) * result)
	return iter(a, 1)

def accumulate(combiner, null_value, term, a, next, b):
	def inner(a):
		if a > b:
			return null_value
		else:
			return combiner(term(a), inner(next(a)))
	return inner(a)

def factorial_recu(a, b):
	def term(x):
		return x
	def next(x):
		return x + 1
	return accumulate(mul, 1, term, a, next, b)


