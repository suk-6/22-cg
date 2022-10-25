#!/usr/bin/env python3
from Crypto.Cipher import AES
from Crypto.Util import Padding
import os

BLOCK_SIZE = 16

with open('penguin_and_flag.bmp', 'rb') as f:
    plaintext = f.read()

key = os.urandom(BLOCK_SIZE)

cipher = AES.new(key, AES.MODE_ECB)

ciphertext = cipher.encrypt(Padding.pad(plaintext, BLOCK_SIZE, style='pkcs7'))

with open('encrypted', 'wb') as f:
    f.write(ciphertext)
