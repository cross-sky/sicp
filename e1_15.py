from ucb import trace
def cube(x):
	return x * x * x
def p(x):
	return 3 * x - 4 * cube(x)

@trace
def sine(angle, n = 0):
	if abs(angle) < 0.1:
		print(n)
		return angle
	else:
		return p(sine (angle / 3.0, n + 1))