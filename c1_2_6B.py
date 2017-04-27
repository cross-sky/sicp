import random
import time
from ucb import trace
def even(n):
	return n % 2 == 0

def square(x):
	return x * x

#数的幂对另一个数取模的结果
#@trace
def expmod(base, exp, m):
	if exp == 0:
		return 1
	if even(exp):
		return square(expmod(base, exp // 2, m)) % m
	else:
		return (base * expmod(base, exp - 1, m)) % m

#@trace
def fermat_test(n):
	def try_it(a):
		return expmod(a, n, n) == a		#随机数幂次方取模
	return try_it(random.randint(1, n - 1) + 1)  #生成随机数

#@trace
def fast_prime(n, times):
	if times == 0:
		return True
	if fermat_test(n):
		return fast_prime(n, times - 1)
	else:
		return False

def continue_prime(n, times):
	if times == 0:
		return
	if fast_prime(n, 2):
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

def odd(n):
	return n % 2 == 0

def next_odd(n):
	if odd(n):
		return n + 1
	else:
		return n + 2