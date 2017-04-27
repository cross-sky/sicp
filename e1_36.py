tolerance = 0.0001

import time
import math 
def fixed_point(f, first_guess):
	def close_enough(v1, v2):
		return abs(v1 - v2) < tolerance
	def trys(guess):
		next = f(guess)
		if close_enough(guess, next):
			return next
		else:
			return trys(next)
	return trys(first_guess)
	
def average(x, y):
	return (x + y) / 2

def logs():
	ftime = time.time()
	print(fixed_point(lambda x: math.log(1000) / math.log(x), 2))
	etime = time.time()
	print(etime - ftime)

def log_a():
	def fuma():
		return lambda x: 3 / math.log(x)
	def fuma_aver(f):
		return lambda x: average(x, f(x))

	ftime = time.time()
	print(fixed_point(fuma_aver(lambda x: math.log(1000) / math.log(x)), 2))
	etime = time.time()
	print(etime - ftime)

	