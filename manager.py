import json
import os
import streamlit as st  
from crypto import encrypt_passw, decrypt_passw

DATA_FILE = "vault.json"

# Load existing password data from file
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}

# Save password data to file
def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

# Add a new password (encrypt before saving)
def add_password(site, username, password):
    data = load_data()
    data[site] = {
        "username": username,
        "password": encrypt_passw(password)
    }
    save_data(data)
    st.success(f"Password saved for {site}")

# Get password for a site (decrypt before displaying)
def get_password(site):
    data = load_data()
    if site in data:
        decrypted = decrypt_passw(data[site]["password"])
        st.subheader(f" Credentials for {site}")
        st.write(f"**Username:** {data[site]['username']}")
        st.code(decrypted, language="text")
        st.info("Password shown above. You can copy it manually.")
    else:
        st.error("No password found for that site.")
