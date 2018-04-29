from ray_tracing.triangle import Triangle
from ray_tracing.vector import Vector
import numpy
import math


class Polygon:

    def __init__(self, points, color):
        self.color = color
        self.triangles = Polygon.divide_into_triangles(points, color)
        self.triangle_touched = None

    @staticmethod
    def divide_into_triangles(points, color):

        triangles = []

        first_point = points.pop(0)

        for index, point in enumerate(points):
            if index != (len(points) - 1):
                triangles.append(Triangle((first_point, point, points[index + 1]), color))

        return triangles

    def hit(self, ray_direction, ray_origin):

        for triangle in self.triangles:
            if triangle.hit(ray_direction, ray_origin):
                self.triangle_touched = triangle
                return True
        return False

    def get_minimum_t(self, ray_direction, ray_origin):

        return self.triangle_touched.get_minimum_t(ray_direction, ray_origin)

    def polygon_normal(self, p):

        different_points_in_triangle = []

        for index, point in enumerate(self.triangle_touched.points):
            if different_points_in_triangle.__len__() < 2:
                if p != point:
                    different_points_in_triangle.append(point)

        return Vector(numpy.cross((Vector.init_with_points(p, different_points_in_triangle[0])).vector,
                               (Vector.init_with_points(p, different_points_in_triangle[1])).vector)).unit_vector()


    def lambert(self, ray_direction, ray_origin, t, lamps):

        p = ray_direction.map(lambda value, index: value * t + ray_origin.vector[index]).vector

        n = self.polygon_normal(p)

        pixel_color = []
        L = 0

        for rgb_color in self.color:

            for lamp in lamps:
                l = Vector.init_with_points(p, lamp.position).unit_vector()

                L += rgb_color * lamp.intensity * max(0, numpy.dot(n.vector, l.vector))

            pixel_color.append(L)
            L = 0

        return (int(pixel_color[0]),
                int(pixel_color[1]),
                int(pixel_color[2]))

    def blihn_pmong(self, ray_direction, ray_origin, t, lamps, sensibility, environment):

        p = ray_direction.map(lambda value, index: value * t + ray_origin.vector[index]).vector
        v = ray_direction.unit_vector()

        n = self.polygon_normal(p)

        pixel_color = []
        lambert = self.lambert(ray_direction, ray_origin, t, lamps)
        L = 0

        for index, rgb_color in enumerate(self.color):

            for lamp in lamps:
                l = Vector.init_with_points(p, lamp.position).unit_vector()
                h = v.map(lambda value, index: value + l.vector[index]).unit_vector()

                L += lambert[index] + lamp.color[index] * lamp.intensity * math.pow(
                    max(0, numpy.dot(n.vector, h.vector)),
                    sensibility)

            pixel_color.append(environment.intensity * environment.color[index] + L)
            L = 0

        return (int(pixel_color[0]),
                int(pixel_color[1]),
                int(pixel_color[2]))
