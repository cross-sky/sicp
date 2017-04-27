
def cont_re(N, D, k):
	def cf(i):
		if i >= k:
			return N(k) / D(k)
		else:
			return N(i) / (D(i) + cf(i+1))
	return cf(1)

def di_cont(x):
	def is3n(x):
		return (x + 1) % 3 == 0
	if is3n(x):
		return 2 * (x + 1) // 3
	else:
		return 1

def test1(x):
	return 2 + cont_re(lambda x:1,
				di_cont,
				x)

def cont_it(N, D, k):
	def itor(i, result):
		if i == 0:
			return result
		else:
			return itor(i - 1, N(i) / (D(i) + result))

	return itor(k - 1, N(k) / D(k))

def test2(x):
	return 2 + cont_it(lambda x:1,
						di_cont,
						x)

