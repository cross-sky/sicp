
def cont_re(N, D, k):
	def cf(i):
		if i >= k:
			return N(k) / D(k)
		else:
			return N(i) / (D(i) + cf(i+1))
	return cf(1)

def test1(x):
	return 1 + cont_re(lambda x:1,
				lambda x: 1,
				x)

def cont_it(N, D, k):
	def itor(i, result):
		if i > k:
			return result
		else:
			return itor(i + 1, N(i) / (D(i) + result) )

	return itor(1, N(1) / D(1))

def test2(x):
	return 1 + cont_it(lambda x:1,
						lambda x: 1,
						x)

