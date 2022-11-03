# LockBox | Windows NT Standalone Edition

# Imports
from json import load
from time import time, sleep
from random import randint, choice
from os import system
from cryptography.fernet import Fernet
from PIL import Image as imge

# General Variables
tempstr = ""

# Coloured Text Variables
CEND = "\33[0m"
CRED = "\33[31m"
CBLU = "\33[34m"
CGRN = "\33[32m"

# Encryption & Decryption methods
def encrypt_dat(location, key):
    "Encrypt the specified file"

def decrypt_dat(location, key):
    "Decrypt the specefied file"


### MAIN ###
print("LockBox::Action::Starting")

# Read from settings.json, and print collected imageLoc data to terminal
print("LockBox::Action::Starting::Reading//settings.jsonc")
print(CBLU + "LockBox::Action::Starting::ReadData//settings.jsonc: " + CEND)
from settings import imgLoc_1, imgLoc_2, imgLoc_3
setImp = (imgLoc_1 + "//" + imgLoc_2 + "//" + imgLoc_3)

print(CGRN + str(setImp) + CEND)

# Creating a random number to choose an image
print("LockBox::Action::Starting::PixelRand//CreateNum()")
numList = []
for i in range(1000):
    temp = randint(1, 3)
    numList.append(temp)
print("LockBox::Action::Starting::PixelRand//NumList[]:")
print(CGRN + str(numList) + CEND)
temp = randint(1, 1000)
imgNum = numList[temp]
numList.clear()

# Getting image pixel counts
print("LockBox::Action::Starting::PixelDet//PixelCount")
# opening images for use
if(imgNum == 1):
    image = imge.open(imgLoc_1)
elif(imgNum == 2):
    image = imge.open(imgLoc_2)
elif(imgNum == 3):
    image = imge.open(imgLoc_3)

width, height = image.size()
print("LockBox::Action::Starting::PixelDet//PixelCount:")
print(CGRN + str(width*height) + CEND)
# getting colour data randomly from the images, putting into array
colourSTR = ""
for i in range(100):
    ranWI = randint(1, width)
    ranHI = randint(1, height)

    image_pix = image.convert('RGB')
    r, g, b = image_pix.getpixel((ranWI, ranHI))
    colourSTR += (r + g + b)

print(CGRN + str(colourSTR) + CEND)

print("LockBox::Action::Starting::PixelFinal//FinalList")
finalList = ""
for i in range(256):
    temp = randint(1, len(colourSTR))
    char = colourSTR[temp]
    finalList += char

print("LockBox::Action::Starting::PixelFinal//FET_Pin:")
for i in range(4):
    temp = randint(1, 256)
    tempstr += finalList[temp]
print(CGRN + tempstr + CEND)