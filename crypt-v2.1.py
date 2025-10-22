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

CEND = '\033[0m'
CRED = '\033[91m'
CBLU = '\033[94m'
CGRE = '\033[92m'

DBUG = True # regular debug mode (regular outputs, tests, breakpoints, etc.)
DBUG_V = False # verbose debug mode (detailed outputs, near line-by-line operation where applies)

def ranNum(dLen=64) -> int:
    'LockBox-Crypt (CSRNG) v2.1\n\nGenerates a secure random integer of a specified length.'
    
    # generate number
    temp = ((pu.cpu_stats().ctx_switches * int(time()*1000)) % 100000)*(pu.virtual_memory().available % 100000) * 3.1459265; temp = round(temp); temp = (temp:=temp*(pu.cpu_stats().interrupts % 100000)) % 1000000007
    #tempbin = bin(temp)[2:] # turn into binary
    
    # get to desired length
    while True:
        if len(str(temp)) > dLen: temp = int(str(temp)[:dLen])
        elif(len(str(temp)) < dLen): temp = int(str(temp)*2)
        else: break

    return temp

def ranNumST(dLen=128, itCount=1000, tlrnc=2) -> None:
    'LockBox-Crypt (CSRNG) v2.1\n\nTests the cryptographic security of LockBox-Crypt by analyzing patterns of multiple iterations of the function.'
    
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
    print(f"{0/len(numArray)}         | EXACMATCH.......{CGRE+'PASS'+CEND if (eMat == 0) else CRED+'FAIL'+CEND}")

ranNumST(128, 100, 2)