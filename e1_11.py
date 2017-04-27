def sum_three1(x):
	def sum_three_iter(x):
		if x < 3:
			return x
		else:
			return sum_three_iter(x-1) + 2 *sum_three_iter(x - 2) + 3 * sum_three_iter(x -3)
	return sum_three_iter(x)


def sum_three2(x):
	def sum_thre2_iter(x_1, x_2, x_3, count):
		if count < 3:
			return count
		else:
			sums = x_1 + 2 * x_2 + 3 * x_3
			if count == 3:
				return sums
			else:
				return sum_thre2_iter(sums, x_1, x_2, count - 1)
	return sum_thre2_iter(2, 1, 0, x)


def sum_three3(x):
	def sum_three3_iter(a, b, c, i, n):
		if i == n:
			return c
		else:
			return sum_three3_iter(a+2*b+3*c, a, b, i+1, n)
	return sum_three3_iter(2, 1, 0, 0, x)
