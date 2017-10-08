from alice import *
from c2_3_3c import *
from ucb import trace

def list_tree(element):
	return car(partical_tree((element), len(element)))

@trace
def partical_tree(elts, n):
	if n == 0:
		return cons([], elts)
	else:
		left_size = (n - 1) // 2
		left_result = partical_tree(elts, left_size)
		left_tree = car(left_result)
		non_left_elts = cdr(left_result)
		right_size = n - (left_size + 1)
		this_entry = car(non_left_elts)
		right_result = partical_tree(cdr(non_left_elts), right_size)
		right_tree = car(right_result)
		remaining_elts = cdr(right_result)
		return cons(make_tree(this_entry, left_tree, right_tree), remaining_elts)

lt = [1, 3, 5, 7, 9, 11]
list_tree(lt)