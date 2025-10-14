# LockBox

LockBox is a multi-faceted (Asym & Sym) encryption suite designed for simplicity and adaptability to all user needs. 

Despite it's originating code being written in Python (DefSec nerds cry your heart out!), LockBox is designed to be easily translatable to other languages and platforms, to ensure east of user use. As such, (Most) features from one language or platform are designed to be translateable to another- With minor exceptions, such as slight changes in the GUI (Such as changing from **Python's TQDM** to **C++'s Qt Progress Bars**).

After the first v1 Python release (And subsequent bugfixes), I plan to port the code to more popular languages for more popular and adaptable systems, specifically **C++** and **Java**. However, I would also encourage other devlopers to port the code to *(Quote unquote)*, "Better Languages", such as **Rust** and a .DOTNET language like **C#**.

### How It Works

[Put info here once you figure out how to make it work ;)]

## Code SubSection & To-Do List

- [X] **LockBox-Crypt v2.1 (CSRNG)**
  - Cryptographically Secure Random Number Generator- Uses multiple entropic numeric sources to generate a random number of a specified length. 
  - **Sub-Changelog:**
    - Micro-ized the code; `ranNum` & `ranNumST` Functions Occupy < 80 Lines (6Kb)
    - Integrated Security Test function to verify clean distribution of digits & cryptographic security; Can specify generated number length, number of iterations, and end tolerance level (Defaults 128, 1000, 2%)
- [ ] **LockBox-EncryptiCode v0.2**
  - To replace old Enc/Dec Class & System. Newer, cleaner, and more secure- No longer uses completely arbitrary methods of encryption, instead uses structured asym/sym depending on user usecase- Designed to be expandable. 
  - **Sub-Changelog:**
    - Created skeleton of EC Class