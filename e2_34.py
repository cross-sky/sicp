from c2_2_3b import *

def horner(x, sequence):
	"""x"""
	return accumulate(lambda this_coeff, higher_terms: this_coeff + x * higher_terms, 
		0, sequence)
