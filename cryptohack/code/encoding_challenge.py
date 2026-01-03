from pwn import * # pip install pwntools
import json
from Crypto.Util.number import long_to_bytes
import codecs
import base64

HOST = "socket.cryptohack.org"
PORT = 13377

r = remote(HOST, PORT)


def json_recv():
    line = r.readline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)

for i in range(100):
    challenge = json_recv()
    print(f"Challenge {i}: {challenge}")

    if challenge["type"] == "base64":
        decoded = base64.b64decode(challenge["encoded"]).decode()
    elif challenge["type"] == "hex":
        decoded = bytes.fromhex(challenge["encoded"]).decode()
    elif challenge["type"] == "rot13":
        decoded = codecs.decode(challenge["encoded"], 'rot_13')
    elif challenge["type"] == "bigint":
        decoded = long_to_bytes(int(challenge["encoded"], 16)).decode()
    elif challenge["type"] == "utf-8":
        decoded = ''.join(chr(b) for b in challenge["encoded"])

    response = {"decoded": decoded}
    json_send(response)

flag = json_recv()
print(flag)
