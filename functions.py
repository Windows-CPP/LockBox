from typing_extensions import Self


class Encryptor():
    'Class in charge of encrypting data'
    __key__ = ""
    __tempString__ = ""

    def __init__(self, key):
        'Init func for Encyptor'
        self.__key__ = key

    def setSeed(self, key):
        'Changes the key that the encryptor uses'
        self.__key__ = key

    def encrypt(self, textString):
        'Method that encrypts data using key'
        
        __tempString__ = textString
        for i in range(len(textString)):
            for j in range(j):
                if(j > 9):
                    break
                # ecnryption functions go here