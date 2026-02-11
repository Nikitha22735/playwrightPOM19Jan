import json


def jsonData(path):
    with open(path) as data:
        jsonData = json.load(data)
        return jsonData