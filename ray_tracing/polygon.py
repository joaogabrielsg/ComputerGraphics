from triangle import Triangle


class Polygon:

    def __init__(self, points, color):
        self.color = color
        self.triangles = Polygon.divide_into_triangles(points, color)
        self.triangle_touched = None

    @staticmethod
    def divide_into_triangles(points, color):

        triangles = []

        first_point = points.pop(0)

        print(first_point)

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

        # smaller_t = 1000
        #
        # for triangle in self.triangles:
        #     t = triangle.get_minimum_t(ray_direction, ray_origin)
        #     if t < smaller_t:
        #         smaller_t = t
        #
        # return smaller_t


