import sys
sys.setrecursionlimit(10000)
from ucb import trace

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

def factorial_recu(a, b):
	def term(x):
		return x
	def next(x):
		return x + 1
	return product_recu(term, a, next, b)

def factorial_iter(a, b):
	def term(x):
		return x
	def next(x):
		return x + 1
	return product_iter(term, a, next, b)

def pi_recu(n):
	def term(x):
		return x * (x + 2) / square(x + 1)
	def next(x):
		return x + 2
	return product_recu(term, 2, next, n) * 4

def pi_iter(n):
	def term(x):
		return x * (x + 2) / square(x + 1)
	def next(x):
		return x + 2
	return product_iter(term, 2, next, n) * 4

