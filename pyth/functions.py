import os
import os

def cls():
    'Clears the CLI.'
    os.system("cls")

def autoImageManifeset(location):
    'Scans the number and names of all images inside of the specefied directory, and puts them into a returned array.\n\nUsage: autoImageManifest(location)'
    numFiles = 0
    fileLocAr = {}

    # Scanning for no of files in directory using os.listdir
    for path in os.listdir(location):
        if os.path.isfile(os.path.join(location, path)):
            numFiles += 1
    
    # Getting file names and types & adding to array
    for i in range(numFiles):
        tempString = "./images/" + str(i) + ".jpg"
        fileLocAr[i] = tempString
    
    # Returning file locations in dictionary
    return fileLocAr