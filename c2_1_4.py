def add_interval(x, y):
	return make_interval(low_bound(x) + low_bound(y), upper_bound(x) + upper_bound(y))

def mul_interval(x, y):
	p1 = low_bound(x) * low_bound(y)
	p2 = low_bound(x) * upper_bound(y)
	p3 = upper_bound(x) * low_bound(y)
	p4 = upper_bound(x) *upper_bound(y)
	return make_interval(min(p1, p2, p3, p4), max(p1, p2, p3, p4))

def div_interval(x, y):
	if low_bound(y) * upper_bound(y) < 0:
		assert(0),"Div 0: "
	return mul_interval(x, make_interval(1 / upper_bound(y), 1 / low_bound(y)))

def make_interval(x, y):
	return cons(x, y)

def cons(x, y):
	def dispach(m):
		if m == 0:
			return x
		else:
			return y
	return dispach

def low_bound(x):
	return x(0)

def upper_bound(x):
	return x(1)

def sub_interval(x, y):
	"""return make_interval(low_bound(x) - upper_bound(y), upper_bound(x) - low_bound(y))"""
	return add_interval(x, make_interval(-upper_bound(y), -low_bound(y)))

def make_center_width(c, w):
	return make_interval(c - w, c + w)

def center(i):
	return (low_bound(i) + upper_bound(i)) / 2

def  width(i):
	return (upper_bound(i) - low_bound(i)) / 2

def make_center_percent(cen, per):
	return make_interval(cen - cen * 100 / per, cen + cen * 100 / per)

def percent(x):
	return abs(width(x) * 100 / center(x))
