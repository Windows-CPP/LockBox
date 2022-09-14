# Imports
from time import time, sleep
from random import randint, choice
from json import dumps, loads, load
from os import system
#from gpio4 import GPIO # Used to control GPIO buttons
from cryptography.fernet import Fernet
from encrypted_files.lockbox_settings import KeyLocations # Encryption/decryption method
from terminal import LB_Terminal # The terminal that allows commands to be run

# Note: Designed to run on Ubuntu Server 22.14+

# Settings JSON (JEPY)
SET_JSON_KEY = "b'p9pnL3dRhJBfbnS3j034gCO9U9LeH6lwhpb9JFT45UM='"
SET_JSON_LOC = "C:\Users\StG_44\Desktop\Project Lockbox\LockBox_Code\encrypted_files\lockbox_settings.py"

# Code Locations (JEPY)
PWORD_LOC = "" # Main password location
MAN_TFA_LOC = "" # Manual 2FA passcode location
REM_TFA_LOC = "" # Remote 2FA code location
REC_CODE_LOC = "" # Recovery passcode location

# General Variables
network_connection = False # If the Pi is network-enabled. Disabled with code `DISNET()`, enabled with `ENANET()`.
tfa_lock = True # Whether the 2FA has been bypassed by activation- Manual or remote. Relocked with code `SIGNOUT()`
rem_tfa = False

# Coloured Text Variables
CEND = "\33[0m"
CRED = "\33[31m"
CBLU = "\33[34m"
CGRN = "\33[32m"

def encrypt_dat(location, key):
    "Encrypt the specified file"

    file = open(SET_JSON_LOC, "r")
    fernet = Fernet(SET_JSON_KEY)
    encMessage = fernet.encrypt(file.encode())
    file.close()

    file = open("/encrypted_files/lockbox_settings.jepy")
    file.write(encMessage)
    file.close()

def decrypt_dat(location, key):
    "Decrypt the specefied file"

### MAIN ###
print("Booting...")

# Decrypts the JEPY format of the settings file, makes it Python, and imports it
# Afterwards, it deletes the Python file
print("15% | Decrypting and importing LOCKBOX settings...")
encrypt_dat(SET_JSON_LOC, SET_JSON_KEY) # temporary to encrypt the file

"""
from encrypted_files.lockbox_settings import Keys, KeyLocations, Settings # imports the required scheiße



print("25% | Locating level 2 key locations...")
version = Settings.version
# Key-Storing Variables
mainPW_Loc = KeyLocations.mainPW
man2FA_Loc = KeyLocations.man2FA
recovr_Loc = KeyLocations.recovr

print("35% | Copying level 2 decryption keys...")
mainPW_Key = Keys.mainPW
man2FA_Key = Keys.man2FA
rem2FA_Key = Keys.rem2FA
recovr_Key = Keys.recovr

print("45% | Deleting decrypted Python file...")
# add deletion code here ig

print("50% | Decrypting level 2 decription keys...")
"""