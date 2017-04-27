def squart_iter(guess, x):
	def square(x):
		return x * x

	def goodEnough(guess, x):
		return abs(square(guess) - x) < 0.001

	def improve(guess, x):
		return average(guess, x / guess)
	def average(x, y):
		return (x + y) / 2

	if(goodEnough(guess,x)):
		return guess
	else:
		return squart_iter(improve(guess, x),x)

def sqrt(x):
	"""Sqrt of X
	#>>> sqrt()
	"""
	return squart_iter(1.0, x)