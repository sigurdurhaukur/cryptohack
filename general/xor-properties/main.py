
key1 = 'a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313'

def hex_to_int(*argv):
    results = []
    for arg in argv:
        results.append(int(bytes.fromhex(arg)))

hex_to_int(key1)
