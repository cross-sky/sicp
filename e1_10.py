def ack(x, y):
	if y == 0:
		return 0
	elif x == 0:
		return 2 * y
	elif y == 1:
		return 2
	else:
		return ack(x - 1, ack(x, y - 1))