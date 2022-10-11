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
    print(f"[blink red]No {file_config} file found. Exiting.")
    sys.exit(1)
with open(file_config, 'r') as f:
    config = json.load(f)
# Loaf stuff.
file_creds = "creds.ini"
if not path.isfile(file_creds):
    print(f"[blink red]No {file_creds} file found. Exiting.")
    sys.exit(1)
loaf = Loaf(file=file_creds)
# Flask stuff.
app = Flask(__name__)
CORS(app)

# Importing here avoids circular imports.
from src.routes import home
