from PIL import Image

gamma = 1

image_filename = "prof.jpeg"
image = Image.open(image_filename)

pixels = list(image.getdata())

pixels_out = []

for pixel in pixels:
    r = int(((pixel[0] / 255) ** gamma) * 255)
    g = int(((pixel[1] / 255) ** gamma) * 255)
    b = int(((pixel[2] / 255) ** gamma) * 255)

    pixels_out.append((r, g, b))

image_out = Image.new(image.mode, image.size)
image_out.putdata(pixels_out)

image_out.show()
