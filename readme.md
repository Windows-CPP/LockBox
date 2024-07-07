# LockBox - Open-Source and Simple Encyrption

## Design

### What It Does

LockBox is a symmetric-encryption algorithm *designed* to be run as a standalone program- E.g., in cases of local file encryption. However, under the license of LockBox, all users are allowed to customize it to their needs. 

### How It Works

LockBox works by using a custom, crytographically-secure random number generator to generate a symmetric key, based on values such as time since Unix epoch, the bit values of random RAM addresses, and more. 

This varies HEAVILY from former versions of LockBox, which used a unique method of random image generation as a way or storing and sharing keys- Which was both stupid and smart in equal rites. 

## To-Do List

- [ ] HandleFile()
  - Handles the file to-be encrypted. Mostly running checks to ensure memory stability, as well as preparing for padding.
- [ ] Padder()
  -  Uses either an ANSI-X.923 or a PKCS#7-style method of padding. 
- [ ] IntraVenous()
    - I kinda just like the name, but this is actually the Initilizing Vector. Similar to traditional encryption algorithms, the IV is prepended to the encrypted text to make it simple to remove during decryption. This is only to make the protocol much more adaptable, especially in cases of live data streams. 
- [ ] EncDec
  - The actual encryption and decryption code. This is going to be the hardest part, and will therefore take the longest. 
- [ ] Validate()
    - Simple validation script. Just decrypts the data and compares the results. Simple, quick, and effective. 