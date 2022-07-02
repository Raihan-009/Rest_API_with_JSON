import json

video_info = '''{"Videos" : [
    {
        "category": "react",
        "video": [
            {
                "URL": "1234",
                "ID": "answer 1",
                "KEYWORD": "Instalaltion"
            },
            {
                "URL": "12345",
                "ID": "answer 1",
                "KEYWORD": "Documentaion"
            },
            {
                "URL": "12346",
                "ID": "answer 1",
                "KEYWORD": "Dependecies"
            }
        ]
    },
    {
        "category": "docker",
        "video": [
            {
                "URL": "12347",
                "ID": "answer 1",
                "KEYWORD": "Instalaltion"
            },
            {
                "URL": "12348",
                "ID": "answer 1",
                "KEYWORD": "Documentaion"
            },
            {
                "URL": "12349",
                "ID": "answer 1",
                "KEYWORD": "Dependecies"
            }
        ]
    }
]}
'''

print("*******************")
data = json.loads(video_info)
print(type(data))
print(data)
print("*******************")
for video in data['Videos']:
    print(video)
print("*******************")
for video in data['Videos']:
    print(video['category'])
print("*******************")
for video in data['Videos']:
    print(video['video'])

print("*******************")

new_json = json.dumps(data, indent=2)
print(new_json)