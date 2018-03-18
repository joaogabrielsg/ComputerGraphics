import numpy


class Vector():

    def __init__(self, vector):
        self.vector = vector

    # (vetor) / (||vetor||)
    # @staticmethod
    # def unit_vector(vector):
    #     vector_module = numpy.linalg.norm(vector)
    #     return [vector[0] / vector_module, vector[1] / vector_module, vector[2] / vector_module]

    def unit_vector(self):
        vector_module = numpy.linalg.norm(self.vector)
        return Vector([self.vector[0] / vector_module, self.vector[1] / vector_module, self.vector[2] / vector_module])

    # @staticmethod
    def non_collinear_vector(self):
        t_min_index = 0
        t_min = 0

        for index, value in enumerate(self.vector):
            if (t_min > abs(value)):
                t_min_index = index

        t = self.vector[:]
        t[t_min_index] = 1

        return Vector(t)

    def multiply_by_number(self, number):
        vector = []
        for value in self.vector:
            vector.append(value * number)

        return Vector(vector)

    def sum_by_number(self, number):
        vector = []
        for value in self.vector:
            vector.append(value + number)

        return Vector(vector)

    def sum_by_vector(self, vector):
        out_vector = []
        for index, value in enumerate(self.vector):
            out_vector.append(value + vector.vector[index])

        return Vector(out_vector)

    def subtract_by_vector(self, vector):
        out_vector = []
        for index, value in enumerate(self.vector):
            out_vector.append(value - vector.vector[index])

        return Vector(out_vector)


    #
    # def map_in_vector(self, function):
    #     vector = []
    #     for value in self.vector:
    #         vector.append(lambda value: function(value))
    #
    #     return Vector(vector)