def add_rat(x, y):
	return make_ret((numer(x) * denom(y) + numer(y) * denom(x)), denom(x) * denom(y))

def sub_rat(x, y):
 	return make_ret((numer(x) * denom(y) - numer(y) * denom(x)), denom(x) * denom(y)) 

def mul_rat(x, y):
 	return make_ret(numer(x) * numer(y), denom(x) * denom(y))

def div_rat(x, y):
	return make_ret(numer(x) * denom(y), denom(x) * numer(x))

def equal_rat(x, y):
	return numer(x) * denom(y) == numer(y) * denom(x)

