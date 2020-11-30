import os
import hashlib

import binascii
import sys
from base64 import b64encode


#gather arguments from input and it only takes the first 2
arglist = sys.argv

#assign arguments to defined strings
H_PASS = str(arglist[1])
SALT = str(arglist[2])
Pwd = str(arglist[3])

#assuming that we found a match. Assigning stored data to variables to be processed
#to compare later
StoredHashedPassword = H_PASS
StoredSalt = SALT;

#convert string to hex bytes to be used to generated the hashed password from the Pwd passed by user
bsalt = bytes.fromhex(StoredSalt)

#created a new hashed based on the input passed (Pwd) and the stored salt (StoredSalt)
ProcessedHashed = hashlib.pbkdf2_hmac('sha256',Pwd.encode('utf-8'),bsalt, 10000)

#if hashed value from db matches the processed hashed, then it is a valid login
if ProcessedHashed.hex() == StoredHashedPassword:
    print("Valid")
else:
    print ("Invalid")
