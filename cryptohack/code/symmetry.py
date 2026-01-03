import requests
ciphertext='41de01d32a6089c1b50b421553602e0aa27291748d709262dbfd4af78e511e57fae6b94fe637f05c5edfb346f4576c8abd'
iv=ciphertext[:32]
plaintext=''
url='https://aes.cryptohack.org/symmetry/encrypt/'
def xor_two_strings(s1, s2):
    return bytes(a ^ b for a, b in zip(s1, s2))
blocks=[ciphertext[i:i+32] for i in range(32, len(ciphertext), 32)]
for i in blocks:
    r=requests.get(url+i+'/'+iv+'/').json()
    plaintext+=r['ciphertext']
    iv=xor_two_strings(bytes.fromhex(i), bytes.fromhex(r['ciphertext'])).hex()

print(bytes.fromhex(plaintext))