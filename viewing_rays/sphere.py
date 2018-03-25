import numpy
from vector import Vector
import math


class Sphere:
    def __init__(self, center, ray, color):
        self.center = Vector(center)
        self.ray = ray
        self.color = color

    def hit(self, ray_direction, ray_origin):
        subtract_origin_center = ray_origin.map(lambda value, index: value - self.center.vector[index])

        delta = (math.pow((numpy.dot(ray_direction.map(lambda value, index: value * 2).vector,
                                     subtract_origin_center.vector)), 2)) - (
                        numpy.dot(ray_direction.vector, ray_direction.vector) * 4 * (
                        (numpy.dot(subtract_origin_center.vector,
                                   subtract_origin_center.vector)) - math.pow(self.ray, 2)))

        return False if delta < 0 else True

    def get_minimum_t(self, ray_direction, ray_origin):
        subtract_origin_center = ray_origin.map(lambda value, index: value - self.center.vector[index])

        delta = (math.pow((numpy.dot(ray_direction.vector,
                                     subtract_origin_center.vector)), 2)) - (
                        numpy.dot(ray_direction.vector, ray_direction.vector) * ((numpy.dot(subtract_origin_center.vector,
                                                                              subtract_origin_center.vector)) - math.pow(
                    self.ray, 2)))

        t_first = (numpy.dot(ray_direction.map(lambda value, index: value * (-1)).vector,
                             subtract_origin_center.vector) + math.sqrt(delta)) / numpy.dot(ray_direction.vector,
                                                                                            ray_direction.vector)
        t_second = (numpy.dot(ray_direction.map(lambda value, index: value * (-1)).vector,
                              subtract_origin_center.vector) - math.sqrt(delta)) / numpy.dot(ray_direction.vector,
                                                                                             ray_direction.vector)

        return min(t_first, t_second)
