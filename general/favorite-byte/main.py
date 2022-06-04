import binascii

msg = binascii.unhexlify('73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d')

def xor_me(text, value):
    return ''.join(chr(character ^ value) for character in text)

for i in range(255):
    result = xor_me(msg, i)
    if "crypto{" in result:
        print(result)

