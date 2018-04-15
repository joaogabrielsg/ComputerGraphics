import numpy


class Vector:

    def __init__(self, vector):
        self.vector = vector

    @classmethod
    def init_with_points(cls, start_point, end_point):

        vector = []
        for index, point in enumerate(end_point):
            vector.append(point - start_point[index])

        return cls(vector)

    def unit_vector(self):
        vector_module = numpy.linalg.norm(self.vector)
        return Vector([self.vector[0] / vector_module, self.vector[1] / vector_module, self.vector[2] / vector_module])

    def non_collinear_vector(self):
        t_min_index = 0
        t_min = 0

        for index, value in enumerate(self.vector):
            if (t_min > abs(value)):
                t_min_index = index

        t = self.vector[:]
        t[t_min_index] = 1

        return Vector(t)

    def map(self, function):
        vector = []
        for index, value in enumerate(self.vector):
            vector.append(function(value, index))
        return Vector(vector)
