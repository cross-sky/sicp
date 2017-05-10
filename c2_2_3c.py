from c2_2_3b import *
from operator import add
from c1_2_6B import fast_prime
from c2_2_3a import filters
from ucb import trace

#@trace
def flatmap(proc, seq):
	return accumulate(add, [], maps(proc, seq))

#@trace
def prime_sum(pair):
	return fast_prime(car(pair) + pair[1], 3)

def make_pair_sum(pair):
	return add([car(pair)], cdr[pair], [car(pair) + pair[1]])

#@trace
def prime_sum_pairs(n):
	return maps(make_pair_sum(
					filters(prime_sum(
								flatmap(
									lambda i: maps(lambda j: add([i], [j]),
													range(1, i - 1)),
									range(1, n))))))

