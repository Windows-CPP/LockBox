# LockBox | Windows NT Standalone Build

# Windows NT Standalone Build
# v0.6-beta

# Imports
from random import randint, choice
from PIL import Image as imge
from time import sleep
from functions import cls # will come in handy later fs

# Temp Est Variables Variables
tempstr = ""
numFail = 0

# Coloured Text Variables
CEND = "\33[0m"
CRED = "\33[31m"
CORG = "\33[33m"
CBLU = "\33[34m"
CGRN = "\33[32m"


### MAIN ###
print("LockBox::Action::Starting")


################################################ BETA CHANNEL WORKLIST START ################################################
# originally, this would inmport a set num of images
# now, it will import however many images are registered in `settings.py`
# makers life easier when 100+ imagse are imported for the final release

# Read from settings.json, and print collected imageLoc data to terminal
print("\n\nLockBox::Action::Starting::Reading//settings.py")
print(CBLU + "LockBox::Action::Starting::ReadData//settings.jsonc: " + CEND)
from settings import imgLoc
setImp = ""
for i in range(len(imgLoc)):
    setImp += str(imgLoc[i])
    setImp += ", "

print(CGRN + str(setImp) + CEND)

# Creating a random number to choose an image
print("\nLockBox::Action::Starting::PixelRand//CreateNum()")
numList = []
for i in range(1000):
    temp = randint(1, len(imgLoc))
    numList.append(temp)

# Choosing random number to choose an image
print("\nLockBox::Action::Starting::PixelRand//CreateNum()")
print(CBLU + "LockBox::Action::Starting::PixelRand//NumList[]:" + CEND)
print(CGRN + str(numList) + CEND)
print(CBLU + "LockBox::Action::Starting::PixelRand--WAIT_STOP_COMMAND(5_SECONDS):" + CEND)
sleep(5)
print(CBLU + "LockBox::Action::Starting::PixelRand--CONTINUE_PAST_COMMAND(0S):" + CEND)
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

print(CORG + "LockBox::Action::Starting::PixelRand//FailCount: " + str(numFail) + CEND)
print(CGRN + "LockBox::Action::Starting::PixelRand//SuccessTry_Parse() " + CEND)

# Getting image pixel counts
print("\nLockBox::Action::Starting::PixelDet//PixelCount")

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


################################################ BETA CHANNEL WORKLIST END ################################################


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
    temp = randint(0, 255)
    tempstr += finalList[temp]
print(CGRN + tempstr + CEND)

"""
Note for future reference
The string `finalList` contains the 256 numbers that should be used from now out, disregard most of the other lists and variables-
they're safe to overwrite now
"""
