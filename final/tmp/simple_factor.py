#!/usr/bin/env python3
import random

import gmpy2
from Crypto.Util.number import bytes_to_long, getStrongPrime, \
                                inverse, long_to_bytes

class RSA():
    def __init__(self):
        self.N = 0
        self.p = 0
        self.q = 0
        self.e = 0
        self.d = 0
        self.generate_key()

    def generate_key(self):
        print('Generating key..')
        self.N = 0
        self.d = -1
        while self.d < pow(self.N, 0.292):
            self.p = getStrongPrime(1024)
            self.q = gmpy2.next_prime(self.p + random.getrandbits(520))
            self.N = self.p * self.q
            self.e = 0x10001
            self.d = inverse(self.e, self.N - self.p - self.q + 1)

    def encrypt(self, plaintext):
        ciphertext = pow(bytes_to_long(plaintext), self.e, self.N)
        return ciphertext

    def decrypt(self, ciphertext):
        plaintext = long_to_bytes(pow(ciphertext, self.d, self.N))
        return plaintext

with open('./flag', 'rb') as f:
    flag = f.read()

rsa = RSA()

def main():
    print('Welcome to dream\'s RSA server')

    while True:
        print('[1] Generate key')
        print('[2] Encrypt flag')
        print('[3] Get info')

        menu = input('> ')

        if menu == '1':
            rsa.generate_key()
        elif menu == '2':
            print('encrypted flag:', rsa.encrypt(flag))
        elif menu == '3':
            print('N:', rsa.N)
            print('e:', rsa.e)
        else:
            print('Nope')

if __name__ == '__main__':
    main()
