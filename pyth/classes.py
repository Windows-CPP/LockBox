from tqdm import tqdm

class EncDec():
    'Class that houses the main Encryption and Decryption methods for LockBox.\n\nUsage: `EncDec.crypt(key, location)`, `EncDecName.decrypt(key, location)`'
    __key__ = []
    __location__ = ""
    __enclevel__ = 0


    def __init__(self, keyIn, locIn, enclIn):
        'Init class for EncDec.'
        self.__key__ = keyIn
        self.__location__ = locIn
        self.__enclevel__ = enclIn

    def updateDat(self, keyIn, locIn, enclIn):
        'Updates location and key for EncDec.'
        self.__key__ = keyIn
        self.__location__ = locIn
        self.enclevel = enclIn

    # Possible way to do 256x encryption-
    # Index # of charachters in document, Take current indexed charachter and find it's ASCII char value
    # Add number if <= 6, subtract number if >=5, Add charachter to spot
    # Repeat for every number in FinalList until original charachter is 256 different charachters
    def crypt(self):
        'The main encryption algorithym for LockBox.'
        newLoc = str(self.__location__ + "cryptal.txt")
        newFile = open(newLoc, 'x')
        opeFile = open(self.__location__, 'r')
        tempString = ""

        for i in tqdm(range(len(opeFile))):
            chara = opeFile[i]
            charaVal = ascii(chara)

            for b in range(self.__key__):
                newCharVal = charaVal + self.__key__[b]
                # Need to get this value back down to a range of ASCII character
                # Need a number I can divide this by to get it between the range of:
                # 0 - 
            tempString += newCharVal
    
    # For decryption-
    # Group the document into 256-byte sized chunks (256 characters per chunk), Use the opposite method of encryption- add number if >=, subtract if <= 6
    # If all 256 characters are the same, then replace all of them with just one of that character
    # Else, there is document corruption
    def decrypt(self):
        'The main decryption algorithym for LockBox.'

class DataSend():
    'Sends encrypted data via the LKBX// protocol.'