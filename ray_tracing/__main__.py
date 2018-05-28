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

    # Starting Ray-Tracing
    rays = Ray(point_e=[20, 20, -20], distance=20, top=20, bottom=-20, right=20, left=-20)

    #image size
    image_size = [100, 100]

    cos = math.cos(180)
    sen = math.sin(180)

    # Setting the Ray-tracing matrix size
    ray_matrix_normal = rays.parallel_projection(row=image_size[0], column=image_size[1])

    # Setting the Ray-tracing rotation 180
    ray_matrix_rotate = rays.perspective_projection_2d(row=image_size[0], column=image_size[1], matrix_2d=[(cos, sen), (-sen, cos)])

    # Setting the Ray-tracing scale 2x size
    ray_matrix_scale = rays.perspective_projection_2d(row=image_size[0], column=image_size[1], matrix_2d=[(0.5, 0.0), (0.0, 0.5)])

    # Setting the Ray-tracing reflection
    ray_matrix_reflection = rays.perspective_projection_2d(row=image_size[0], column=image_size[1], matrix_2d=[(-1, 0), (0, 1)])

    # Setting the Ray-tracing shear
    ray_matrix_shear = rays.perspective_projection_2d(row=image_size[0], column=image_size[1], matrix_2d=[(1, 2), (0, 1)])

    # Creating objects to be displayed in the image
    objects = [Sphere(center=(-4, 0, 0), ray=2, color=(150, 100, 150)),
               Sphere(center=(2, -5, 2), ray=3, color=(250, 250, 250)),
               Polygon(points=[[0, 0, 0], [4, 2, 0], [0, 4, 0]], color=(200, 200, 200))]

    objects2 = [Sphere(center=(-4, 0, 0), ray=2, color=(150, 100, 150)),
                Sphere(center=(2, -5, 2), ray=3, color=(250, 250, 250)),
                Polygon(points=[[0, 0, 0], [4, 0, 0], [4, 4, 0], [0, 4, 0]], color=(200, 200, 200))]

    objects3 = [Sphere(center=(-4, 0, 0), ray=2, color=(150, 100, 150)),
                Sphere(center=(2, -5, 2), ray=3, color=(250, 250, 250)),
                Polygon(points=[[0, 0, 0], [4, 0, 0], [6, 2, 0], [4, 4, 0], [0, 4, 0]], color=(100, 150, 20))]

    spheres = [Sphere(center=(-4, 0, 0), ray=2, color=(150, 100, 150)),
               Sphere(center=(2, -5, 2), ray=3, color=(250, 250, 250))]

    cube = [Cube(center=(2, -5, 2), side_size=5)]

    # Creating illumination points
    lamps = [Lamp(intensity=1, color=[100, 100, 100], position=[-10, -10, 10]), Lamp(intensity=0.5, color=[100, 100, 100], position=[0, 0, 0])]

    # Creating environment
    environment = Environment(intensity=0.1, color=[40, 100, 150])

    # Inserting objects in the image
    # Image.generate_objects_image(polygons=objects3, matrix=ray_matrix_normal, image_size=image_size, lamps=lamps, sensibility=10, environment=environment)
    # Image.generate_objects_image(polygons=objects3, matrix=ray_matrix_scale, image_size=image_size, lamps=lamps, sensibility=10, environment=environment)
    # Image.generate_objects_image(polygons=objects3, matrix=ray_matrix_reflection, image_size=image_size, lamps=lamps, sensibility=10, environment=environment)
    # Image.generate_objects_image(polygons=objects3, matrix=ray_matrix_rotate, image_size=image_size, lamps=lamps, sensibility=10, environment=environment)
    # Image.generate_objects_image(polygons=objects3, matrix=ray_matrix_shear, image_size=image_size, lamps=lamps, sensibility=10, environment=environment)

    Image.generate_objects_image(polygons=cube, matrix=ray_matrix_normal, image_size=image_size, lamps=lamps, sensibility=10, environment=environment)

if __name__ == '__main__':
    main()
