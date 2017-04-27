us_coins = list([50, 25, 10, 5, 1])

def cc(amount, coin_values):
	if amount == 0:
		return 1
	elif amount < 0 or no_more(coin_values):
		return 0
	else:
		return cc(amount, except_first_denomination(coin_values)) + \
		cc(amount - first_denomination(coin_values), coin_values)

def no_more(values):
	return not values

def except_first_denomination(values):
	return values[1:]
def first_denomination(values):
	return values[0]
