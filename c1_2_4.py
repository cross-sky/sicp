def expt1(b, n):
	def expt_iter(b, counter, product):
		if counter == 0:
			return product
		else:
			return expt_iter(b, counter - 1, b * product)
	return expt_iter(b, n, 1)

def square(x):
	return x * x

def expt2(b, n):
	def even(n):
		return n % 2 == 0
	if n == 0:
		return 1
	if even(n):
		return square(expt2(b, n//2))
	else:
		return b * expt2(b, n-1)