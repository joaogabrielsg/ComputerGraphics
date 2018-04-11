import numpy


class Triangle:

    def __init__(self, points, color):
        self.color = color
        self.points = points

    def get_A(self, direction):

        matrix = []

        for index, value in enumerate(direction.vector):
            matrix.append([(self.points[0][index] - self.points[1][index]),
                           (self.points[0][index] - self.points[2][index]),
                           (value)])

        return numpy.linalg.det(matrix)

    def get_beta(self, direction, origin):

        matrix = []

        for index, value in enumerate(direction.vector):
            matrix.append([(self.points[0][index] - origin.vector[index]),
                           (self.points[0][index] - self.points[2][index]),
                           (value)])

        return numpy.linalg.det(matrix) / self.get_A(direction)

    def get_gama(self, direction, origin):

        matrix = []

        for index, value in enumerate(direction.vector):
            matrix.append([(self.points[0][index] - self.points[1][index]),
                           (self.points[0][index] - origin.vector[index]),
                           (value)])

        return numpy.linalg.det(matrix) / self.get_A(direction)

    def hit(self, ray_direction, ray_origin):

        beta = self.get_beta(ray_direction, ray_origin)
        gama = self.get_gama(ray_direction, ray_origin)

        return True if beta > 0.0 and gama > 0.0 and beta + gama < 1.0 else False

    def get_minimum_t(self, ray_direction, ray_origin):

        matrix = []

        for index, value in enumerate(ray_origin.vector):
            matrix.append([(self.points[0][index] - self.points[1][index]),
                           (self.points[0][index] - self.points[2][index]),
                           (self.points[0][index] - ray_origin.vector[index])])

        return numpy.linalg.det(matrix) / self.get_A(ray_direction)