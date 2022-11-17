# LockBox - A Personal Server Security Solution

## Design

### What it Does

LockBox is an encryption method that is designed to run standalone or as a method inside of another Python program.
It takes a string-based input (Input *can* be an `int`, but will return as an `str`).
This is taken through our encryption algorithim to try and make data secure in a 256-bit format.

### How it Works

LockBox first generates random numebrs as best as it can, several times over again to find a true random number.
It then looks at pixels of an image, and finds random pixels out of a random image out of a random selection of images- Really, really random.
Using these found pixels, it takes their RGB values and generates a key out of those colour values, as well as more random numbers.
Through this key, it encrypts your data into a long and secure string, only decryptable via the same key.
