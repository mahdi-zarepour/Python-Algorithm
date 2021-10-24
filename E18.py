"""

    One time pad Cipher

"""


import random


class OneTime:

    def encrypt(self, text):
        plain = [ord(i) for i in text]
        key = []
        cipher = []

        for i in plain:
            k = random.randint(1, 300)
            c = (i + k) * k
            cipher.append(c)
            key.append(k)
        
        return cipher, key

    def decrypt(self, chipher, key):
        plain = []
        
        for i in range(len(chipher)):
            p = int((chipher[i] - key[i] ** 2) / key[i])
            plain.append(p)
        
        result = ''.join([chr(i) for i in plain])
        return result






cipher, key = OneTime().encrypt('Mahdi')
print(cipher, key, sep='\n')

print(OneTime().decrypt(cipher, key))