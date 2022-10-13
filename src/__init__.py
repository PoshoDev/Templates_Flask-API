from os import path
import sys
import json
from flask import Flask
from flask_cors import CORS
from rich import print
from loaf import Loaf

# Load config file.
file_config = "config.json"
if not path.isfile(file_config):
    print(f"[red]No {file_config} file found.")
    config = None
else:
    with open(file_config, 'r') as f:
        config = json.load(f)
# Loaf stuff.
file_creds = "creds.ini"
if not path.isfile(file_creds):
    print(f"[red]No {file_creds} file found.")
    loaf = None
else:
    loaf = Loaf(file=file_creds)
# Flask stuff.
app = Flask(__name__)
app.config['SECRET_KEY'] = 'MySecretKey'
CORS(app)

# Importing here avoids circular imports.
from src.routes import home, login
