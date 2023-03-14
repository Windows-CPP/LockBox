# Changelog

## v0.6.3-b (Silent)

- Updated comments for legebility

## v0.6.4-b (Silent)

- Began process of moving ecnryption method from `lockbox_main` to `c_LockBoxAction`

## v0.6.5-b

### General

- Added gitignore
  - This makes it easier to ignore files I don't want uploaded lol
- 3x10 Key Encryption Method
  - Just allows me to hide the key's data in 10 pixels in 3 500x500 images, which is made more legible for human rememberance later on
  - More secure than saving the key somewhere and having to save another key somewhere else to decrypt it, wayy easier to find
  - Plus something like this would be smaller than most keys, so binary data doesn't need to be read by a human mind, and something like `GRN-(4x6,1x2),BLU-[etc...]` would be easier

### KeyGen Class

- Moved `KeyGen` class to own file
- Wrote a test for the `KeyGen` class
- Prepped two more methods: `fetchKey()` & `hideKey()` on top of main `generate()` function
  - `fetchKey()` works to decrypt the 3x10 key encryption method, while `hideKey()` does the oppposite and encrypts the key using the 3x10 method

### EncDec / ED Class

- Finally cleared out old code
- Prepped for updated code (Hopefully by v0.7.0-b on the wint branch)

### Plans

- By v0.7.0-b on the wint branch, I plan to:
  - Finish the KeyGen class (Specifically fetch & hide key methods)
  - Write tests for the fetch & hide key methods
  - Create the ED class methods for encryption and decryption
  - Write tests for the ED class methods
