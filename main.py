## imports
from random import randint
from time import time
from tqdm import tqdm

## variables
# coloured text vars
CEND = '\u001b[0m'
CRED = '\u001b[31m'
CGRN = '\u001b[32m'
CBLU = '\u001b[34m'


## functions
def ranNumGen(numdigits):
    'ranNumGen(int numdigits) -> int memBit\n\nGenerates a cryptographically secure random number with a specified number of digits. This function is highly inefficient, but when generating smaller numbers (5-10 digits), it remains relatively quick.'

    # turn epoch into one number (remove the decimal point)
    epoch = str(time()).replace(".", "") # epoch time
    epoch = int(epoch)

    # we're making this a function so it can be repeated as neccesary to reach the ideal number of digits (numdigits)
    def makeShitHappen():
        memBit = "0b"
        # generate random binary number
        for i in range(len(str(epoch))):
            epoch_s = str(epoch)[randint(0, len(str(epoch))-1)] + str(epoch)[randint(0, len(str(epoch))-1)]
            epoch_s = int(epoch_s)
            mask = 1 << 0
            is_set = (int(epoch_s) & mask) != 0
            if(is_set):
                memBit += "1"
            else:
                memBit += "0"
            
        # make binary number an integer
        memBit = (int(memBit, 2))
        return memBit

    # get to ideal number of digits (numdigits)
    rannum = makeShitHappen()
    
    while(len(str(rannum)) != numdigits):
        if(len(str(rannum)) < numdigits):
            rannum = str(rannum)
            rannum += str(makeShitHappen())
            rannum = int(rannum)
        elif(len(str(rannum)) > numdigits):
            rannum = str(rannum)
            rannum = rannum.replace(rannum[randint(0, len(rannum)-1)], "")
            rannum = int(rannum)
        else:
            break
        #print(str(rannum)) # debug print statement
    return rannum

def GenerateKey():
    'Generates a set of keys used for encryption.'