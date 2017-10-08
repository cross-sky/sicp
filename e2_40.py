from c2_2_3b import maps
from c2_2_3c import flatmap
from operator import add

def unique_pairs(n):
	return flatmap(lambda i: maps(lambda j: add([i], [j]), 
									range(1, i)),
						range(1, n + 1))

