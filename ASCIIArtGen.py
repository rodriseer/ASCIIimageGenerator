from PIL import Image, ImageDraw, ImageFont
import math

# full chars use, include or add characters as you will
chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "[::-1]

charArray = list(chars)
charLength = len(charArray)
interval =charLength/256

# lower values in scaleFactor return a less ASCII image, higher values return more ASCII characters to the image
scaleFactor = 0.02

oneCharWidth = 10
oneCharHeight = 18


def getChar(inputInt):
    return charArray[math.floor(inputInt*interval)]

text_file = open("Output.txt", "w")

im = Image.open(r"//////")

fnt = ImageFont.truetype('C:\\Windows\\Fonts\\lucon.ttf', 15)


width, height = im.size
im = im.resize((int(scaleFactor*width), int(scaleFactor*height*(oneCharWidth/oneCharHeight))), Image.NEAREST)
width, height = im.size
pix = im.load()

outputImage = Image.new('RGB', (oneCharWidth * width, oneCharHeight * height), color = (0, 0, 0))
d = ImageDraw.Draw(outputImage)

for i in range(height):
    for j in range(width):
        r, g, b = pix[j, i]

        """
        converting image to black and white first
        divide total values by mean 3
        then converting these values to gray color
        """ 
        h = int(r/3 + g/3 + b/3)
        pix[j, i] = (h, h, h)
        text_file.write(getChar(h))
        d.text((j*oneCharWidth, i * oneCharHeight), getChar(h), font = fnt, fill = (r, g, b))

    text_file.write('\n')


im.save(r"///")
outputImage.save(r"////")
