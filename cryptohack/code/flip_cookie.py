import requests
cookie="a270bd6bec1905258982b65cc5c2971a63b71fb380390e1e3b76dd736fe04cfdb3fb04b82f09048e9224a060d19945f0"
iv=cookie[:32]
co=cookie[32:64]
url='https://aes.cryptohack.org/flipping_cookie/check_admin/'
s1=b'admin=True;\x05\x05\x05\x05\x05'
s2=b'admin=False;expi'
def xor_two_strings(s1, s2):
    return bytes(a ^ b for a, b in zip(s1, s2))
sendiv=xor_two_strings(xor_two_strings(s1, s2), bytes.fromhex(iv))
print(len(sendiv.hex()))
r=requests.get(url+co+'/'+sendiv.hex()+'/').json()
print(r)