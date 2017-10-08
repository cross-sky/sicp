from alice import *
def memq(item, x):
	if x == []:
		return False
	elif item == car(x):
		return x
	else:
		return memq(item, cdr(x))