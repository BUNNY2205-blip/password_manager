import json
import os #for checking if file exists
from crypto import encrypt_passw, decrypt_passw #custom encryption function
import pyperclip  #for copying passwords directly to the clipboards

DATA_FILE = "vault.json"

# Load existing password data from file
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)  #gives the data present in the dictionary and if not it will return an empty dictionary
    return {}

# Save password data to file
def save_data(data):
    with open(DATA_FILE, "w") as f: #saves the data into the json file 
        json.dump(data, f, indent=4)

# Add a new password (encrypt before saving)
def add_password(site, username, password):
    data = load_data()
    data[site] = {
        "username": username,
        "password": encrypt_passw(password)
    }
    save_data(data)
    print(f" Password saved for {site}")

# Get password for a site (decrypt before displaying)
def get_password(site):
    data = load_data()
    if site in data:
        decrypted = decrypt_passw(data[site]["password"])
        print(f"\n Site: {site}")
        print(f" Username: {data[site]['username']}")
        print(f" Password: {decrypted}")
        pyperclip.copy(decrypted)
        print(" Password copied to clipboard!")
    else:
        print(" No password found for that site.")
