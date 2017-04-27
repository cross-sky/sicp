def positive(x):
	return x > 0
def negtive(x):
	return x < 0
def average(x, y):
	return (x + y) / 2
def close_enough(x, y):
	return abs(x - y) < 0.001


def search(f, neg_point, pos_point):
	mid_point = average(neg_point, pos_point)
	if close_enough(neg_point, pos_point):
		return mid_point
	test_value = f(mid_point)
	if positive(test_value):
		return search(f, neg_point, mid_point)
	if negtive(test_value):
		return search(f, mid_point, pos_point)
	else:
		return mid_point

def half_method(f, a, b):
	a_value = f(a)
	b_value = f(b)

	if (negtive(a_value) and positive(b_value)):
		return search(f, a, b)
	if (negtive(b_value) and positive(a_value)):
		return search(f, b, a)
	else:
		print("Values are not of opposite sign ")