import binascii

msg = binascii.unhexlify('0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104')

def find_gcf(a, b):
    if a % b != 0:
        return gcd2(b, a % b)
    else:
        return b



