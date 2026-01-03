# zlib compression will reduce length of repeated patterns
# so we can use it to guess the next char in the flag

# example: crypto|crypto -> crypto|
#          cryptc|crypto -> cryptc|o 
# so correct pattern will give min length after compression
import requests
import zlib
import string
st='crypto'

chars=string.printable
url='https://aes.cryptohack.org/ctrime/encrypt/'
def get_length(s):
    r=requests.get(url+s.encode().hex()+'/')
    return len(bytes.fromhex(r.json()['ciphertext']))

for i in range(5):
    a=0
    temp=''
    for c in chars:
        print('Trying:',st+c)
        test_str=st+c
        l=get_length(test_str)
        if a==0:
            a=l
            temp=c
        else:
            if l<a:
                st+=c
                break
            elif l>a:
                st+=temp
                break
    print(st)
