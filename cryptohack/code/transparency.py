from Crypto.PublicKey import RSA
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
key=RSA.importKey(open('transparency_afff0345c6f99bf80eab5895458d8eab.pem').read())
print(key.n)
print(key.e)
public_numbers = rsa.RSAPublicNumbers(e=key.e, n=key.n)

public_key = public_numbers.public_key()
public_key_bytes = public_key.public_bytes(
    encoding=serialization.Encoding.DER,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# Compute the SHA256 hash of the serialized public key bytes
digest = hashes.Hash(hashes.SHA256())
digest.update(public_key_bytes)
print(digest.finalize().hex())

# Finally, use advanced search of crt.sh website with sha256 public key and get the subdomain