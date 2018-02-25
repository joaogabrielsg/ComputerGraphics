from PIL import Image

alpha = 0.2

alpha_channel_filename = "alpha_channel.png"
background_filename = "background.jpg"
foreground_filename = "foreground.png"

alpha_channel = Image.open(alpha_channel_filename)
background = Image.open(background_filename)
foreground = Image.open(foreground_filename)

alpha_channel_pixels = list(alpha_channel.getdata())
foreground_pixels = list(foreground.getdata())
background_pixels = list(background.getdata())

alpha_channel_pixels_out = []

pixels_out = []

for alpha_channel_pixel in alpha_channel_pixels:
    r = int(alpha_channel_pixel[0] * (1 - alpha))
    g = int(alpha_channel_pixel[1] * (1 - alpha))
    b = int(alpha_channel_pixel[2] * (1 - alpha))

    alpha_channel_pixels_out.append((r, g, b, 255))


for index_pixel in range(len(alpha_channel_pixels_out)):
    ra = alpha_channel_pixels_out[index_pixel]
    rf = foreground_pixels[index_pixel]
    rb = background_pixels[index_pixel]

    r_alpha = int((rf[0] * (ra[0] / 255)))
    g_alpha = int((rf[1] * (ra[1] / 255)))
    b_alpha = int((rf[2] * (ra[2] / 255)))

    if r_alpha == 0 & g_alpha == 0 & b_alpha == 0:
        pixels_out.append((rb[0], rb[1], rb[2]))
    else:
        r = int((r_alpha) + ((1 - alpha) * rb[0]))
        g = int((g_alpha) + ((1 - alpha) * rb[1]))
        b = int((b_alpha) + ((1 - alpha) * rb[2]))

        pixels_out.append((r, g, b))

image_out = Image.new(foreground.mode, foreground.size)
image_out.putdata(pixels_out)

image_out.show()