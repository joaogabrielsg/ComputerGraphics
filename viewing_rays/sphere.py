import numpy
from vector import Vector
import math


class Sphere:
    def __init__(self, center, ray, color):
        self.center = Vector(center)
        self.ray = ray
        self.color = color

    def hit(self, ray_direction, ray_origin):

        print(Vector(ray_origin))
        substraction_origin_center = ray_origin.subtract_by_vector(self.center)

        sqrt = (numpy.dot(substraction_origin_center.vector, substraction_origin_center.vector)) - math.pow(self.ray, 2)

        delta_second = numpy.dot(ray_direction, ray_direction) * 4 * sqrt

        delta_first = numpy.dot(Vector(ray_direction).multiply_by_number(2).vector, substraction_origin_center.vector)

        delta_first = math.pow(delta_first, 2)

        delta = delta_first - delta_second

        return False if delta < 0 else True

    def t(self, ray_direction, ray_origin):
        substraction_origin_center = ray_origin.subtract_by_vector(self.center)

        delta_second = (numpy.dot(substraction_origin_center.vector, substraction_origin_center.vector)) - math.pow(self.ray, 2)

        delta_second = numpy.dot(ray_direction, ray_direction) * 4 * delta_second

        delta_first = numpy.dot(Vector(ray_direction).multiply_by_number(2).vector, substraction_origin_center.vector)

        delta_first = math.pow(delta_first, 2)

        delta = delta_first - delta_second

        t_first = (numpy.dot((Vector(ray_direction).multiply_by_number(-1).vector), substraction_origin_center.vector) + math.sqrt(delta)) / numpy.dot(ray_direction, ray_direction)
        t_second = (numpy.dot((Vector(ray_direction).multiply_by_number(-1).vector), substraction_origin_center.vector) - math.sqrt(delta)) / numpy.dot(ray_direction, ray_direction)

        return min(t_first, t_second)






