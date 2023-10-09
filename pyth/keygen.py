## Coloured Text Variables
CEND = "\33[0m"
CRED = "\33[31m"
CORG = "\33[33m"
CBLU = "\33[34m"
CGRN = "\33[32m"
CMGT = "\33[35m"

let = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"] # array of all english letters

# homebrewed libs
from pyth.settings import genInf, settings # General Info, Image Location
from pyth.functions import cls, autoImageManifeset # Helps to index the image manifest in `Reading//settings.py`

# other libs
from random import randint
from PIL import Image as imge # used to read image size
from tqdm import tqdm # progress bar
from time import sleep
from datetime import timezone
import datetime

## idk if it's smart to keep keygen as a class
## but i'm not a smart man
## SO HERE WE GO
class KeyGen():
    