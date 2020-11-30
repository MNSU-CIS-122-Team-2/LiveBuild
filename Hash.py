import os
import hashlib
import binascii
import sys
from base64 import b64encode


# gather arguments from input and it only takes the first 2
arglist = sys.argv
hash = str(arglist[1])

saltString = os.urandom(16)# generate random salt (makes hash unique) in bytes
salt = saltString.hex();# convert to hexadecimal to store in database

#printing the salt
print(salt)
bsaltedString = bytes.fromhex(salt);# convert to bytes for algorithm for hash

# creates hash based on random salt and argument
myKey = hashlib.pbkdf2_hmac('sha256', hash.encode('utf-8'), bsaltedString, 10000)

hashed = myKey.hex()
#printing the hashed password
print(hashed)
