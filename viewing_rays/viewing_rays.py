import math
import numpy
from vector import Vector
from sphere import Sphere
from image import Image


class Ray:

    def __init__(self, point_e, distance, top, bottom, right, left):

        self.point_e = Vector(point_e)

        self.distance = distance
        self.top = top
        self.bottom = bottom
        self.right = right
        self.left = left

        self.w = self.point_e.unit_vector()
        self.t = self.w.non_collinear_vector()
        self.u = Vector(numpy.cross(self.w.vector, self.t.vector)).unit_vector()
        self.v = Vector(numpy.cross(self.w.vector, self.u.vector))

    def perspective_projection(self, row, column):

        matrix = numpy.zeros((row, column), dtype=numpy.ndarray)

        for index, pixel in numpy.ndenumerate(matrix):
            U = self.left + (self.right - self.left) * (index[0] + 0.5) / row
            V = self.bottom + (self.top - self.bottom) * (index[1] + 0.5) / column

            direction_v = self.v.map(lambda value, index: value * V)
            direction_u = self.u.map(lambda value, index: value * U)
            direction_w = self.w.map(lambda value, index: value * self.distance)

            direction = direction_u.map(lambda value, index: value + direction_v.vector[index])
            direction = direction.map(lambda value, index: value + direction_w.vector[index])

            matrix[index[0]][index[1]] = (direction.vector, self.point_e)

        return matrix


rays = Ray([10, 10, 10], 5, 5, -5, 5, -5)
spheres = [Sphere((0, 0, 0), 2, (150, 100, 150)), Sphere((2, -3, 2), 3, (250, 250, 250))]

matrix = rays.perspective_projection(300, 200)
Image.spheres_image(spheres, matrix, [300, 200])
