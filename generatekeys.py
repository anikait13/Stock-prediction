import pickle
from pathlib import Path

import streamlit_authenticator as stauth

import yaml

from yaml.loader import SafeLoader

with open('credential.yaml', 'r') as f:
    data = list(yaml.load_all(f,SafeLoader))
    print(data[0])

with open('credential.yaml') as file:
    config = yaml.load(file,SafeLoader)