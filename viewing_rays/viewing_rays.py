import numpy
from vector import Vector
from sphere import Sphere
from image import Image
from polygon import Polygon
from triangle import Triangle


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

    def get_U(self, index_i, row):
        return self.left + (self.right - self.left) * (index_i + 0.5) / row

    def get_V(self, index_j, column):
        return self.bottom + (self.top - self.bottom) * (index_j + 0.5) / column

    def get_perspective_direction(self, U, V):

        return ((self.u.map(lambda value, index: value * U)).map(
            lambda value, index: value + (self.v.map(lambda value, index: value * V)).vector[index])).map(
            lambda value, index: value + (self.w.map(lambda value, index: value * self.distance)).vector[index])

    def get_parallel_origin(self, U, V):

        return (self.u.map(lambda value, index: value * U)).map(
            lambda value, index: value + (self.v.map(lambda value, index: value * V)).vector[index] +
                                 self.point_e.vector[index])

    def perspective_projection(self, row, column):

        matrix = numpy.zeros((row, column), dtype=numpy.ndarray)

        for index, pixel in numpy.ndenumerate(matrix):
            matrix[index[0]][index[1]] = (self.get_perspective_direction(
                self.get_U(index[0], row),
                self.get_V(index[1], column)), self.point_e)

        return matrix

    def parallel_projection(self, row, column):

        matrix = numpy.zeros((row, column), dtype=numpy.ndarray)

        for index, pixel in numpy.ndenumerate(matrix):
            matrix[index[0]][index[1]] = (self.w, self.get_parallel_origin(
                self.get_U(index[0], row),
                self.get_V(index[1], column)))

        return matrix


rays = Ray([10, 10, 10], 5, 5, -5, 5, -5)
spheres = Sphere((0, 0, 0), 2, (150, 100, 150)), Sphere((2, -3, 2), 3, (250, 250, 250))
# triangle = Triangle([[0, 0, 0, ], [4, 0, 0], [2, 4, 0]], (200, 200, 200))

# polygon = Polygon([[0, 0, 0], [4, 0, 0], [4, 4, 0], [0, 4, 0]], (200, 200, 200))


objects = [Sphere((0, 0, 0), 2, (150, 100, 150)), Sphere((2, -3, 2), 3, (250, 250, 250)), Polygon([[0, 0, 0], [4, 2, 0], [0, 4, 0]], (200, 200, 200))]
objects2 = [Sphere((0, 0, 0), 2, (150, 100, 150)), Sphere((2, -3, 2), 3, (250, 250, 250)), Polygon([[0, 0, 0], [4, 0, 0], [4, 4, 0], [0, 4, 0]], (200, 200, 200))]
objects3 = [Sphere((0, 0, 0), 2, (150, 100, 150)), Sphere((2, -3, 2), 3, (250, 250, 250)), Polygon([[0, 0, 0], [4, 0, 0], [6, 2, 0], [4, 4, 0], [0, 4, 0]], (200, 200, 200))]


matrix = rays.perspective_projection(200, 200)
# Image.generate_spheres_image(spheres, matrix, [200, 200])
Image.generate_objects_image(objects, matrix, [200, 200])
Image.generate_objects_image(objects2, matrix, [200, 200])
Image.generate_objects_image(objects3, matrix, [200, 200])




