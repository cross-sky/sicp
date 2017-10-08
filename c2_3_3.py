from alice import *

def element_of_set(x, sets):
	if len(sets) == 0:
		return False
	elif car(sets) == x:
		return True
	else:
		return element_of_set(x, cdr(sets))

def adjoin_set(x, sets):
	if element_of_set(x, sets):
		return sets
	else:
		return cons(x, sets)

def intersection_set(set1, set2):
	if len(set1) == 0 or len(set2) == 0:
		return []
	elif element_of_set(car(set1), set2):
		return cons(car(set1), intersection_set(cdr(set1), set2))
	else:
		return intersection_set(cdr(set1), set2)

def union_set(set1, set2):
	def iters(inputs, result):
		if len(inputs) == 0:
			return result
		else:
			cur_e = car(inputs)
			remain_e = cdr(inputs)
			if element_of_set(cur_e, result):
				return iters(remain_e, result)
			else:
				return iters(remain_e, cons(cur_e, result))
	return iters(set1 + set2, [])
