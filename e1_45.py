import sys   
sys.setrecursionlimit(1000000)

toerance = 0.001

def close_enough(x1, x2):
	return abs(x1 - x2) < toerance

def fixed_point(f, first_guess):
	def trys(guess):
		next = f(guess)
		if close_enough(guess,next):
			return next
		else:
			return trys(next)
	return trys(first_guess)

def average(x, y):
	return (x + y) / 2

def average_damp(f):
	return lambda x: average(x, f(x))

def compose(f, g):
	return lambda x:f(g(x))

def repeate(f, n):
	def iter(i, fs):
		if i == 1:
			return fs #........fs
		else:
			return iter(i - 1, compose(f, fs))
	return iter(n, f)

def even(n):
	return n % 2 == 0

def square(x):
	return x * x


def fast_expt(b, n):
	
	if n == 0:
		return b
	if even(n):
		return square(fast_expt(b, n // 2))
	else:
		return b * fast_expt(b, n - 1)

#平均阻尼震荡?????????

def average_damp_n(f, n):
	return repeate(average_damp(f), n)

def af(n, times, x):
	return	fixed_point(
						average_damp(
							repeate(lambda y: x / fast_expt(y, n-2), 
								times)), 
						1.0)

def ag(n, times):
	return lambda x: fixed_point(average_damp_n(lambda y: x / fast_expt(y, n - 2),
												times),
								1.0)
