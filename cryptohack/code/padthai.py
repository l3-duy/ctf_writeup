from pwn import *
import json
from Crypto.Util.number import long_to_bytes

HOST = "socket.cryptohack.org"
PORT = 13421

r = remote(HOST, PORT)

def json_recv():
    line = r.readline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)

def check_unpad(iv, ct):
    data={'option':'unpad','ct':(iv+ct).hex()}
    json_send(data)
    response=json_recv()
    return response['result']

def one_block_attack(ct):
    block_size=16
    recovered_block=[0]*block_size

    for padding_length in range(1, block_size+1):
        modified_block=[padding_length ^ i for i in recovered_block] # doing this will give correct format when unpad 
        for guess in range(256): # guess have the form of (padding_length ^ original_byte)
            print(f"Trying guess {guess} for padding length {padding_length}")
            modified_block[-padding_length] = guess
            if check_unpad(bytes(modified_block), ct):
                if padding_length == 1:
                    # Check for false positive
                    modified_block[-padding_length - 1] ^= 1
                    if not check_unpad(bytes(modified_block), ct):
                        continue
                recovered_byte = guess ^ padding_length # reverse the earlier xor to get original byte
                recovered_block[-padding_length] = recovered_byte
                print(f"Recovered byte: {recovered_byte} -> {long_to_bytes(recovered_byte)}")
                break
    return recovered_block

def attack(iv, ct):
    full_msg=b''
    msg_blocks=[ct[i:i+16] for i in range(0, len(ct), 16)]
    for block in msg_blocks:
        print("Attacking block:", block.hex())
        recovered_block=one_block_attack(block)
        full_msg+=bytes([a ^ b for a, b in zip(recovered_block, iv)])
        iv=block # previous ciphertext block becomes iv for next block (cbc)
    return full_msg

r.recvuntil(b"\n")
data={'option':'encrypt'}
json_send(data)
response=bytes.fromhex(json_recv()['ct'])
iv, ct = response[:16], response[16:]
msg=attack(iv, ct)
data={'option':'check','message':msg.decode()}
json_send(data)
response=json_recv()
print("Flag:", response['flag'])