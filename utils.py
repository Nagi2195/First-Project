import json


def json_reader(filepath):
    try:
        with open(filepath) as f:
            data = json.load(f)
            return data
    except Exception as e:
        print(e)
