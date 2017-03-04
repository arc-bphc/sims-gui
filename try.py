import json

with open('config.json') as data_file:
    data = json.load(data_file)
print data['Settings']['fingerprint']['sensorPath']
