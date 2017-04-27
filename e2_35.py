from c2_2_3b import *
def count_leaves(seque):
	"""fail.. can not do this
(define (count-leaves t)
  (accumulate +
              0 
              (map (lambda (sub-t)
                     (if (pair? sub-t) 
                       (count-leaves sub-t) 1))
                   t)))

    actualy it could done
    compare s would be a int or a list
	"""
	return accumulate(add, 0, maps(lambda s: 1 if type(s) == int else count_leaves(s), seque))