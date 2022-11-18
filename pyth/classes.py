class EncDec():
    'Class that houses the main Encryption and Decryption methods for LockBox.\n\nUsage: `EncDec.crypt(key, location)`, `EncDecName.decrypt(key, location)`'

    def __init__(self, keyIn, locIn):
        'Init class for EncDec.'
        self.__key__ = keyIn
        self.__location__ = locIn

    def updateDat(self, keyIn, locIn):
        'Updates location and key for EncDec.'
        self.__key__ = keyIn
        self.__location__ = locIn

    # Possible way to do 256x encryption-
    # Index # of charachters in document
    # Take current indexed charachter and find it's char value
    # Add number if <= 6, subtract number if >=5
    # Add charachter to spot
    # Repeat for every number in FinalList until original charachter is 256 different charachters
    def crypt(self, __key__):
        'The main encryption algorithym for LockBox.'
    
    def decrypt(self, __key__):
        'The main decryption algorithym for LockBox.'

class DataSend():
    'Sends encrypted data via the LKBX// protocol.'