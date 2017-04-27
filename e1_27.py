def even(x):
	return x % 2 == 0
def square(x):
	return x * x
def expmod(base, exp, m):
	if exp == 0:
		return 1
	if even(exp):
		return square(expmod(base, exp // 2, m)) % m
	else:
		return base * expmod(base, exp - 1, m) % m


def is_prime(n):
	def searcch(a, n):
		if a >= n:
			return True
		if congruent(a, n):
			return searcch(a + 1, n)
		else:
			return False

	def congruent(a, n):
		return expmod(a, n, n) == a

	return searcch(2, n)

