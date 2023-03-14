## Imports
from tqdm import tqdm

class ED():
	'The main Encryption/Decryption class. \n\nUses: `Encrypt()`, `Decrypt()`'
	__key__ = [] # key to be used for encryption/decryption
	__location__ = "" # location of the file to be encrypted/decrypted

	# Init
	def __init__(self, keyIn, locIn):
		'Init class for EncDec.'
		__key__ = keyIn
		__location__ = locIn

	# Setters
	def setKey(self, keyIn):
		'Sets the key for the EncDec class.'
		__key__ = keyIn
	def setLocation(self, locIn):
		'Sets the location for the EncDec class.'
		__location__ = locIn
	def setEncLevel(self, enclIn):
		'Sets the encryption level for the EncDec class.'
		__enclevel__ = enclIn

	# Actual Stuff (not rdj stuff btw)
	def Encrypt(self):
		'Encrypts the given file using the key and location.'

	def Decrypt(self):
		'Decrypts the given file using the key and location.'