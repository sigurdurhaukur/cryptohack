import binascii

key1 = 'a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313'
key1x2 = '37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e'
key1x2x3 = 'c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1'
key1x2x3xflag = '04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf'

def get_bytes(hexst):
    binascii.unhexlify(hexst)

flag = get_bytes(key1)
# flag = get_bytes(key1) ^ get_bytes(key1x2) ^ get_bytes(key1x2x3) ^ get_bytes(key1x2x3xflag)

print(flag)
