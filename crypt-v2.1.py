"""
LockBox-Crypt v2.1
Cryptographically-Secure Random Number Generator (CS-RNG)

Last Major: Oct. 14, 2025
License: WTFPLv2 <http://www.wtfpl.net/txt/copying/>

Designed to securely generate random numbers for use in security applications. 
Homebrewed version of the Python 'secrets' module, uses entropic numbers from the host machine to ensure randomness.
Requires PSUTIL (For both) and TQDM (For SecureTest). 
"""

from time import time
import psutil as pu
from tqdm import tqdm

CEND, CRED, CBLU, CGRE = '\033[0m', '\033[91m', '\033[94m', '\033[92m'

DBUG = True # regular debug mode (regular outputs, tests, breakpoints, etc.)
DBUG_V = False # verbose debug mode (detailed outputs, near line-by-line operation where applies)


## num & token gens
def ranNum(dLen=64, min=-1, max=-1) -> int:
    'Generates a secure random integer of a specific length.\n\nNOTE: min & max can result in infinite loop if not properly set. Ensure that the range between min & max can accommodate the digit length specified by dLen.'
    
    while True:
        # generate number
        temp = ((pu.cpu_stats().ctx_switches * int(time()*1000)) % 100000)*(pu.virtual_memory().available % 100000) * 3.1459265; temp = round(temp); temp = (temp:=temp*(pu.cpu_stats().interrupts % 100000)) % 1000000007
        #tempbin = bin(temp)[2:] # turn into binary
        
        # get to desired length
        while True:
            if len(str(temp)) > dLen: temp = int(str(temp)[:dLen])
            elif(len(str(temp)) < dLen): temp = int(str(temp)*2)
            else: break

        # check if min/max valid
        if(min == -1 or max == -1): # no min/max specified; skip this step
            return temp
        else: # min/max specified
            if(temp >= min and temp <= max): # within range
                return temp
            elif(temp < min or temp > max): # out of range; regenerate number
                temp = ((pu.cpu_stats().ctx_switches * int(time()*1000)) % 100000)*(pu.virtual_memory().available % 100000) * 3.1459265; temp = round(temp); temp = (temp:=temp*(pu.cpu_stats().interrupts % 100000)) % 1000000007
                continue


"""
- [ ] token generation
    - [ ] byte tokens (v2.3)
    - [ ] hexadec tokens (v2.4)
    - [ ] url-safe tokens (v2.5)
- [ ] ranGenST - make work for token generation (crypt v2.2)
    | currently, ranNumST only works for pure numbers due to the subfunc of the digit distribution check only having 0-9 as valid
    | digits. could rework with a real-time dictionary, where if a new character is found, it is added to a dict with a count
    | of occurances, as opposed to a static list of every possible character- this also ensures that the distribution check
    | will only count distribution of characters that actually appear in the generated tokens, as opposed to fucking up the 
    | distribution percentages by including characters that never appear
    |
    | not a lot of work, but will end up being a complete rework of that section of code- do this before working on token gen
    |
    | python 'secrets' does not have a test function, so this will be a unique (maybe pointless) feature of LockBox

"""
def ranToken(tkTp='url', dLen=64) -> None:
    'Generates a secure random token of a specified length & type.'
    
    # since a byte can hold 256 values, generate a single bit to represent hundreds place;
    # if int <=3, then XX; if int >3 & <=7, then 1XX; if int >7, then 2XX
    # then, generate the required number as an int between the min & max above, convert to a byte value
    # repeat as many times as dLen specifies
    if(tkTp=='byt'):
        temp = b''
        while True:
            sT = ranNum(1)
            if(sT <= 3):
                temp = (ranNum(2, 0, 99)).to_bytes(1, 'big')
            elif(sT > 3 and sT <= 7):
                temp = (ranNum(3, 100, 199)).to_bytes(1, 'big')
            else:
                temp = (ranNum(3, 200, 255)).to_bytes(1, 'big')
            

            print(f"{len(temp)} / {temp}")
            if(len(temp) == dLen):
                return temp
            else:
                temp = b''
    
    # generates a hexadecimal token of length dLen; look more into this later
    elif(tkTp=='hex'):
        pass

    # generates a url-safe token of length dLen; maybe have a dictionary of valid characters to choose from, then 
    # generate a number to use as an index to pick from the dict, repeat dLen times
    # this one is easier than the hex one lol
    elif(tkTp=='url'):
        pass
    else:
        return None

## num & token tests
def ranGenST(dLen=128, itCount=1000, tlrnc=2) -> None:
    'Tests the cryptographic security of LockBox-Crypt by analyzing patterns of multiple iterations of the function.'
    
    numArray = []
    for i in tqdm(range(itCount), desc="ranNumSecureTest"):
        numArray.append(ranNum(dLen))
    
    # get number distibution
    numDist = [0,0,0,0,0,0,0,0,0,0]
    numPerc = [0,0,0,0,0,0,0,0,0,0]
    for i in numArray:
        for j in str(i):
            numDist[int(j)] += 1
    # get distribution percentages
    for i in numDist:
        numPerc[numDist.index(i)] = round((i/sum(numDist))*100,2)

    # num dist info
    if(DBUG):
        print(f"DBUG:NumTests()::SelRunArray:[numarry]")
        print(f"Number Distribution (i): {numDist} | ChkSm-{sum(numDist)}/{dLen*itCount}")
        print(f"Number Distribution (%): {numPerc}") 
        numDistCpy = numDist.copy(); numDistCpy.sort()
        print(f"3 LST Frequent Digits: {[numDist.index(numDistCpy[i]) for i in range(3)]} | Occurences: {[numDistCpy[i] for i in range(3)]}")
        print(f"3 MST Frequent Digits: {[numDist.index(numDistCpy[-(i+1)]) for i in range(3)]} | Occurences: {[numDistCpy[-(i+1)] for i in range(3)]}")
        
        input(f"Analysis Complete: Test Results Below. Press ENTER to continue.") if DBUG_V else print(f"Analysis Complete: Test Results Below.")
        print(f"{sum(numDist)}/{dLen*itCount} | CHKSUM..........{CGRE+'PASS'+CEND if (sum(numDist) == dLen*itCount) else CRED+'FAIL'+CEND}")
            
    # numeric consistency / tolerance check
    tollvl = (tlrnc/100)*(itCount*dLen/10)
    print(f"TLRNC LVL: {tollvl} ({tlrnc}%)")
    for idx, val in enumerate(numPerc):
        if(DBUG_V): input(f"NumPerc[].indexDigit(): {val} | {tlrnc+10}/{10-tlrnc} | {val}")
        if val < (10-tlrnc) or val > (10+tlrnc):
            print(f"DGT{idx}        | TLRNCE..........{CRED+'FAIL'+CEND} | {val} / {round(val-(10+tlrnc), 2) if (val > (10+tlrnc)) else round((10-tlrnc)-val, 2)}%; {10+tlrnc}/{10-tlrnc}")
        else:
            print(f"DGT{idx}        | TLRNCE..........{CGRE+'PASS'+CEND}")
    print(f"Number Distribution: {numPerc}")

    # exact matches check
    eMat = 0
    for i in range(len(numArray)):
        for j in range(i+1, len(numArray)):
            if numArray[i] == numArray[j]:
                eMat += 1
    print(f"{0}/{len(numArray)}       | EXACMATCH.......{CGRE+'PASS'+CEND if (eMat == 0) else CRED+'FAIL'+CEND}")
    return None
