from ray_tracing.polygon import Polygon
from ray_tracing.vector import Vector


colors = [(255, 0, 0),
          (50, 205, 50),
          (0, 0, 255),
          (255, 255, 255),
          (255, 255, 0),
          (255, 168, 0)]

class Cube:
    def __init__(self, center, side_size):
        self.squares = Cube.divide_into_cubes(center, side_size)
        self.square_touched = None

    @staticmethod
    def divide_into_faces(points):
        faces = [
            ([points[2], points[6], points[7], points[3]]),
            ([points[1], points[5], points[6], points[2]]),
            ([points[7], points[6], points[5], points[4]]),
            ([points[0], points[1], points[2], points[3]]),
            ([points[3], points[7], points[4], points[0]]),
            ([points[4], points[5], points[1], points[0]]),
        ]

        return faces

    @staticmethod
    def divide_into_nine_squares(points, side_size):

        squares = []
        unit_x_vector = Vector.init_with_points(points[0], points[1]).unit_vector()
        unit_y_vector = Vector.init_with_points(points[0], points[3]).unit_vector()

        for y in range(3):
            for x in range(3):

                squares.append(Polygon(points=[
                       ((points[0][0] + (unit_x_vector.vector[0] * x * (side_size / 3)) + (
                                   unit_y_vector.vector[0] * y * (side_size / 3))),
                        (points[0][1] + (unit_x_vector.vector[1] * x * (side_size / 3)) + (
                                   unit_y_vector.vector[1] * y * (side_size/3))),
                        (points[0][2] + (unit_x_vector.vector[2] * x * (side_size / 3)) + (
                                   unit_y_vector.vector[2] * y * (side_size/3)))),

                       ((points[0][0] + (unit_x_vector.vector[0] * (x + 1) * (side_size / 3)) + (
                                   unit_y_vector.vector[0] * y * (side_size / 3))),
                        (points[0][1] + (unit_x_vector.vector[1] * (x + 1) * (side_size / 3)) + (
                                    unit_y_vector.vector[1] * y * (side_size / 3))),
                        (points[0][2] + (unit_x_vector.vector[2] * (x + 1) * (side_size / 3)) + (
                                    unit_y_vector.vector[2] * y * (side_size / 3)))),

                       ((points[0][0] + (unit_x_vector.vector[0] * (x + 1) * (side_size / 3)) + (
                               unit_y_vector.vector[0] * (y + 1) * (side_size / 3))),
                        (points[0][1] + (unit_x_vector.vector[1] * (x + 1) * (side_size / 3)) + (
                                unit_y_vector.vector[1] * (y + 1) * (side_size / 3))),
                        (points[0][2] + (unit_x_vector.vector[2] * (x + 1) * (side_size / 3)) + (
                                unit_y_vector.vector[2] * (y + 1) * (side_size / 3)))),

                       ((points[0][0] + (unit_x_vector.vector[0] * x * (side_size / 3)) + (
                               unit_y_vector.vector[0] * (y + 1) * (side_size / 3))),
                        (points[0][1] + (unit_x_vector.vector[1] * x * (side_size / 3)) + (
                                unit_y_vector.vector[1] * (y + 1) * (side_size / 3))),
                        (points[0][2] + (unit_x_vector.vector[2] * x * (side_size / 3)) + (
                                unit_y_vector.vector[2] * (y + 1) * (side_size / 3)))),
                       ],
                                       color=(colors[x+y])))

        return squares

    @staticmethod
    def divide_into_cubes(center, side_size):

        squares = []
        squares_faces = []

        faces = Cube.divide_into_faces(
            [(0, 0, 0), (10, 0, 0), (10, 10, 0), (0, 10, 0), (0, 0, 10), (10, 0, 10), (10, 10, 10), (0, 10, 10)])

        for face in faces:
            squares_faces.append(Cube.divide_into_nine_squares(face, 10))

        for face in squares_faces:
            for square in face:
                squares.append(square)

        return squares

    def hit(self, ray_direction, ray_origin):

        for square in self.squares:
            if square.hit(ray_direction, ray_origin):
                self.square_touched = square
                return True
        return False

    def get_minimum_t(self, ray_direction, ray_origin):

        return self.square_touched.get_minimum_t(ray_direction, ray_origin)

    def blihn_pmong(self, ray_direction, ray_origin, t, lamps, sensibility, environment):

        return self.square_touched.blihn_pmong(ray_direction, ray_origin, t, lamps, sensibility, environment)
