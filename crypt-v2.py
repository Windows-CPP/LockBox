## LockBox-Crypt v2
from time import time
import psutil as pu
from tqdm import tqdm

# turn on/off debug inputs
DBUG = False

print(f"lockBox_subMod2_crypt v0.2")
print(f"last_update: sept-5-2025\n\n")

CBLU = '\033[94m'  # Blue
CGRE = '\033[92m'  # Green
CRED = '\033[91m'  # Red
CEND = '\033[0m'   # End color


"""
1) get random number (s) -> convert to 8-digit blocks -> modulus each digit (results in 1 or 0)
    convert binary to int -> put ints into 8-digit blocks

39182739192746581923817301928316 -> 39182739-19274658-19238173-01928316 -> 
11100111-11010110-11100101-00010100 -> 231-514-202-315-142-023-151-420-231-514-20... -> 
23151420-23151420-23151420-23151420-...

2) get cpu switch count -> get mean of digits -> multiply by 10 -> convert to 16-digit blocks
    convert 2-digit substrings to chars (based on alphanumerical index)

3) if int >= 5, place random char from step 2 after number; if int < 5, dont place char
"""
def ranNum(iKeyLen: int, KeyLen: int) -> int:
    'Generate a random integer of a specified length.'

    binStr = ""

    iram = pu.virtual_memory().available
    icpu = pu.cpu_stats().ctx_switches

    for i in range(iKeyLen): 
        iram=round(iram*pu.cpu_stats().interrupts)
        icpu=round(icpu*pu.virtual_memory().total)
        if DBUG == True: input(f"#DEBUG#:getStats(): ICPU: {str(icpu)} | IRAM: {str(iram)}")

        # get iram and icpu to a set length
        while True:
            if len(str(iram)) > iKeyLen or len(str(icpu)) > KeyLen: iram = int(str(iram)[:iKeyLen]); icpu = int(str(icpu)[:iKeyLen])
            if( len(str(iram)) < iKeyLen or len(str(icpu)) < KeyLen): iram = int(iram)*int(iram); icpu = int(icpu)*int(icpu)
            if(len(str(iram)) == KeyLen and len(str(icpu)) == KeyLen): break
        if DBUG == True: input(f"#DEBUG#:setStatLen(): ICPU: {str(icpu)} | IRAM: {str(iram)}")

        # modulate each digit by 2 to result in 1 or 0
        tempBinStr = ''
        i = 0
        while True:
            if i > len(str(iram)) and i > len(str(icpu)): break # if both strings are exhausted, break
            if len(str(tempBinStr)) >= iKeyLen: break # if tempBinStr is long enough, break
            if i <= len(str(iram)): tempBinStr += str(int(str(iram)[i])%2)
            if i <= len(str(icpu)): tempBinStr += str(int(str(icpu)[i])%2)
            if DBUG == True: input(f"#DEBUG#:modulusDigits():modulus(): TEMPBINSTR: {str(tempBinStr)} | TEMPBINSTR_LEN: {len(str(tempBinStr))}/{iKeyLen} |")
            i += 1
        binStr += tempBinStr
        if DBUG == True: input(f"#DEBUG#:modulusDigits(): BINSTR: {str(binStr)} | ICPU: {str(iram)} | IRAM: {str(iram)}")

        # construct binary string based on stats, convert to int
        i = 0

        # get binStr to a set length
        while True:
            if len(str(binStr)) > iKeyLen: binStr = int(str(binStr)[:iKeyLen])
            elif(len(str(binStr)) < iKeyLen): binStr = int(str(binStr)*2)
            else: break
            ## debug shit
        if DBUG == True: input(f"#DEBUG#:: binStrLen: {len(str(binStr))}/{iKeyLen} | binStr: {binStr}")

        # turn binStr into 4-digit blocks, then turn 4-digit blocks into integers
        tempStr = ""
        key = 0
        while True:
            if i > len(str(binStr))-1: break
            tempStr += str(binStr)[i]
            if i%4 == 0 and i!=0: key += int(tempStr, 2); tempStr = ''
            i += 1
        if DBUG == True: input(f"#DEBUG#:binToInt(): KEY: {str(key)} | BINSTR: {str(binStr)}")
        
        # get key to a set length
        while True: 
            if len(str(key)) > KeyLen: key = int(str(key)[:KeyLen])
            elif(len(str(key)) < KeyLen): key = int(str(key)*2)
            else: break

        # turn key into an integer, return
        key = int(key)
        return key


# ---------------------- TESTING AREA ---------------------- #
# checks: 
# 1) key length is correct
# 2) ensure no exact repeated keys
# 3) check for numerical bias / patterns

KEYS_TO_GENERATE, KEY_LENGTH = 10, 128
generatedKeys = []


print(f"{CBLU}BEGINING KEY GENERATION{CEND}")
stTm2 = time() # start timer
for i in tqdm(range(KEYS_TO_GENERATE)):
    generatedKeys.append(ranNum(KEY_LENGTH, KEY_LENGTH))

enTm2 = time() # end timer

print(f"GEN_TIME: {round(enTm2-stTm2, 2)}s")
print(f"{CBLU}BEGINING KEY ANALYSIS{CEND}")

# check all key lengths correct
wronLen = 0
stTm2 = time()
print(f"{CBLU}KEYLEN CHECK{CEND}")
for i in range (len(generatedKeys)):
    if len(str(generatedKeys[i])) != KEY_LENGTH:
        wronLen += 1

# check for exact repeated keys
repKey = 0
print(f"{CBLU}REPEATED_KEY CHECK{CEND}")
for i in tqdm(range(len(generatedKeys))):
    for j in range(i+1, len(generatedKeys)):
        if generatedKeys[i] == generatedKeys[j]: repKey += 1


# check for numerical bias / patterns
print(f"{CBLU}NUM_BIAS CHECK{CEND}")
numCount = [0]*10
for i in range (len(generatedKeys)):
    for j in range (len(str(generatedKeys[i]))):
        numCount[int(str(generatedKeys[i])[j])] += 1

# % each number appears
totalNums = sum(numCount)
for i in range (len(numCount)):
    numCount[i] = (numCount[i], round((numCount[i]/totalNums)*100, 2))


enTm2 = time()
print(f"{CBLU}CHECKS COMPLETE. ANALYSIS RESULTS:{CEND}")
print(f" ELAPS_TIME:{round(enTm2-stTm2, 2)}s")
print(f"KEYS_GEN: {len(generatedKeys)}/{KEYS_TO_GENERATE}")
print(f"WRON_LEN: {wronLen} | WRON_LEN_PCT: {round((wronLen/len(generatedKeys))*100, 2)}%")
print(f"KEY_DUPE: {repKey} | KEY_DUPE_PCT: {round((repKey/len(generatedKeys))*100, 2)}%")
print(f"NUM_BIAS: {numCount}")
print("\n\nTESTS COMPLETE. PRESS [ENTER] TO PRINT KEYS.")
input()
for i in range (len(generatedKeys)):
    print(f"KEY_{i+1}: {generatedKeys[i]}")