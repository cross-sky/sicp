tolerance = 0.0001

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
	