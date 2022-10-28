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
            if(__tempString__[i] == '1'):
                __tempString__[i] = 'temp' # How do we do this using the key? We need to make an algor
            if(__tempString__[i] == '2'):
                ''
            if(__tempString__[i] == '3'):
                ''
            if(__tempString__[i] == '4'):
                ''
            if(__tempString__[i] == '5'):
                ''
            if(__tempString__[i] == '6'):
                ''
            if(__tempString__[i] == '7'):
                ''
            if(__tempString__[i] == '8'):
                ''
            if(__tempString__[i] == '9'):
                ''
            if(__tempString__[i] == '0'):
                ''