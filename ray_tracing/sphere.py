import numpy
from ray_tracing.vector import Vector
import math


class Sphere:
    def __init__(self, center, ray, color):
        self.center = center
        self.ray = ray
        self.color = color

    def hit(self, ray_direction, ray_origin):
        subtract_origin_center = ray_origin.map(lambda value, index: value - self.center[index])

        delta = (math.pow((numpy.dot(ray_direction.map(lambda value, index: value * 2).vector,
                                     subtract_origin_center.vector)), 2)) - (
                        numpy.dot(ray_direction.vector, ray_direction.vector) * 4 * (
                        (numpy.dot(subtract_origin_center.vector,
                                   subtract_origin_center.vector)) - math.pow(self.ray, 2)))

        return False if delta < 0 else True

    def get_minimum_t(self, ray_direction, ray_origin):
        subtract_origin_center = ray_origin.map(lambda value, index: value - self.center[index])

        delta = (math.pow((numpy.dot(ray_direction.vector,
                                     subtract_origin_center.vector)), 2)) - (
                        numpy.dot(ray_direction.vector, ray_direction.vector) * (
                            (numpy.dot(subtract_origin_center.vector,
                                       subtract_origin_center.vector)) - math.pow(
                        self.ray, 2)))

        t_first = (numpy.dot(ray_direction.map(lambda value, index: value * (-1)).vector,
                             subtract_origin_center.vector) + math.sqrt(delta)) / numpy.dot(ray_direction.vector,
                                                                                            ray_direction.vector)
        t_second = (numpy.dot(ray_direction.map(lambda value, index: value * (-1)).vector,
                              subtract_origin_center.vector) - math.sqrt(delta)) / numpy.dot(ray_direction.vector,
                                                                                             ray_direction.vector)

        return min(t_first, t_second)

    def lambert(self, ray_direction, ray_origin, t, lamp):

        p = ray_direction.map(lambda value, index: value * t + ray_origin.vector[index]).vector
        n = Vector.init_with_points(p, self.center).unit_vector()
        l = Vector.init_with_points(p, lamp.position).unit_vector()

        pixel_color = []

        for rgb_color in self.color:
            pixel_color.append(rgb_color * lamp.intensity * max(0, numpy.dot(n.vector, l.vector)))

        return (int(pixel_color[0]),
                int(pixel_color[1]),
                int(pixel_color[2]))

    def blihn_pmong(self, ray_direction, ray_origin, t, lamp, sensibility, environment):

        p = ray_direction.map(lambda value, index: value * t + ray_origin.vector[index]).vector
        n = Vector.init_with_points(p, self.center).unit_vector()
        l = Vector.init_with_points(p, lamp.position).unit_vector()
        v = ray_direction.unit_vector()
        h = v.map(lambda value, index: value + l.vector[index]).unit_vector()

        pixel_color = []
        lambert = self.lambert(ray_direction, ray_origin, t, lamp)

        for index, rgb_color in enumerate(self.color):
            pixel_color.append(environment.intensity * environment.color[index] +
                               lambert[index] +
                               lamp.color[index] * lamp.intensity * math.pow(max(0, numpy.dot(n.vector, h.vector)),
                                                                             sensibility))

        return (int(pixel_color[0]),
                int(pixel_color[1]),
                int(pixel_color[2]))
