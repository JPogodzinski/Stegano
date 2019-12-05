from PIL import Image
import bitarray


def str2bit(text):
    array = bitarray.bitarray()
    array.frombytes(text.encode('utf-8'))
    print("bit array: ", array)
    result = (str(array))[10:-2]
    return result


def encode(data, filename):
    bits = str2bit(data)
    print(bits)
    image = Image.open(filename)
    width, height = image.size
    i = 0
    for x in range(0, width):
        for y in range(0, height):
            pixel = list(image.getpixel((x, y)))
            for n in range(0, 3):
                if i < len(bits):
                    pixel[n] = pixel[n] & ~1 | int(bits[i])
                    i = i + 1
            image.putpixel((x, y), tuple(pixel))
    image.save("secret.png", "PNG")
    return len(bits)


def decode(filename):
    result = []
    image = Image.open(filename)
    width, height = image.size
    for x in range(0, width):
        for y in range(0, height):
            pixel = list(image.getpixel((x, y)))
            for n in range(0, 3):
                result.append(pixel[n] & 1)
    data = "".join([str(x) for x in result])
    return data


if __name__ == '__main__':
    text = "Skadze maja wiedziec w syberyjskich borach, Ze to zycie to tylko taka metafora."
    leng=encode(text, "image.png")
    decoded = decode("secret.png")
    print(decoded[:1000])
    print(decoded[:leng])
