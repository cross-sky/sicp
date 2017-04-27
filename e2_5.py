""" 复合数据的构成方式和解析方式"""


def cons(a, b):
	return pow(2, a) * pow(3, b)
def iters(x, n, result):
	if x % n == 0:
		return iters(x // n, n, result + 1)
	else:
		return result

def car(x):
	return iters(x, 2, 0)

def cdr(x):
	return iters(x, 3, 0)