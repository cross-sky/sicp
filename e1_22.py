import time
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

def odd(n):
	return n % 2 == 0

def next_odd(n):
	if odd(n):
		return n + 1
	else:
		return n + 2

def timed_prime_test(n):
	print("\r\n")
	print(n)
	start_prime_test(n, time.time())

def start_prime_test(n, start_time):
	if prime(n):
		report_prime(time.time() - start_time)

def report_prime(n):
	print("***")
	print(n)

def continue_prime(n, times):
	if times == 0:
		return
	if prime(n):
		print(n)
		continue_prime(next_odd(n), times - 1)
	else:
		continue_prime(next_odd(n), times)

def search_prime(n):
	print("primes:")
	start_time = time.time()
	continue_prime(n, 3)
	end_time = time.time()
	print(end_time - start_time)