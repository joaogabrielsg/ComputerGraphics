import numpy
from vector import Vector
import math


class Sphere:
    def __init__(self, center, ray, color):
        self.center = center
        self.ray = ray
        self.color = color

    def hit(self, ray_direction, ray_origin):

        substraction_origin_center = Vector(ray_origin).subtract_by_vector(self.center)

        delta_second = (numpy.dot(substraction_origin_center, substraction_origin_center)) - math.pow(self.ray, 2)

        delta_second = numpy.dot(ray_direction, ray_direction) * 4 * delta_second

        delta_first = numpy.dot(Vector(ray_direction).multiply_by_number(2), substraction_origin_center)

        delta = delta_first - delta_second

        return True if delta < 0 else False

    def t(self, ray_direction, ray_origin):
        substraction_origin_center = Vector(ray_origin).subtract_by_vector(self.center)

        delta_second = (numpy.dot(substraction_origin_center, substraction_origin_center)) - math.pow(self.ray, 2)

        delta_second = numpy.dot(ray_direction, ray_direction) * delta_second

        delta_first = numpy.dot(Vector(ray_direction).multiply_by_number(2), substraction_origin_center)

        delta = delta_first - delta_second

        t_first = (numpy.dot((Vector(ray_direction).multiply_by_number(-1)), substraction_origin_center) + math.sqrt(delta)) / numpy.dot(ray_direction, ray_direction)
        t_second = (numpy.dot((Vector(ray_direction).multiply_by_number(-1)), substraction_origin_center) - math.sqrt(delta)) / numpy.dot(ray_direction, ray_direction)

        return min(t_first, t_second)






