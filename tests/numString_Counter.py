# Counts the number of numbers in a given string
# Used to test lockbox_main.py/CreateNum()

baseStr = [0, 2, 2, 0, 0, 2, 2, 2, 0, 1, 2, 2, 2, 1, 2, 2, 0, 2, 1, 0, 1, 2, 1, 0, 2, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 2, 0, 2, 1, 0, 0, 2, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 1, 0, 0, 2, 1, 0, 2, 0, 2, 2, 2, 1, 0, 1, 1, 1, 0, 1, 2, 2, 0, 2, 1, 2, 2, 1, 2, 1, 2, 2, 2, 1, 0, 2, 1, 1, 1, 2, 0, 2, 0, 0, 1, 1, 0, 1, 1, 1, 0, 2, 0, 0, 2, 2, 0, 2, 0, 1, 0, 1, 1, 2, 1, 0, 2, 2, 1, 1, 2, 0, 1, 1, 2, 2, 0, 0, 2, 0, 1, 1, 1, 2, 1, 2, 0, 2, 1, 0, 2, 0, 0, 0, 2, 1, 1, 1, 2, 0, 1, 0, 1, 2, 0, 1, 2, 1, 0, 1, 1, 1, 1, 0, 2, 1, 1, 0, 0, 2, 1, 0, 2, 1, 2, 2, 2, 2, 2, 0, 1, 0, 2, 0, 1, 0, 1, 2, 0, 2, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 2, 1, 2, 0, 1, 0, 2, 0, 0, 1, 2, 0, 1, 1, 0, 0, 2, 1, 1, 0, 2, 2, 2, 1, 1, 0, 1, 1, 2, 1, 2, 1, 2, 2, 1, 1, 0, 0, 0, 0, 2, 1, 0, 0, 2, 0, 1, 0, 2, 1, 2, 0, 0, 2, 0, 2, 2, 1, 2, 2, 1, 2, 1, 2, 1, 0, 2, 2, 0, 0, 1, 1, 0, 1, 2, 2, 0, 0, 1, 0, 0, 1, 2, 2, 0, 1, 2, 0, 0, 0, 2, 2, 0, 2, 2, 0, 1, 2, 0, 1, 1, 1, 0, 0, 2, 1, 0, 0, 2, 0, 2, 0, 2, 2, 2, 0, 0, 0, 1, 1, 2, 0, 1, 1, 0, 1, 0, 1, 2, 0, 2, 1, 0, 0, 2, 1, 1, 0, 2, 1, 0, 2, 2, 2, 0, 2, 0, 1, 1, 0, 1, 2, 2, 2, 2, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 2, 0, 2, 0, 0, 1, 0, 1, 1, 2, 0, 2, 0, 1, 0, 0, 2, 0, 2, 2, 0, 2, 0, 2, 0, 1, 2, 1, 2, 1, 1, 0, 1, 2, 2, 2, 2, 1, 1, 2, 0, 2, 2, 2, 2, 1, 0, 1, 2, 1, 1, 0, 2, 0, 2, 2, 0, 2, 2, 2, 1, 0, 1, 0, 1, 0, 2, 1, 2, 0, 0, 1, 2, 0, 1, 0, 0, 2, 1, 2, 0, 0, 1, 2, 0, 2, 0, 2, 0, 1, 1, 0, 0, 0, 2, 0, 0, 2, 1, 2, 0, 1, 0, 1, 2, 0, 0, 1, 2, 2, 0, 0, 1, 2, 1, 1, 1, 1, 0, 2, 2, 1, 0, 2, 1, 1, 0, 1, 1, 0, 2, 0, 1, 2, 0, 1, 2, 2, 0, 1, 1, 1, 1, 0, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 1, 2, 0, 0, 0, 1, 2, 0, 0, 1, 0, 2, 0, 0, 2, 1, 2, 2, 1, 0, 1, 1, 2, 0, 2, 0, 1, 2, 1, 0, 1, 1, 2, 0, 1, 2, 1, 0, 1, 0, 2, 0, 0, 1, 1, 0, 2, 2, 0, 0, 1, 0, 0, 2, 2, 0, 2, 0, 2, 1, 2, 0, 2, 2, 1, 1, 2, 0, 2, 2, 1, 2, 1, 2, 2, 0, 2, 2, 0, 0, 1, 1, 0, 0, 1, 0, 0, 2, 2, 0, 2, 0, 2, 2, 0, 1, 2, 2, 2, 1, 1, 2, 0, 2, 0, 1, 2, 1, 2, 1, 1, 0, 2, 2, 1, 1, 2, 2, 2, 0, 0, 2, 2, 2, 2, 2, 0, 0, 1, 2, 1, 1, 1, 1, 2, 2, 2, 1, 0, 1, 2, 1, 2, 0, 1, 1, 2, 2, 2, 1, 1, 0, 1, 2, 0, 1, 0, 2, 1, 0, 0, 2, 2, 1, 0, 2, 1, 0, 1, 1, 1, 2, 1, 2, 0, 1, 0, 2, 1, 1, 2, 2, 1, 0, 0, 2, 1, 2, 2, 0, 0, 0, 1, 2, 2, 0, 1, 2, 2, 2, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 2, 1, 2, 2, 2, 1, 0, 0, 1, 1, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 2, 2, 1, 0, 2, 1, 1, 0, 2, 0, 1, 2, 0, 2, 1, 2, 1, 0, 1, 2, 1, 2, 2, 1, 0, 1, 0, 2, 2, 0, 1, 0, 1, 2, 2, 2, 0, 0, 0, 2, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 2, 2, 2, 0, 1, 1, 0, 2, 2, 1, 2, 1, 1, 2, 2, 1, 2, 0, 0, 1, 2, 2, 1, 0, 0, 2, 0, 0, 1, 2, 0, 1, 2, 0, 1, 1, 0, 1, 2, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 2, 1, 2, 1, 0, 0, 2, 2, 0, 2, 2, 1, 1, 2, 1, 2, 1, 1, 2, 1, 2, 2, 0, 2, 1, 1, 1, 2, 1, 2, 2, 2, 1, 2, 0, 1, 2, 1, 1, 2, 1, 2, 1, 1, 0, 2, 0, 2, 0, 2, 1, 1, 1, 1, 0, 2, 2, 0, 0, 2, 2, 0, 1, 2, 1, 0, 0, 2, 0, 0, 0, 2, 0, 1, 0, 2, 1, 0, 2, 0, 0, 2, 2, 2, 2, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 2, 0, 0, 2, 1, 2, 1, 1, 0, 2, 1, 2, 2, 1, 0, 2, 1, 1, 0, 1, 2, 2, 0, 2, 2, 1, 2, 1, 2, 0, 0, 0, 2, 2, 1, 1, 0, 2, 0, 2, 1, 1, 2, 0, 2, 1, 1, 2]
numList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
totalLen = len(baseStr)
numCount = 0

for i in range(len(baseStr)):
    if(baseStr[i] == numList[0:9]):
        numCount += 1

print("Total Length of String: " + str(totalLen))
print("# of Numbers in String : " + str(numCount))