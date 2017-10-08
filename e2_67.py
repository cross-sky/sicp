from c2_3_4 import *

def sample_tree():
	return make_code_tree(make_leaf("A", 4), 
		make_code_tree(make_leaf("B", 2), 
			make_code_tree(make_leaf("D", 1), make_leaf("C", 1))))

def sample_message():
	return [0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0]