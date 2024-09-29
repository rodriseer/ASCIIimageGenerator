from PIL import Image, ImageDraw, ImageFont
import math

# you can change these characters below as you will, changing these characters changes hthe image's vibe
# in ASCII these characters are defined by brightness level, hence why these chacracters being selected by me firstly
chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "[::-1] # reverses the string

"""
charArray: this will convert the string chars into a list of individual characters (elements on the list)
charLength: the lenght of this var(int) will depend on the total size of the charArray(list)
interval: in ASCII dividing the total number of characters (charLength) by 256, the code determines how many shades 
          of gray each character will represent (from 0 to 255)
"""
charArray = list(chars)
charLength = len(charArray)
interval = charLength/256

"""
scaleFactor: return a less quantity ASCII image, higher values return more qunatity ASCII characters to the image
oneCharWidth: defines the width of one character in the ASCII art in pixels
oneCharHeight: defines the height of one character in the ASCII art in pixels
"""
scaleFactor = 0.02
oneCharWidth = 10
oneCharHeight = 18

def getChar(inputInt):
    """
    for further understanding of what this method is returning:
    inputInt: represents an integer value, corresponding to a grayscale pixel intensity (0 to 255)
    interval: this was defined earlier as charLength/256, which divides the total number of characters in charArray by 256 (the range of possible pixel intensities)
              so each character in charArray represents a different range of brightness

    inputInt * interval: this scales the pixel intensity (inputInt) to match the index range of charArray. 
               if inputInt is 128 (mid-range gray), multiplying it by the interval maps it to a value between 0 and charLength - 1 (the index range of charArray)

    math.floor: ensures that the result is rounded down to the nearest whole number
    """
    return charArray[math.floor(inputInt*interval)]
"""
text_file: defines the name of the file this program will generate
im: the image file you want to convert
fnt: the font you want to use for the characters in ASCII art, change the font as you as each one will change the overral vibe
"""
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
        divide total values by mean 3 and then converting these values to gray color
        """ 
        h = int(r/3 + g/3 + b/3)
        pix[j, i] = (h, h, h)
        text_file.write(getChar(h))
        d.text((j*oneCharWidth, i * oneCharHeight), getChar(h), font = fnt, fill = (r, g, b))

    text_file.write('\n')


im.save(r"///")
outputImage.save(r"////")
