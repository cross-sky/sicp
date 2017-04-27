def pascal_1(row, col):
	def pascal_1_iter(row, col):
		if row == col or col == 0:
			return 1
		else:
			return pascal_1_iter(row - 1, col - 1) + pascal_1_iter(row - 1, col)
	return pascal_1_iter(row, col)


def pascal_2(row, col):

	def fact_iter(product, n, max):
		if n > max:
			return product
		else:
			return fact_iter(product * n, n + 1, max)
	def factorial(n):
		return fact_iter(1, 1, n)
	return factorial(row) // (factorial(col) * factorial(row - col))