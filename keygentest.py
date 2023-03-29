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
    test1 = True
else:
    testsPassed += 0
    test1 = False

#test2
print(CM+"\n\nTEST 2: Key Characters"+CE)
print(KeyGen.key)
inputv = input(str("IS THIS TEST PASSED (Y/N)? "))
if(inputv == "Y"):
    testsPassed += 1
    test2 = True
else:
    testsPassed += 0
    test2 = False

#test3
print(CM+"\n\nTEST 3: Key Length"+CE)
print("Actual: " + str(len(KeyGen.key)))
print("Expected: " + str(settings["enclevel"]*128))
if(len(KeyGen.key) == settings["enclevel"]*128):
    testsPassed += 1
    test3 = True
else:
    testsPassed += 0
    test3 = False

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
print(CM+"\n\nTESTS PASSED: " + CE +str(testsPassed) + "/" + str(totalTests))
print(CM+"TESTS FAILED: " + CE + str(totalTests-testsPassed) + "/" + str(totalTests))
print(CM+"SUCCESS RATE: " + CE+ str((testsPassed/totalTests)*100) + "%")
print("")
print(CM+"TIME ELAPSED: " + str(round(endTime - staTime, 2)) + "s" + CE)
print(CM+"TEST COMPLETED: " + str(datetime.datetime.now()) + CE)

print("\n\nBreakdown of Tests:")
print(CM + "TEST 1 FAIL/PASSSED:  " + CE+ str(test1))
print(CM + "TEST 2 FAIL/PASSSED:  " + CE+ str(test2))
print(CM + "TEST 3 FAIL/PASSSED:  " + CE+ str(test3))