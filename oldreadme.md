# LockBox - A Personal Server Security Solution

## Design

### What it Does

LockBox is an encryption tool that is designed to be run as either a standalone program or as a server-side encryption protocol.
It takes any string-based input (Input *can* be another type of input (Whether it be `bin`, `int`, or `double`),
but will return as a string once encrypted & decrypted), and turns it into a long binary string based off of several factors,
including image R,G,B values & ASCII values of the string.

A variable **enclevel** by multiples of x128 (E.g., x256, x512, etc.). In turn, every single value
in the string will be a multiple of 128 long (1 letter turns into 128 letters, for example). For best use, use x256 encrpyption
(enclevel of 2), as x256 is modern-day military-grade encryption available to all via other encryption solutions like AES-256.

Another variable is the **Image Generation Factor** (IGF). The IGF is a set variable (Just like the enclevel) that factors the size of the
images generated later in the encryption proccess. The IGF is a multiple of 16, going up exponentially. The reccomended IGF is 8, as 16*8=128,
which would be a 128x128 image- 16,384 pixels in total for use in the IS-ESA.

### How it Works

#### TL;DR: It's complex, but it works

If you don't have time, here's a quick run-through, using an `enclevel` of 2, and an `IGF` of 8.

1) LockBox takes the string input, and converts it to binary for later use.
2) It then creates the RNA, or Random Number Array. This is a large array of random numbers, based around the `enclevel` variable.
3) Several images based around the RNA are created. The size of the images is based around the `IGF` variable (128x128 in this case).
4) One image is chosen to house the IS-ESA, as well as create the EncDec key. The key is created by using the R,G,B values of the image.
5) The key is then used to encrypt the string, and the IS-ESA is hidden in the image, while the binary string is turned into a normal string.
6) This string is then combined with the ES-ESA.
7) The final string, as well as the 3 to 5 images are then returned to the user.

Taking into account the images are 128x128 pixels, there are over 16,384 pixels that can be used to hide the IS-ESA.
Even more in-depth, every one of those pixels can occupy 3 different component values of the R,G,B scale, which is 16,777,216 different values
in total.

That means that in-total, there are 274,877,906,944 different combinations of R,G,B values that can be used to hide the IS-ESA.
That's 274 Billion different combinations, and that's just for one image. There are 3 to 5 images used in the encryption process, resulting in a
theoretical total of anywhere from 824 Billion to 1.37 Trillion different combinations of R,G,B values that can be used to hide the IS-ESA.

#### The Whole Shebang

LockBox first creates a large array of random numbers. The size of this array is based around the multiple of 128 you choose to
encrypt your data by. This array is ran over several times by a random number generator to ensure that the numbers are as random as possible.

Once the Random Number Array (RNA) is made, LockBox then generates several (Baseline of 3, up to 5) images based around the RNA. These images are 128x128 pixels, each pixel a different R,G,B colour value, each representing a different code when *"Decrypted"* via an internal algorithm.

One image is then selected to be used for Key Generation. The R,G,B values of the image are decoded via the same algorithm as before,
and the code generated from the images is used to create both the Encryption/Decryption key, as well as the
**Image-Side Encryption String Appendage** (IS-ESA). The ESA is a two-part code hidden in both the original image used to generate the key
(Named the IS-ESA), and the encrypted string itself (Named the ES-ESA). When both the IS-ESA and ES-ESA are available to the LockBox decryptor,
it combines information from the ES-ESA and the IS-ESA to create decryption instructions, which are then used to decrypt the string.

Complex, I know, but everything for the safety of data!
