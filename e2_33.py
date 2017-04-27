from c2_2_3b import *
from ucb import trace
@trace
def map(p, sequence):
	""" 
	>>> map(abs, [-1, 2, -3])
	>>> [1, 2, 3]
	"""
	return accumulate(lambda x, y: cons(p(x), y), [], sequence)

def append(seq1, seq2):
	"""append accumulate"""
	return accumulate(cons, seq2, seq1)

def length(sequence):
	return accumulate(lambda x, y: 1 + y, 0, sequence)