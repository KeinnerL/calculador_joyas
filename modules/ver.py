import json

def ver_json():
    with open("joyas.json", "r", encoding="utf-8") as joyas:
        data = json.load(joyas)
    
    print(data)