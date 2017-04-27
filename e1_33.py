import sys
sys.setrecursionlimit(10000)
from ucb import trace
from operator import *
from e1_23 import prime

def product_recu(term, a, next, b):
	if a > b:
		return 1
	else:
		return term(a) * product_recu(term, next(a), next, b)

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

def filt_accumulate(combiner, null_value, term, a, next, b, valid):
	if a > b:
		return null_value
	rest_term = filt_accumulate(combiner, null_value, term, next(a), next, b, valid)
	if valid(a):
		return combiner(term(a), rest_term)
	else:
		return rest_term

def filt_t(a, b):
	def term(x):
		return x
	def next(x):
		return x + 1
	return filt_accumulate(add, 0, term, a, next, b, prime)

def filt_accumulate_iter(combiner, null_value, term, a, next, b, valid):
	def inner(a, result):
		if a > b:
			return result
		if valid(a):
			return inner(next(a), result + term(a))
		else:
			return inner(next(a), result)
	return inner(a, 0)

def filt_t_iter(a, b):
	def term(x):
		return x
	def next(x):
		return x + 1
	return filt_accumulate_iter(add, 0, term, a, next, b, prime)

