from alice import *
from ucb import trace

def odd(x):
	return x % 2

@trace
def filters(predicate, sequence):
	if len(sequence) < 1:
		return []
	if predicate(car(sequence)):
		return cons(car(sequence), filters(predicate, cdr(sequence)))
	else:
		return filters(predicate, cdr(sequence))

