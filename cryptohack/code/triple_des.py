import requests

def encrypt_flag(key):
    url = 'https://aes.cryptohack.org/triple_des/encrypt_flag/'
    r = requests.get(url + key + '/').json()
    return r['ciphertext']

def encrypt(key, text):
    url = 'https://aes.cryptohack.org/triple_des/encrypt/'
    r = requests.get(url + key + '/' + text + '/').json()
    return bytes.fromhex(r['ciphertext'])

key=b'\x00'*8+b'\xff'*8 # this is 2key for 3DES, so k1=0000000000000000, k2=ffffffffffffffff
# F(F(M))=E(k1, D(k2, E(k1, F(M)))) = M, cancels out bcuz E(K1, E(K1, X))=X, D(K2, D(K2, X))=X
# bcuz k1,k2 are weak keys in single DES
print(encrypt(key.hex(), encrypt_flag(key.hex()))) # encrypt 2 times
