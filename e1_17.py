def double(x):
	return x + x

def halve(x):
	return x / 2

def event(x):
	return x % 2 == 0

	
def multi(a, b):
	if b == 0:
		return 0
	if event(b):
		return double(multi(a, b // 2))
	else:
		return a + multi(a, b - 1)