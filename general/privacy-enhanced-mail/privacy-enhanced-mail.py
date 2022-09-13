#!/usr/bin/env python3

from Crypto.PublicKey import RSA

f = open('./privacy_enhanced_mail.pem','r')
contents = f.read()
print(contents)
key = RSA.importKey(contents)

print(key)
