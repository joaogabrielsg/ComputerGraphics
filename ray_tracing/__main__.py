import math

from ray_tracing.viewing_rays import Ray
from ray_tracing.sphere import Sphere
from ray_tracing.image import Image
from ray_tracing.lamp import Lamp
from ray_tracing.polygon import Polygon
from ray_tracing.environment import Environment
from ray_tracing.cube import Cube

def main():
    # This is an example of how you can use this module, creating objects and displaying them on an image.

    #image size
    image_size = [70, 70]

    cube = [Cube(center=(2, -5, 2), side_size=5)]

    # Creating illumination points
    lamps = [Lamp(intensity=1, color=[100, 100, 100], position=[-10, -10, 10]),
             Lamp(intensity=1, color=[100, 100, 100], position=[0, 0, 0]),
             Lamp(intensity=1, color=[100, 100, 100], position=[10, 10, -10]),
             Lamp(intensity=1, color=[100, 100, 100], position=[20, 30, 10]),
             Lamp(intensity=1, color=[100, 100, 100], position=[30, 10, 30]),
             ]


    # Creating environment
    environment = Environment(intensity=0.1, color=[40, 100, 150])

    for i in range(10, 150, 25):

        # Starting Ray-Tracing
        rays = Ray(point_e=[i, -i, 20], distance=20, top=20, bottom=-20, right=20, left=-20)

        # Setting the Ray-tracing matrix size
        ray_matrix_normal = rays.parallel_projection(row=image_size[0], column=image_size[1])

        Image.generate_objects_image(polygons=cube, matrix=ray_matrix_normal, image_size=image_size, lamps=lamps, sensibility=10, environment=environment)


if __name__ == '__main__':
    main()
