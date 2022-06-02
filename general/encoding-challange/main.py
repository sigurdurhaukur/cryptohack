from pwn import * # pip install pwntools
import json
import base64

r = remote('socket.cryptohack.org', 13377, level = 'debug')

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)


received = json_recv()

print(received["type"])

decoded = ""
if received["type"] == "base64":
    decoded = base64.b64decode(received["encoding"])
elif received["type"] == "utf-8":
    for i in received["encoding"]:
        decoded += ord(i)
elif received["type"] == "hex":
    decoded = bytearray.fromhex(received["encoding"]).decode()


to_send = {
    "decoded": "changeme"
}
json_send(to_send)


json_recv()
