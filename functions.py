from typing_extensions import Self


class Encryptor():
    'Class in charge of encrypting data'
    __key__ = ""

    def __init__(self, key):
        'Init func for Encyptor'
        self.key = key

    def encrpt(self, textString):
        'Method that encrypts data using key'
        for i in range(len(textString)):
            'temp_placeholder'