## Coloured Text Variables
CEND = "\33[0m"
CRED = "\33[31m"
CORG = "\33[33m"
CBLU = "\33[34m"
CGRN = "\33[32m"
CMGT = "\33[35m"

## Imports
# Custom Libs & Data
from pyth.settings import genInf, settings # General Info, Image Location
from pyth.functions import cls, autoImageManifeset # Helps to index the image manifest in `Reading//settings.py`
print("LockBox::Action::Boot::GetLibs()[RESPONSE]: Custom Libs Loaded.")
from random import randint
from PIL import Image as imge # used to read image size
from tqdm import tqdm # progress bar
from time import sleep
from datetime import timezone
import datetime
print("LockBox::Action::Boot::GetLibs()[RESPONSE]: Premade Libs Loaded.")

## THE KEY GENERATION CLASS IS REEAAAAALL
# can we get much hi-er? so high, ooaahh, ooahhaoohh

class KeyGen():
	'Class that houses the Key Generator. Methods:\n\n`fetchKey()`,  `hideKey()`,  `generate()`'
	key = ""

	def __init__(self, key):
		self.key = key

	def setKey(self, key):
		'Manually set the key for the KeyGen class.'
		self.key = key

	def fetchKey(self):
		'Decrypt the key from the 3-image 10 pixel method (Aka, the 3x10 Method)'
		# work to actually find key in the 3-image method mumbo jumbo goes here
	
	def hideKey(self):
		'Encrpt the key using the 3x10 method.'
		# work to actually hide the key in the 3-image method mumbo jumbo goes here

	def generate(): # lmao cognitive complexity is at 35 / 15 maximum, whoopsy daisy
		'Generates a key to be used for encryption and decryption.'
		tempstr = ""
		numFail = 0
		
		# Version Printer
		print("LockBox::Action::Starting")
		print("LockBox::" + genInf["build"] + "/" + genInf["version"])
		print("LockBox::Action::Boot::GetLibs()")

		# LockBox::Action::Starting::ReadData//settings.py
		# Read from settings.py, and print collected imageLoc data to terminal
		print("\n\nLockBox::Action::Starting::Reading//settings.py")
		print(CBLU + "LockBox::Action::Starting::ReadData//settings.py: " + CEND)

		location = "./images/"
		imgLoc = autoImageManifeset(location) # manifest the images in the images folder

		setImp = ""
		for i in range(len(imgLoc)):
			setImp += str(imgLoc[i])
			setImp += ", "

		print(CGRN + str(setImp) + CEND) # print the manifest

		# LockBox::Action::EncLevel()
		# Prints the ecnryption level
		enclevel = settings["enclevel"] * 128 # enclevel is a surprise tool that will help us later
		print("\nLockBox::Action::ENCLEVEL(" + str(enclevel) + "x)")
		
		# LockBox::Action::PixelRand::CreateNum_S1()
		# Creating a random number to choose an image
		print("\nLockBox::Action::PixelRand//CreateNum_S1()")
		numList = []
		for i in range(1000):
			temp = randint(0, (len(imgLoc) - 1)) ## changed from 1 to 0, added -1, fixes bug outlined in bugReportLog_ID001.txt
			numList.append(temp)

		# LockBox::Action::PixelRand::CreateNum_S2()
		# Creating a random number to choose a pixel
		print("\nLockBox::Action::PixelRand::CreateNum_S2()")
		print(CBLU + "LockBox::Action::Starting::PixelRand//NumList: " + CEND)
		print(CGRN + str(numList) + CEND)
		print("lenOf(numList): " + CBLU + str(len(numList)) + CEND)

		temp = randint(0, len(imgLoc))
		imgNum = numList[temp]

		#LockBox::Action::ImageOpen()
		# Opening the images for use
		print("\nLockBox::Action::ImageOpen()")
		for i in range(len(imgLoc)):
			if(i == imgNum):
				image = imge.open(imgLoc[imgNum])
			elif(i != imgNum):
				numFail += 1
			else:
				true = true # i know this is bad, but i'm too lazy to fix it lmaooo (plus it works)

		# LockBox::Action::PixelRand::FailCount()
		# Checking how many images failed to open
		print("\nLockBox::Action::PixelRand::FailCount()")
		if(numFail != len(imgLoc)): # if at least one image succeeds
			print(CORG + "LockBox::Action::PixelRand::FailCount()[RESPONSE]: " + CEND + str(numFail) + " images failed to open.")
		elif(numFail == len(imgLoc)): # if all images fail
			print(CRED + "LockBox::Action::PixelRand::FailCount()[RESPONSE]: " + CEND + "All images failed to open. Please check your image manifest in `Reading//settings.py` and try again.")
			print(CRED + "ERROR_CODE::[CODE] | IMG_INDEX_RANGE_ERROR | Exit Code 1" + CEND)
			sleep(15)
			exit()
		print(CGRN + "LockBox::Action::PixelRand::FailCount()[RESPONSE]: " + CEND + "SuccessTryParse()")
		
		# LockBox::Action::PixelData::PixelCounts()
		# Getting the pixel counts from the images
		print("\nLockBox::Action::PixelData::PixelCounts()")

		width, height = image.size # put image size from tuple into vars

		print(CBLU + "LockBox::Action::PixelData::PixelCounts()[RESPONSE]: " + CEND + "Image Size: " + str(width) + "x" + str(height))

		## LockBox::Action::PixelData::PixelColorData()
		# Getting the pixel color data from the images, storing it for use in a minute
		colorData = ""
		for i in tqdm(range(1024)):
			ranWI = randint(0, (width - 1))
			ranHI = randint(0, (height - 1))

			imgPix = image.convert('RGB') # convert to RGB
			r, g, b = imgPix.getpixel((ranWI, ranHI)) # tuple -> string to store RGB values
			colorData += str((r + g + b)) # stores in string colorData
		print(CGRN + str(colorData) + CEND)

		## LockBox::Action::FinalNumList()
		# Creating the final number list
		print("\nLockBox::Action::FinalNumList()")
		fNL = [] # stands for final number list
		for i in range(enclevel * 2): # generate numerical key based around enclevel times two
			temp = randint(1, (len(colorData) - 1))
			char = colorData[temp]
			fNL.append(char)
		
		## LockBox::Action::KeyCharGen()
		# Turns numerical list into one with chars & numbers based around the % of a timestamp
		print("\nLockBox::Action::KeyCharGen()")
		charList = "" # the list of chars & numbers that make up the key

		dt = datetime.datetime.now(timezone.utc) # get current time (in whatever PST or MST bs)
		dt_utc = dt.replace(tzinfo=timezone.utc) # convert to UTC
		dts = dt_utc.timestamp()
		dts = dts.__round__()

		# i know this was the shittest way to do it, but i'm wayy too over my head rn to improve it
		# plus I can barely get it working, it's less reliable than a Ford (We all know what ford stands for)
		# IT WASN'T THIS BAD B4 WHY DOES IT SUCK NOW
		# I DON'T EVEN KNOW WHY THIS SHIT WORKS??? IT JUST DOES????? BUT NOT PROPERLY?!?!?!?
		if(dts % 2 == 0): # if the timestamp is even
			for i in tqdm(range(len(fNL))):
				tempChar = fNL[i]
				if(i % 2 == 0): # if the index is even, do this stuff
					if(tempChar != 0): # if the char is not 0, multiply by a random number, get said numbers char value, and add it to charList
						tempChar = round(int(tempChar) * randint(99, 1000))
						charList += str(chr(int(tempChar))) # THIS LOOKS RETARDED LMAOOOO (does it even work?)
					elif(tempChar == 0): # if the char is 0, set to random number and do the same
						tempChar = randint(1, 9)
						tempChar = round( tempChar * randint(99, 1000))
						charList += str(tempChar)
				elif(i % 2 != 0): # if the index is odd, skip this iteration
					continue

		elif(dts % 2 != 0): # if the timestamp is odd
			for i in tqdm(range(len(fNL))):
				tempChar = fNL[i]
				if(i % 2 != 0): # if the index is odd, do this stuff
					if(tempChar != 0): # if the char is not 0, multiply by a random number, get said numbers char value, and add it to charList
						tempChar = round(int(tempChar) * randint(99, 1000))
						#print(CMGT + str(tempChar) + CEND) ## DEBUG LINE -- FOR TESTING ONLY!!! L##
						charList += str(chr(int(tempChar))) # THIS LOOKS RETARDED LMAOOOO (does it even work?)
					elif(tempChar == 0): # if the char is 0, set to random number and do the same
						tempChar = randint(1, 9)
						tempChar = round(tempChar * randint(99, 1000)) 
						charList += str(tempChar)
				elif(i % 2 != 0): # if the index is odd, skip this iteration
					continue
		
		## LockBox::Action::KeySet()
		# Sets the key to the generated key
		print("\nLockBox::Action::KeySet()")
		KeyGen.key = charList

		## LockBox::Action::Cleanup()
		# Deletes RAM-heavy vars and closes images
		print("\nLockBox::Action::Cleanup()")
		
		# del all the resource-heavy vars
		del(numList)
		del(fNL)
		del(charList)
		del(colorData)

		# close all the images opened
		image.close()