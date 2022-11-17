class EncDec():
    'Class that houses the main Encryption and Decryption methods for LockBox. Usage: `EncDec.crypt(key, location)`, `EncDecName.decrypt(key, location)`'

    def __init__(self, keyIn, locIn):
        'Init class for EncDec.'
        self.__key__ = keyIn
        self.__location__ = locIn

    def updateDat(self, keyIn, locIn):
        'Updates location and key for EncDec.'
        self.__key__ = keyIn
        self.__location__ = locIn

    def crypt(self, __key__):
        'The main encryption algorithym for LockBox.'
    
    def decrypt(self, __key__):
        'The main decryption algorithym for LockBox.'