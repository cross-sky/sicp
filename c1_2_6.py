def divides(a, b):
	return b % a == 0
def smallest_divisor(n):
	return find_divisor(n, 2)

def square(n):
	return n * n
def find_divisor(n, test_divisor):
	if square(test_divisor) > n:
		return n

	if divides(test_divisor, n):
		return test_divisor
	else:
		return find_divisor(n, test_divisor + 1)

def prime(n):
	return n == smallest_divisor(n)
