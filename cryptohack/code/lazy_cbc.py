import requests

def xor_two_strings(s1, s2):
    return bytes(a ^ b for a, b in zip(s1, s2))

# based on cbc decryption, we use two cipher blocks of 16 "a", which means the ciphertext is "a"*32
url1='https://aes.cryptohack.org/lazy_cbc/receive/'
ciphertext=("a"*32).encode().hex()
r=requests.get(url1+ciphertext+'/')
plaintext=r.json()['error'][19:]
# now we know: 
# (16*"a") xor (2nd block of plaintext) = (2nd block of ciphertext) after decryption = (16*"a") after decryption
# (1st block of plaintext) xor (key) = (16*"a") after decryption
# -> key = (1st block of plaintext) xor (16*"a") xor (2nd block of plaintext)
b=('a'*16).encode().hex()
x=xor_two_strings(bytes.fromhex(plaintext[32:]), bytes.fromhex(b))
key=xor_two_strings(bytes.fromhex(plaintext[:32]), x).hex()

url2 = 'https://aes.cryptohack.org/lazy_cbc/get_flag/'
flag=requests.get(url2+key+'/').json()['plaintext']
print(bytes.fromhex(flag).decode())