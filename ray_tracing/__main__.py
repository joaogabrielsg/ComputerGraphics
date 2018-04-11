from viewing_rays import Ray
from sphere import Sphere
from image import Image
from lamp import Lamp
from polygon import Polygon
from environment import Environment


def main():
    # Starting Ray-Tracing
    rays = Ray(point_e=[10, 10, 10], distance=5, top=5, bottom=-5, right=5, left=-5)

    # Creating objects to be displayed in the image
    objects = [Sphere(center=(-4, 0, 0), ray=2, color=(150, 100, 150)),
               Sphere(center=(2, -5, 2), ray=3, color=(250, 250, 250)),
               Polygon(points=[[0, 0, 0], [4, 2, 0], [0, 4, 0]], color=(200, 200, 200))]

    objects2 = [Sphere(center=(-4, 0, 0), ray=2, color=(150, 100, 150)),
                Sphere(center=(2, -5, 2), ray=3, color=(250, 250, 250)),
                Polygon(points=[[0, 0, 0], [4, 0, 0], [4, 4, 0], [0, 4, 0]], color=(200, 200, 200))]

    objects3 = [Sphere(center=(-4, 0, 0), ray=2, color=(150, 100, 150)),
                Sphere(center=(2, -5, 2), ray=3, color=(250, 250, 250)),
                Polygon(points=[[0, 0, 0], [4, 0, 0], [6, 2, 0], [4, 4, 0], [0, 4, 0]], color=(200, 200, 200))]

    spheres = [Sphere(center=(-4, 0, 0), ray=2, color=(150, 100, 150)),
               Sphere(center=(2, -5, 2), ray=3, color=(250, 250, 250))]

    # Creating ilumination points
    lamp = Lamp(intensity=1, color=[100, 100, 100], position=[-10, -10, -10])

    # Creating environment
    environment = Environment(intensity=0.1, color=[40, 100, 150])

    # Setting the image size
    matrix = rays.perspective_projection(row=200, column=200)

    # Inserting objects in the image
    Image.generate_spheres_image(spheres=spheres, matrix=matrix, image_size=[200, 200], lamp=lamp, sensibility=10, environment=environment)


if __name__ == '__main__':
    main()