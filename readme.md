# LockBox - Open-Source and Simple Encyrption

## Design

### What It Does

LockBox is a symmetric-encryption algorithm *designed* to be run as a standalone program- E.g., in cases of local file encryption. However, under the license of LockBox, all users are allowed to customize it to their needs. 

### How It Works

LockBox works by using a custom, crytographically-secure random number generator to generate a symmetric key, based on values such as time since Unix epoch, the bit values of random RAM addresses, and more. 

This varies HEAVILY from former versions of LockBox, which used a unique method of random image generation as a way or storing and sharing keys- Which was both stupid and smart in equal rites. 

## To-Do List

- [X] PrepFile()
  - Small misnomer- Does not prep the file itself, instead gives a block size that the file will be broken into in order to encrypt it. This is almost entirely useless on modern systems, only really existing to support memory-limited and legacy systems.  
- [ ] Enc/Dec
  - The actual encryption and decryption code. This is going to be the hardest part, and will therefore take the longest. 
- [ ] Padder()
  -  Uses either an ANSI-X.923 or a PKCS#7-style method of padding. 
- [ ] Validate()
    - Simple validation script. Just decrypts the data and compares the results. Simple, quick, and effective. 