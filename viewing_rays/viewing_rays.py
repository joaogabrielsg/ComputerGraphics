import math
import numpy
from vector import Vector
from sphere import Sphere
from PIL import Image

class Ray():

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

            matrix[index[0]][index[1]] = direction.vector

        return matrix


    def image_spheres(self, spheres, matrix):

        image = []

        for index, direction in numpy.ndenumerate(matrix):

            color = (0, 0, 0)
            smaller_t = 1

            for sphere in spheres:

                if sphere.hit(direction, self.point_e):

                    t = sphere.t(direction, self.point_e)

                    if t < smaller_t:
                        smaller_t = t
                        color = sphere.color

            image.append(color)

        return image


image = []

rays = Ray([10, 10, 10], 5, 5, -5, 5, -5)

matrix = rays.perspective_projection(200, 200)
spheres = [Sphere((0,0,0), 3, (150, 100, 150)), Sphere((2,-3,2), 5, (250, 250, 250))]
image = rays.image_spheres(spheres, matrix)

image_out = Image.new("RGBA", (200, 200))
image_out.putdata(image)
image_out.show()