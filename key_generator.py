from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()  #generate a key for our use
    with open("secret.key", "wb") as key_file:  #stores the key in the binary form for our use 
        key_file.write(key)

generate_key()
#encrypting passwords before saving them
#and decrypting while retriving
#for the generation of the key we are using cryptography library as we will be using the same key for both encryptoin and decryption
