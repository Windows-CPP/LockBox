from random import randint
from time import time
from tqdm import tqdm

## coloured text vars
CEND = '\u001b[0m'
CRED = '\u001b[31m'
CGRN = '\u001b[32m'
CBLU = '\u001b[34m'

###############################################################
def ranNumGen(numdigits):
    'Custom, cryptographically-secure random number generator.'

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
            rannum += makeShitHappen()
        elif(len(str(rannum)) > numdigits):
            rannum = str(rannum)
            rannum = rannum.replace(rannum[randint(0, len(rannum)-1)], "")
            rannum = int(rannum)
        else:
            break
    
    return rannum

###############################################################
## runtest vars
ranGen = True

def runTest(ranGen):
    'Runs tests of specified functions.'


    if ranGen:
        print(f"{CBLU}CURRENT TEST: RANNUMGEN(){CEND}")
        tstcnt = 1000
        t_length = 10
        
        bins = [] # binaries
        bins_l = "" # length of each integer

        # generate numbers and turn into integers
        for i in tqdm(range(tstcnt)):
            bins.append(ranNumGen(t_length))
        
        print(str(bins))
        print(f"{CBLU}TEST 1: LENGTH CONSISTENCY{CEND}")
        print(f"TARGET: {t_length}")

        pas = 0
        fal = 0

        for i in range(len(bins)):
            bins_l = str(len(str(bins[i])))
            if bins_l == str(t_length):
                pas += 1
            else:
                fal += 1
        print(f"TEST 1 RESULTS: {pas} PASS / {fal} FAIL")
        if(pas == tstcnt):
            print(f"{CGRN}TEST 1 PASSED{CEND}")
        else:
            print(f"{CRED}TEST 1 FAILED{CEND}")

###############################################################
runTest(ranGen)