from alice import *
from e2_47 import *

def make_vect(x, y):
	return [x, y]

def xcor_vert(v):
	return v[0]

def ycor_vert(v):
	return v[1]


def add_vect(v1, v2):
	return make_vect(xcor_vert(v1) + xcor_vert(v2), ycor_vert(v1) + ycor_vert(v2))

def sub_vect(v1, v2):
	return make_vect(xcor_vert(v1) - xcor_vert(v2), ycor_vert(v1) - ycor_vert(v2))

def scale_vect(factor, vect):
	return make_vect(factor*xcor_vert(vect), factor * ycor_vert(vect))

def frame_coord_map(frame):
	def fun(v):
		return add_vect(origin_frame(frame),
							add_vect(scale_vect(xcor_vert(v), edge1_frame(frame)),
										scale_vect(ycor_vert(v), edge2_frame(frame))))
	return fun