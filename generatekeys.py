import pickle
from pathlib import Path

import streamlit_authenticator as stauth

names = {"Anikait Thakur", "Mohammed Minaam Bhat", "System Admin"}
usernames = {"anikait13", "minaam786", "admin"}
passwords = {"9868", "1234", "admin"}

# uses bcrypt to hash passwords
hashed_passwords = stauth.Hasher(passwords).generate()

# finding path to pickle file
file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("wb") as file:
    pickle.dump(hashed_passwords, file)

