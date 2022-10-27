# LockBox - A Personal Server Security Solution

This program ensures network security when combined with a LockBox Case. 
(Note: LockBox Case 3D CAD included with this program.)

---
## Security Features

1) Network Connectivity Switch
2) Built-In 2FA Keypad
3) Remote 2FA System
4) Backup Reset Key System
5) Password + Code Encryption

---
## Requirements

- CPU     | ARM Single-Core @ 1.0 GHz or Higher
- RAM     | 1 Gb DDR3 or Higher
- Disk    | 20 Mb
- Network | WiFi Connection
- OS      | Designed for Ubuntu Server 18+

---
## Features

1. 7-Segment LCD Screen  | Shows network connection, SSH connections, RAP+CPU, and lock status

---
## Codes

The main menue of the system has a set of codes for ease-of-use. The codes are as follows:

`ENANET()` - Enable remote connections via WiFi + ZeroTier. Allows remote access via SSH.

`DISNET()` - Disable remote connections via WiFi + ZeroTier.

`SIGNOUT()` - Signout of current LOCKBOX session, re-lock 2FA, re-encrypt and delete decrypted files, and run `DISNET()` automatically.

`SSH()` - Check the number of SSH connections, their identities, and locations. 

`SSH_TERM()` - Terminates all active SSH sessions.

`REM_2FA()` - Whether remote 2FA while `ENANET()` is active is allowed. Takes one of two parameters: `True` and `False`. `False` by default. 

---
## Encryption / Decryption

How the full decryption process works (As of now):

1. The program is run. It locates the `LOCKBOX_SETTINGS.JEPY` file, and decrypts it using a key hard-coded into the program. 
2. Using the file locations decrypted from `LOCKBOX_SETTINGS.JEPY` (Now turned into a `.JSON` file), it finds the keys to decrypt each specefied `JEPY` file. 
3. Using these (Now unlocked) keys, the program can use `deCrypt_KEY()` to decrpyt key-holding files into a readable format. 
4. Once this is done, the specific key can be parsed through `deCrypt_JEPY()` to decrypt a specific `.JEPY` file into a readable `.JSON` file, where the passwords 
and passcodes can be found.

**Total Layers of Encryption**: 2

**Total Layers of 2FA**: 2 (Remote + Manual)


## Resources

**Encryption using Fernet** - https://www.geeksforgeeks.org/how-to-encrypt-and-decrypt-strings-in-python/


## Special Thanks

To **W3Schools** and **GeeksForGeeks** for guides relating to Usage of Fernet