from e2_69 import *
from e2_68 import *

t70 = [['A', 2], ['NA', 16], ['BOOM', 1], ['SHA', 3], ['GET', 2], ['YIP', 9], ['JOB', 2], ['WAH', 1]]

t_hf = generate_huffman_tree(t70)
t_m1 = ['GET', 'A', 'JOB']
r_m1 = encode(t_m1, car(t_hf))
e_m1 = decode(r_m1, car(t_hf))


print(t_m1 == e_m1)
