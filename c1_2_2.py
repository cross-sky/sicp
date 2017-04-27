def countCharge(amount):
	def coinValue(kindOfCount):
		if kindOfCount == 5:
			return 50
		elif kindOfCount == 4:
			return 25
		elif kindOfCount == 3:
			return 10
		elif kindOfCount == 2:
			return 5
		elif kindOfCount == 1:
			return 1
	def cc(amount, kindOfCount):
		if amount == 0:
			return 1
		elif amount < 0 or kindOfCount == 0:
			return 0
		else:
			return cc(amount, kindOfCount - 1) + cc(amount - coinValue(kindOfCount), kindOfCount)
	return cc(amount, 5)