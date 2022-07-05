import json


with open('videos.json')as f:
    data = json.load(f)

for video in data["Info"]:
    print(video)
    if video['category'] == "Gaming":
        print(video)