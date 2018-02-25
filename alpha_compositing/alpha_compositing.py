from PIL import Image

alpha = 0.6

alpha_channel_filename = "alpha_channel.png"
background_filename = "background.jpg"
foreground_filename = "foreground.png"

alpha_channel = Image.open(alpha_channel_filename)
background = Image.open(background_filename)
foreground = Image.open(foreground_filename)

alpha_channel_pixels = list(alpha_channel.getdata())
foreground_pixels = list(foreground.getdata())
background_pixels = list(background.getdata())

pixels_out = []

for alpha_channel_pixel in alpha_channel_pixels:
    r = alpha_channel_pixel[0]

for index_pixel in range(len(alpha_channel_pixels)):
    ra = alpha_channel_pixels[index_pixel]
    rf = foreground_pixels[index_pixel]
    rb = background_pixels[index_pixel]

    r_alpha = int((rf[0] * (ra[0] / 255)))
    g_alpha = int((rf[1] * (ra[1] / 255)))
    b_alpha = int((rf[2] * (ra[2] / 255)))

    r = int((alpha * r_alpha) + ((1 - alpha) * rb[0]))
    g = int((alpha * g_alpha) + ((1 - alpha) * rb[1]))
    b = int((alpha * b_alpha) + ((1 - alpha) * rb[2]))

    pixels_out.append((r, g, b))

image_out = Image.new(foreground.mode, foreground.size)
image_out.putdata(pixels_out)

image_out.show()