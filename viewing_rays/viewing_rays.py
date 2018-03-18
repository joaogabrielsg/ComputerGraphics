import math
import numpy
from vector import Vector
from PIL import Image

# matrix = numpy.zeros((640, 480), dtype=numpy.ndarray)

d = 4
e = [2, -2, 3]

spheres = [{"color": (100, 100, 100), "raio": 1, "center": (0, 0, 0)},
           {"color": (250, 250, 250), "raio": 2, "center": (2, -2, 2)}]

image = []

left = -10
right = 10
top = 5
bottom = -5


#
# e_module = math.sqrt(math.pow(e[0], 2) + math.pow(e[1], 2) + math.pow(e[2], 2))
# w = [e[0] / e_module, e[1] / e_module, e[2] / e_module]
#
# t_min_index = 0
# t_min = 0
#
# for index, value in enumerate(w):
#     if (t_min > abs(value)):
#         t_min_index = index
#
# t = w[:]
# t[t_min_index] = 1
#
# wxt = numpy.cross(t, w)
#
# u = wxt / math.sqrt(math.pow(wxt[0], 2) + math.pow(wxt[1], 2) + math.pow(wxt[2], 2))
#
# v = numpy.cross(u, w)
#
# for index, pixel in numpy.ndenumerate(matrix):
#
#     U = left + (right - left) * (index[0] + 0.5)
#     V = bottom + (top - bottom) * (index[1] + 0.5)
#
#     direction = (v[0] * V, v[1] * V, v[2] * V)
#
#     direction = (direction[0] + (u[0] * U), direction[1] + (u[1] * U), direction[2] + (u[2] * U))
#
#     product_d_w = (w[0] * d, w[1] * d, w[2] * d)
#
#     direction = (direction[0] - product_d_w[0], direction[1] - product_d_w[1], direction[2] - product_d_w[2])
#
#     # - calcular o delta e ver se é igual
#
#     smaller_T = None
#     color = (0, 0, 0)
#
#     for sphere in spheres:
#         c = sphere["center"]
#         r = sphere["raio"]
#
#         subtraction_e_c = (e[0] - c[0], e[1] - c[1], e[2] - c[2])
#
#         delta = ((subtraction_e_c[0] * (2 * d)),
#                  (subtraction_e_c[1] * (2 * d)),
#                  (subtraction_e_c[2] * (2 * d)))
#
#         delta = numpy.dot(delta, delta)
#
#         delta -= 4 * (d * d) * ((numpy.dot(subtraction_e_c, subtraction_e_c)) - (r * r))
#
#     # - com o delta determinar o t
#
#         if (delta >= 0):
#             T = ((subtraction_e_c[0] * d),
#                  (subtraction_e_c[1] * d),
#                  (subtraction_e_c[2] * d))
#
#             T = numpy.dot(T, T)
#
#             T -= 4 * (d * d) * ((numpy.dot(subtraction_e_c, subtraction_e_c)) - (r * r))
#
#
#             T = ((((-d) * subtraction_e_c[0]) - math.sqrt(-T)) / (d * d),
#                  (((-d) * subtraction_e_c[1]) - math.sqrt(-T)) / (d * d),
#                  (((-d) * subtraction_e_c[2]) - math.sqrt(-T)) / (d * d))
#
#             print(T)
#
#             # Preciso calcuclar o raio para comparar
#             # problema: o raio (P(t)) é um vetor e nao um numero
#             if T > smaller_T:
#                 smaller_T = T
#                 color = sphere["color"]
#
#
#     image.append(color)
#
#     image_out = Image.new("RGBA", (640, 480))
#     image_out.putdata(image)
#
#     image_out.show()


# - com o t determinar o raio P(t)


# matrix[index[0]][index[1]] = (direction, e)

# print(matrix)

class Ray():

    def __init__(self, point_e, distance, top, bottom, right, left):

        self.point_e = Vector(point_e)

        self.distance = distance
        self.top = top
        self.bottom = bottom
        self.right = right
        self.left = left

        self.w = Vector(point_e)

        self.t = self.w.non_collinear_vector()

        self.u = Vector(numpy.cross(self.w.vector, self.t.vector)).unit_vector()

        self.v = Vector(numpy.cross(self.w.vector, self.u.vector))

    def perspective_projection(self, row, column):
        matrix = numpy.zeros((row, column), dtype=numpy.ndarray)

        for index, pixel in numpy.ndenumerate(matrix):
            U = self.left + (self.right - self.left) * (index[0] + 0.5) / row
            V = self.bottom + (self.top - self.bottom) * (index[1] + 0.5) / column

            direction_v = self.v.multiply_by_number(V)

            direction_u = self.u.multiply_by_number(U)

            direction_w = self.w.multiply_by_number(d)

            direction = direction_u.sum_by_vector(direction_v)

            direction = direction.subtract_by_vector(direction_w)

            matrix[index[0]][index[1]] = direction.vector

        return matrix


rays = Ray(e, d, top, bottom, right, left)

print(rays.perspective_projection(640, 480))
