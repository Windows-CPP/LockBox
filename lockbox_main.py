# LockBox | Windows NT Standalone Build

# Windows NT Standalone Build
# v0.6-beta

# Imports
from random import randint, choice
from PIL import Image as imge
from functions import Encryptor # Will be used soon enough

# Temp Est Variables Variables
tempstr = ""

# Coloured Text Variables
CEND = "\33[0m"
CRED = "\33[31m"
CBLU = "\33[34m"
CGRN = "\33[32m"


### MAIN ###
print("LockBox::Action::Starting")

# Read from settings.json, and print collected imageLoc data to terminal
print("\n\nLockBox::Action::Starting::Reading//settings.jsonc")
print(CBLU + "LockBox::Action::Starting::ReadData//settings.jsonc: " + CEND)
from settings import imgLoc_1, imgLoc_2, imgLoc_3
setImp = (imgLoc_1 + " || " + imgLoc_2 + " || " + imgLoc_3)

print(CGRN + str(setImp) + CEND)

# Creating a random number to choose an image
print("\nLockBox::Action::Starting::PixelRand//CreateNum()")
numList = []
for i in range(1000):
    temp = randint(1, 3)
    numList.append(temp)
print(CBLU + "LockBox::Action::Starting::PixelRand//NumList[]:" + CEND)
print(CGRN + str(numList) + CEND)
temp = randint(1, 1000)
imgNum = numList[temp]
numList.clear()

# Getting image pixel counts
print("\nLockBox::Action::Starting::PixelDet//PixelCount")
# opening images for use
if(imgNum == 1):
    image = imge.open(imgLoc_1)
elif(imgNum == 2):
    image = imge.open(imgLoc_2)
elif(imgNum == 3):
    image = imge.open(imgLoc_3)

width, height = image.size

print(CBLU + "LockBox::Action::Starting::PixelDet//PixelCount:" + CEND)
print(CGRN + str(width*height) + " (" + str(width) + "x" + str(height) + ")" + CEND)
# getting colour data randomly from the images, putting into array
colourSTR = ""
for i in range(512):
    ranWI = randint(1, (width - 1))
    ranHI = randint(1, (height - 1))

    image_pix = image.convert('RGB')
    r, g, b = image_pix.getpixel((ranWI, ranHI))
    colourSTR += str((r + g + b))

print(CGRN + str(colourSTR) + CEND)

# Created the final numbers for use in the keygen
print("\nLockBox::Action::Starting::PixelFinal//FinalList")
finalList = ""
for i in range(256):
    temp = randint(1, (len(colourSTR) - 1))
    char = colourSTR[temp]
    finalList += char

# Generates a nonunique pin for the end of the encryption
print(CBLU + "LockBox::Action::Starting::PixelFinal//FET_Pin:" + CEND)
for i in range(4):
    temp = randint(1, 256)
    tempstr += finalList[temp]
print(CGRN + tempstr + CEND)

"""
Note for future reference
The string `finalList` contains the 256 numbers that should be used from now out, disregard most of the other lists and variables-
they're safe to overwrite now
"""
