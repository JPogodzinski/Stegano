from PIL import Image
import bitarray


def bit2str(bits):
    result=bitarray.bitarray(bits).tobytes().decode('ISO-8859-1')
    return result
def str2bit(text):
    result = bitarray.bitarray()
    result.frombytes(text.encode('ISO-8859-1'))
    return result

def encode(text, filename):
    bits=str2bit(text)
    print(bits)
    image=Image.open(filename)
    width, height=image.size
    i=0
    for x in range (0,width):
        for y in range (0, height):
            if(i<len(bits)):
                pixel=list(image.getpixel((x,y)))
                for n in range(0,3):
                    pixel[n]=pixel[n] & ~1 | int(bits[i])
                    i+=1
                image.putpixel((x,y),tuple(pixel))
    image.save("secret.jpg", "JPEG")

def decode(filename):
    result=[]
    image=Image.open(filename)
    width, height = image.size
    for x in range(0, width):
        for y in range(0, height):
                pixel = list(image.getpixel((x, y)))
                for n in range(0, 3):
                    result.append(pixel[n]&1)
    data=bit2str(result)
    return data

if __name__ == '__main__':
    text = "Confusion"
    encode(text, "image.jpg")
    decoded=decode("secret.jpg")
    print(decoded)
