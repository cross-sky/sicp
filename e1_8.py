def cube_iter(preGuess, guess, x):

	def goodEnough(preGuess, guess):
		return abs(preGuess - guess) < 0.001
	def squart(x):
		return x * x
	def avarage(x, y):
		return (x + 2 * y) / 3
	def improveGuess(guess, x):
		return avarage(x / squart(guess), guess)

	if (goodEnough(preGuess, guess)):
		return guess
	else:
		return cube_iter(guess, improveGuess(guess, x), x)

def cube(x):
	return cube_iter(0, 1.0, x)