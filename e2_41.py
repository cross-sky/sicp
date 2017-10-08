from c2_2_3b import *
from operator import add
from c2_2_3c import flatmap
from alice import *
from c2_2_3a import filters

"""
add(add([i], [j]), [k])

"""

def three_pairs(n):
	return flatmap(lambda i: maps(lambda j: maps(lambda k: list([i] + [j] + [k]),
													range(1, j)),
										range(1, i )),
						range(1, n // 2 + 1))

def make_threep_sum(pair):
	return list([pair[0]] + [pair[1]] + [pair[2]] + [sum(pair)])

def sum_equal(pair, n):
	return sum(pair) == n


"""def flat(result, sequence):
	if len(sequence) < 1:
		return result
	else:
		if car(sequence) == []:
			return flat(result, cdr(sequence))
		if len(car(sequence)) == 1:
			return flat(result + car(sequence), cdr(sequence))
		else:
			return flat(result + car(sequence), [cdr(car(sequence))])"""

@trace
def flat(sequence):
	if len(sequence) < 1:
		return []
	if type(car(sequence)) == int and len(sequence) == 3:
		return [sequence]
	else:
		return add(flat(car(sequence))  , flat(cdr(sequence)))

def thre_equal(n):
	return maps(make_threep_sum,
					filters(lambda i: 1 if (sum(i) == n) else 0, 
								flat(three_pairs(n))))

def remove(item, sequence):
	return filters(lambda x: 1 if item != x else 0, sequence)

