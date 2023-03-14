## PLACE IN THE ROOT LOCKBOX DIRECTORY (where the pyth folder is) FOR THE TEST TO WORK!!!

from pyth.keygen import KeyGen
from pyth.settings import settings
import time
import datetime


CE = "\33[0m"
CM = "\33[35m"
testsPassed = 0 # num of tests passed
totalTests = 3 # total num of tests

staTime = time.time()

#test1
print(CM + "\n\nTEST 1: KeyGen.generate()"+CE)
keySamp = KeyGen.key
KeyGen.generate()
keyUpdt = KeyGen.key

if(keySamp != keyUpdt):
    testsPassed += 1
else:
    testsPassed += 0

#test2
print(CM+"\n\nTEST 2: Key Characters"+CE)
print(KeyGen.key)
inputv = input(str("IS THIS TEST PASSED (Y/N)? "))
if(inputv == "Y"):
    testsPassed += 1
else:
    testsPassed += 0

#test3
print(CM+"\n\nTEST 3: Key Length"+CE)
print("Actual: " + str(len(KeyGen.key)))
print("Expected: " + settings["enclevel"]*128)
if(len(KeyGen.key) == settings["enclevel"]*128):
    testsPassed += 1
else:
    testsPassed += 0

"""
#test4
print(CM+"\n\nTEST 4: Key Characteristics"+CE)
print("Key is type: " + str(type(KeyGen.key)))
print("Decimal Value: " + str(ord(KeyGen.key)))
inputv = input(str("IS THIS TEST PASSED (Y/N)? "))
if(inputv == "Y"):
    testsPassed += 1
else:
    testsPassed += 0
"""

endTime = time.time()

#totals
print(CM+"\n\nTESTS PASSED: " + str(testsPassed) + "/" + str(totalTests) +CE)
print(CM+"TESTS FAILED: " + str(totalTests-testsPassed) + "/" + str(totalTests) +CE)
print(CM+"SUCCESS RATE: " + str((testsPassed/totalTests)*100) + "%"+CE)
print("")
print(CM+"TIME ELAPSED: " + str(round(endTime - staTime, 2)) + "s" + CE)
print(CM+"TEST COMPLETED: " + str(datetime.datetime.now()) + CE)