def squart_iter(preGuess, guess, x):
	def square(x):
		return x * x

	def goodEnough(preGuess, guess):
		return abs(preGuess - guess) < 0.001

	def improve(guess, x):
		return average(guess, x / guess)
	def average(x, y):
		return (x + y) / 2

	if(goodEnough(preGuess,guess)):
		return guess
	else:
		return squart_iter(guess, improve(guess, x), x)

def sqrt(x):
	"""Sqrt of X
	#>>> sqrt()
	"""
	return squart_iter(0, 1.0, x)