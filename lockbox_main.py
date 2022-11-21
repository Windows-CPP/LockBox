# LockBox | Windows NT Standalone Build | v0.6.2-b

# Temp Est Variables Variables
tempstr = ""
numFail = 0

# Coloured Text Variables
CEND = "\33[0m"
CRED = "\33[31m"
CORG = "\33[33m"
CBLU = "\33[34m"
CGRN = "\33[32m"

## ENCRYPTION ALGORYTHM START ##
from pyth.settings import genInf
print("LockBox::Action::Starting")
print("LockBox::" + genInf["build"] + "/" + genInf["version"])

print("LockBox::Action::Boot::GetLibs()")

# Premade libs
from random import randint
from PIL import Image as imge # Image size reading lib
from tqdm import tqdm

# Custom libs & data
from pyth.settings import imgLoc, settings # Image locations for later on, too lazy to create an autoManifest
from pyth.functions import cls, autoImageManifeset # will come in handy
from pyth.classes import EncDec # Main encryp/decryp class, kinda needed

enclevel = settings["enclevel"]
enclevel = enclevel * 128

# Read from settings.py, and print collected imageLoc data to terminal
print("\n\nLockBox::Action::Starting::Reading//settings.py")
print(CBLU + "LockBox::Action::Starting::ReadData//settings.py: " + CEND)

location = "./images/"
imgLoc = autoImageManifeset(location)

setImp = ""
for i in range(len(imgLoc)):
    setImp += str(imgLoc[i])
    setImp += ", "

print(CGRN + str(setImp) + CEND)

# Creating a random number to choose an image
print("\nLockBox::Action::Starting::PixelRand//CreateNum()")
numList = []
for i in range(1000):
    temp = randint(0, (len(imgLoc) - 1)) ## changed from 1 to 0, added -1, fixes bug outlined in bugReportLog_ID001.txt
    numList.append(temp)

# Choosing random number to choose an image
print("\nLockBox::Action::Starting::PixelRand//CreateNum()")
print(CBLU + "LockBox::Action::Starting::PixelRand//NumList[]:" + CEND)
print(CGRN + str(numList) + CEND)

temp = randint(0, len(imgLoc))
imgNum = numList[temp]
numList.clear()

# Opening image for use
print("\nLockBox::Action::Starting::ImageOpen() ")
for i in range(len(imgLoc)):
    if(i == imgNum):
        image = imge.open(imgLoc[imgNum])
    elif(i != imgNum):
        numFail += 1
    else:
        true = true

if(numFail != len(imgLoc)):
    print(CORG + "LockBox::Action::Starting::PixelRand//FailCount: " + str(numFail) + CEND)
elif(numFail == len(imgLoc)):
    print(CRED + "LockBox::Action::Starting::PixelRand//FailCount: " + str(numFail) + CRED)
    print(CRED + "LockBox::ErrorReport::ImgOpen() | IMAGE_INDEX_RANGE_ERROR | Exit Code 0" + CEND)
    exit()
print(CGRN + "LockBox::Action::Starting::PixelRand//SuccessTry_Parse() " + CEND)

# Getting image pixel counts
print("\nLockBox::Action::Starting::PixelDet//PixelCount")

width, height = image.size

print(CBLU + "LockBox::Action::Starting::PixelDet//PixelCount:" + CEND)
print(CGRN + str(width*height) + " (" + str(width) + "x" + str(height) + ")" + CEND)
# getting colour data randomly from the images, putting into string for later use
colourSTR = ""
for i in tqdm(range(1024)):
    ranWI = randint(1, (width - 1))
    ranHI = randint(1, (height - 1))

    image_pix = image.convert('RGB')
    r, g, b = image_pix.getpixel((ranWI, ranHI))
    colourSTR += str((r + g + b))

print(CGRN + str(colourSTR) + CEND)

# Created the final numbers for use in the keygen
print("")
print("\nLockBox::Action::Starting::PixelFinal//FinalList")
finalList = []
for i in range(enclevel):
    temp = randint(1, (len(colourSTR) - 1))
    char = colourSTR[temp]
    finalList += char

# Generates a 4-digit ferpin at the end of encryption
print(CBLU + "LockBox::Action::Starting::PixelFinal//FET_Pin:" + CEND)
for i in range(4):
    temp = randint(0, 255)
    tempstr += finalList[temp]
print(CGRN + tempstr + CEND)

## ENCRYPTION ALGORYTHM END ##

"""
Note for future reference
The string `finalList` contains the 256 numbers that should be used from now out, disregard most of the other lists and variables-
they're safe to overwrite now
"""
