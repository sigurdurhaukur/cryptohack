
# the givens
msg = 12
e = 65537
p = 17
q = 23

def encrypt(msg=msg, exp=e, mod= (p * q)):
    return pow(msg, exp, mod)


# encrypt the number
encrypted = encrypt()
print(encrypted)