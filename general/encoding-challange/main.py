from pwn import * # pip install pwntools
from Crypto.Util.number import long_to_bytes
import json
import base64
import codecs

r = remote('socket.cryptohack.org', 13377, level = 'debug')

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)

def find_decoded(received):
    decoded = ""
    if "flag" in received:
        decoded = received["flag"]
    elif received["type"] == "base64":
        decoded = base64.b64decode(received["encoded"]).decode('utf-8')
    elif received["type"] == "utf-8":
        for i in received["encoded"]:
            decoded += chr(i)
    elif received["type"] == "hex":
        decoded = bytearray.fromhex(received["encoded"]).decode()
    elif received["type"] == "rot13":
        rot13 = lambda s : codecs.getencoder("rot-13")(s)[0]
        decoded = rot13(received["encoded"])
    elif received["type"] == "bigint":
        decoded = long_to_bytes(int(received["encoded"], 0)).decode('utf-8')

    return decoded


while True:
    stuff = json_recv()
    decoded = find_decoded(stuff)

    if decoded.find("crypto{") != -1:
        print(stuff["flag"])
        break

    send = {"decoded": decoded}
    json_send(send)

    if type(stuff) != dict:
        break

