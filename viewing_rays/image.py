from PIL import Image as PilImage
import numpy


class Image:

    @staticmethod
    def show(image, row, column):

        image_out = PilImage.new("RGBA", (row, column))
        image_out.putdata(image)
        image_out.show()

    @staticmethod
    def generate_spheres_image(spheres, matrix, image_size, lamp):
        # matrix: first = direction
        #         second = origin

        image = []

        for index, value in numpy.ndenumerate(matrix):

            color = (0, 0, 0)
            smaller_t = 1

            for sphere in spheres:

                if sphere.hit(value[0], value[1]):

                    t = sphere.get_minimum_t(value[0], value[1])

                    if t < smaller_t:
                        smaller_t = t
                        color = sphere.lambert(value[0], value[1], smaller_t, lamp)

            image.append(color)

        Image.show(image, image_size[0], image_size[1])

    @staticmethod
    def generate_objects_image(polygons, matrix, image_size):

        image = []

        for index, value in numpy.ndenumerate(matrix):

            color = (0, 0, 0)
            smaller_t = 1

            for polygon in polygons:

                if polygon.hit(value[0], value[1]):

                    t = polygon.get_minimum_t(value[0], value[1])

                    if t < smaller_t:
                        smaller_t = t
                        color = polygon.color

            image.append(color)

        Image.show(image, image_size[0], image_size[1])
