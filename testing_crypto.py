# test_crypto.py
from crypto import encrypt_passw, decrypt_passw

original = "MySecret123"
enc = encrypt_passw(original)
dec = decrypt_passw(enc)

print(f"Original: {original}")
print(f"Encrypted: {enc}")
print(f"Decrypted: {dec}")
