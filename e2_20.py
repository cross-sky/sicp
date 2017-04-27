def same_parity(*arg):
	assert(arg),'arg is null'
	print(arg)
	m = list(arg)
	n = m[0] % 2
	return [i for i in m if (i % 2 == n) ]