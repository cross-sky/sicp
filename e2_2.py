def make_segment(start_segment, end_segment):
	return cons(start_segment, end_segment)

def start_segment(seg):
	return car(seg)

def end_segment(seg):
	return cdr(seg)

def make_point(x, y):
	return cons(x, y)

def x_point(p):
	return car(p)

def y_point(p):
	return cdr(p)

def midpoint_segment(seg):
	start = start_segment(seg)
	end = end_segment(seg)
	return make_point(average(x_point(start), x_point(end)), average(y_point(start), y_point(end)))