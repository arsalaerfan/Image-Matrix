from PIL import Image

im = Image.open("pic.jpg")

def sepia(p):

    if p[0] < 63:
        r,g,b = int(p[0] * 1.5), p[1], int(p[2] * 0.9)

    elif p[0] > 62 and p[0] < 192:
        r,g,b = int(p[0] * 1.15), p[1], int(p[2] * 0.85)

    else:
        r = int(p[0] * 1.08)
        if r > 255:
            r = 255
        g,b = p[1], int(p[2] * 0.5)
    return r, g, b



new = map(sepia, im.getdata())
im.putdata(list(new))
im.show()