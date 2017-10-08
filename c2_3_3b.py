from alice import *

def element_of_set(x, set):
	if len(set) == 0:
		return False
	elif car(set) == x:
		return True
	elif car(set) < x:
		return False
	else:
		return element_of_set(x, cdr(set))


def intersection_set(set1, set2):
	if len(set1) == 0 or len(set2) == 0:
		return []
	else:
		x1 = car(set1)
		x2 = car(set2)
		if x1 == x2:
			return cons(x1, intersection_set(cdr(set1), cdr(set2)))
		elif x1 < x2:
			return intersection_set(cdr(set1), set2)
		else:
			return intersection_set(set1, cdr(set2))

def adjoin_set(x, set):
	if len(set) == 0:
		return [x]
	else:
		cur_e = car(set)
		if cur_e == x:
			return set
		elif cur_e < x:
			return cons(cur_e, adjoin_set(x, cdr(set)))
		else:
			return cons(x, set)

def union_set(set1, set2):
	def iters(set1, set2, result):
		if len(set1) == 0 or len(set2) == 0:
			return result + set1 + set2
		else:
			x1 = car(set1)
			x2 = car(set2)
			if x1 == x2:
				return iters(cdr(set1), cdr(set2), result + [x1])
			elif x1 < x2:
				return iters(cdr(set1), set2, result + [x1])
			else:
				return iters(set1, cdr(set2), result + [x2])
	return iters(set1, set2, [])

