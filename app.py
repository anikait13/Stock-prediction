import streamlit as st
import pickle
from pathlib import Path
import streamlit_authenticator as stauth

st.title("Welcome to stock predictor LOGIN page app")

# --- USER AUTHENTICATION ---
names = {"Anikait Thakur", "Mohammed Minaam Bhat", "System Admin"}
usernames = {"anikait13", "minaam786", "admin"}

#load hashed passwords
file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)

authenticator = stauth

