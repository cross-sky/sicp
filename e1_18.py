def double(x):
	return x + x

def halve(x):
	return x / 2

def event(x):
	return x % 2 == 0

def fast_mul(a, b):
	def fast_mul_iter(a, b, product):
		if b == 0:
			return product
		if event(b):
			return fast_mul_iter(double(a), b // 2, product)
		else:
			return fast_mul_iter(a, b - 1, product + a)

	return fast_mul_iter(a, b, 0)
	