def square(x):
	return x * x

def fast_expt(b, n):
	def even(x):
		return x % 2 == 0
	def iter(b, n, product):
		if n == 0:
			return product
		if even(n):
			return iter(square(b), n // 2, product)
		else:
			return iter(b, n - 1, product * b)

	return iter(b, n, 1)