from PIL import Image

def genData(data):
    return [format(ord(i), '08b') for i in data]

def modPix(pix, data):
    datalist = genData(data)
    imdata = iter(pix)

    for i in range(len(datalist)):
        pixels = [value for value in imdata.__next__()[:3] +
                              imdata.__next__()[:3] +
                              imdata.__next__()[:3]]

        for j in range(0, 8):
            if datalist[i][j] == '0' and pixels[j] % 2 != 0:
                pixels[j] -= 1
            elif datalist[i][j] == '1' and pixels[j] % 2 == 0:
                pixels[j] -= 1

        if i == len(datalist) - 1:
            if pixels[-1] % 2 == 0:
                pixels[-1] -= 1
        else:
            if pixels[-1] % 2 != 0:
                pixels[-1] -= 1

        yield tuple(pixels[0:3])
        yield tuple(pixels[3:6])
        yield tuple(pixels[6:9])

def encode_image(path, message, output_path):
    img = Image.open(path)
    new_img = img.copy()
    w = new_img.size[0]
    (x, y) = (0, 0)

    for pixel in modPix(new_img.getdata(), message):
        new_img.putpixel((x, y), pixel)
        if x == w - 1:
            x = 0
            y += 1
        else:
            x += 1

    new_img.save(output_path, str(output_path.split('.')[-1]))

def decode_image(path):
    img = Image.open(path)
    data = ''
    imgdata = iter(img.getdata())

    while True:
        pixels = [value for value in imgdata.__next__()[:3] +
                              imgdata.__next__()[:3] +
                              imgdata.__next__()[:3]]
        binstr = ''
        for i in pixels[:8]:
            if i % 2 == 0:
                binstr += '0'
            else:
                binstr += '1'
        data += chr(int(binstr, 2))
        if pixels[-1] % 2 != 0:
            return data