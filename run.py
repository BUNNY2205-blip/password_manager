
import streamlit as st
from manager import add_password, get_password

st.title(" Password Manager")

option = st.selectbox("Choose an action", ["Add Password", "Get Password"])

if option == "Add Password":
    site = st.text_input("Site name")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Save"):
        add_password(site, username, password)
        st.success(" Password saved")

elif option == "Get Password":
    site = st.text_input("Site to retrieve")
    if st.button("Get"):
        get_password(site)

