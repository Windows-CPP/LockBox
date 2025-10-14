## imports
from random import randint
from time import time
from tqdm import tqdm
from os import path 
from psutil import virtual_memory

## variables
# coloured text vars
CEND = '\u001b[0m'
CRED = '\u001b[31m'
CGRN = '\u001b[32m'
CBLU = '\u001b[34m'

# main file vars
loc = "test.txt"
block = 128 # block size in bytes; default 128 bytes


## functions
def ranNumGen(numdigits: int) -> int:
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

## used in Enc() and Dec() to read the file chunk by chunk
def proccessFileChunk(loc, block):
    'proccessFileChunk(str location, int read_block_size) -> None\n\nReads a file chunk by chunk and yields the chunk to the calling function.'
    with open(loc, "r") as f:
        while True:
            chunk = f.read(block)
            if not chunk:
                break
            yield chunk

def prepFile(loc: str, block: int) -> int:
    'prepFile(str location) -> int\n\nRuns memory and drive checks to ensure that the file is ready to be encrypted.'
    
    # check if file exists; if it does, get it's size
    if(path.exists(loc)):
        size = path.getsize(loc)
    # get free memory size
    mem = virtual_memory()
    mem = mem.available
    # compare
    if(size < mem):
        return 32 # break into 32-byte blocks (legacy for low-memory systems)
    else:
        return 128 # defaults to 128-byte blocks (standard)
    
def Enc(loc: str, block:int, read: int, key: int, ivt: int) -> None:
    'Enc(str location, int encrypt_block_size, int read_block_size, int key, init_) -> None\n\nEncrypts a file using a specified key and block size.'
    # process the file in chunks of [read] bytes (defaults to 128; set to 32 on legacy systems)
    for chunk in proccessFileChunk(loc, read):
        