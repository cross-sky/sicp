from e2_40 import unique_pairs
from c2_2_3c import flatmap
from c2_2_3b import *
from c2_2_3a import filters

def unique_triples(n):
	return flatmap(lambda i: maps(lambda j: cons(i, j),
										unique_pairs(i - 1)),
						range(1, n + 1))


def triple_sum_equal(sums, triple):
	return sums == sum(triple)

def remove_triples_not_equal_to(sums, triple):
	return filters(lambda cur: triple_sum_equal(sums, cur), triple)

def triples(x, n):
	return remove_triples_not_equal_to(x, unique_triples(n))