import sys
sys.setrecursionlimit(10000)
from ucb import trace
def sum(term, a, next, b):
	if a > b:
		return 0
	else:
		return term(a) + sum(term, next(a), next, b)
#@trace
def simpson(f, a, b, n):
	def even(x):
		return x % 2 == 0
	def factor(k):
		if k == 0 or k == n:
			return 1
		if even(k):
			return 2
		else:
			return 4
	def sim_term(k):
		return factor(k) * fun(k)
	def fun(k):
		return f(a + k * h)
	def next(k):
		return k + 1

	h = (b - a) / n
	if not even(n):
		return "n can not be odd"
	return sum(sim_term, fun(0), next, n) * h / 3

def sp(a, b, n):
	def  cube(x):
		return x * x * x
	return simpson(cube, a, b, n)