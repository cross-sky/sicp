
def cont_re(N, D, k):
	def cf(i):
		if i >= k:
			return N(k) / D(k)
		else:
			return N(i) / (D(i) + cf(i+1))
	return cf(1)

def di_cont(x):
	return 2 * x + 1

def test1(x):
	return 2 + cont_re(lambda x:1,
				di_cont,
				x)
def square(x):
	return x * x

def cont_it(N, D, k, x):
	def itor(i, result):
		if i == 0:
			return result
		else:
			return itor(i - 1, N(i) * square(x) / (D(i) - result))

	return itor(k - 1, N(k) * square(x) / D(k))

def test2(x, k):
	return cont_it(lambda x:1,
						di_cont,
						k,
						x) / x

