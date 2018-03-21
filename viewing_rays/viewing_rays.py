import math
import numpy
from vector import Vector
from sphere import Sphere
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
            direction_w = self.w.map(lambda value, index: value * d)

            # direction = direction_u.sum_by_vector(direction_v)
            direction = direction_u.map(lambda value, index: value + direction_v.vector[index])
            # direction = direction.subtract_by_vector(direction_w)
            direction = direction.map(lambda value, index: value - direction_w.vector[index])

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






rays = Ray(e, d, top, bottom, right, left)

matrix = rays.perspective_projection(250, 250)

spheres = [Sphere((0,0,0), 1, (100, 100, 100)), Sphere((2,-2,2), 2, (250, 250, 250))]

image = rays.image_spheres(spheres, matrix)

image_out = Image.new("RGBA", (250, 250))

image_out.putdata(image)

print(image_out)

image_out.show()
