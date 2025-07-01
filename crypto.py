from cryptography.fernet import Fernet
#loading the secret key into the file
def load_key():
    return open('secret.key','rb').read()
#now we will be encrypting the password string using fernet
def encrypt_passw(password):
    key = load_key()
    fernet = Fernet(key)
    encryption = fernet.encrypt(password.encode())
    return encryption.decode()
#converting the bytes to string for storage
def decrypt_passw(encrypted_password):
    key = load_key()
    fernet = Fernet(key)
    decryption = fernet.decrypt(encrypted_password.encode())
    return decryption.decode()
#converts bytes back to string