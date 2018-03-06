import math
import numpy

matrix = numpy.zeros((640, 480), dtype=numpy.ndarray)

d = 4
e = [2, -2, 3]
left = -10
right = 10
top = 5
bottom = -5

e_module = math.sqrt(math.pow(e[0], 2) + math.pow(e[1], 2) + math.pow(e[2], 2))
w = [e[0] / e_module, e[1] / e_module, e[2] / e_module]

t_min_index = 0
t_min = 0

for index, value in enumerate(w):
    if (t_min > abs(value)):
        t_min_index = index

t = w[:]
t[t_min_index] = 1

wxt = numpy.cross(t, w)

u = wxt / math.sqrt(math.pow(wxt[0], 2) + math.pow(wxt[1], 2) + math.pow(wxt[2], 2))

v = numpy.cross(u, w)

for index, pixel in numpy.ndenumerate(matrix):

    U = left + (right - left) * (index[0] + 0.5)
    V = bottom + (top - bottom) * (index[1] + 0.5)

    matrix[index[0]][index[1]] = (U, V)

print(matrix)
