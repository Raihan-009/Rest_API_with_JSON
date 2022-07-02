from crypt import methods
from flask import Flask, jsonify

app = Flask(__name__)

files = {
    "Videos": [
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
    ]
  }

@app.route('/')
def index():
    return "API with python flask"

@app.route('/videofiles', methods = ['GET'])
def get():
    return jsonify({'VideoInfo' : files })

@app.route('/videofiles', methods=['POST'])
def create():
    info = {
        "category": "flask",
        "video": [
          {
            "URL": "1230",
            "ID": "answer 1",
            "KEYWORD": "Instalaltion"
          },
          {
            "URL": "12340",
            "ID": "answer 1",
            "KEYWORD": "Documentaion"
          },
          {
            "URL": "12340",
            "ID": "answer 1",
            "KEYWORD": "Dependecies"
          }
        ]
      }
    files["Videos"].append(info)
    return jsonify({'VideoInfo' : files})

if __name__ == "__main__":
    app.run(debug=True)