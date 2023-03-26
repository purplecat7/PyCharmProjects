import json

keyfile = '../config/keyfile.json'
with open(keyfile) as f:
    config = json.load(f)

print(config)