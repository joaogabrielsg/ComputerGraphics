from ray_tracing.viewing_rays import Ray
from ray_tracing.sphere import Sphere
from ray_tracing.image import Image
from ray_tracing.lamp import Lamp
from ray_tracing.polygon import Polygon
from ray_tracing.environment import Environment


def main():
    # This is an example of how you can use this module, creating objects and displaying them on an image.

    # Starting Ray-Tracing
    rays = Ray(point_e=[10, 10, 10], distance=5, top=5, bottom=-5, right=5, left=-5)

    # Setting the Ray-tracing matrix size
    ray_matrix = rays.perspective_projection(row=512, column=512)

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

    # Creating illumination points
    lamps = [Lamp(intensity=1, color=[100, 100, 100], position=[-10, -10, 10]), Lamp(intensity=0.5, color=[100, 100, 100], position=[0, 0, 0])]

    # Creating environment
    environment = Environment(intensity=0.1, color=[40, 100, 150])

    # Inserting objects in the image
    Image.generate_objects_image(polygons=objects3, matrix=ray_matrix, image_size=[512, 512], lamps=lamps, sensibility=10,
                                 environment=environment)


if __name__ == '__main__':
    main()
