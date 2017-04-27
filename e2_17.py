def last_pair(input_list):
	if not input_list[1:]:
		return input_list[0]
	else:
		return last_pair(input_list[1:])