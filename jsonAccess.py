import json


with open('videoInfo.JSON')as f:
    data = json.load(f)
    print(data)