from flask import Flask, jsonify
import datetime
import json

app = Flask(__name__)

with open('projects.json', 'r') as file:
        result = json.load(file)
        print(result)

@app.route('/projects', methods=['GET'])
def get_projects():
    with open('projects.json', 'r') as file:
        result = json.load(file)
        return jsonify({'projects': result})

#@app.route('/recent_projects', methods=['GET'])
#def get_recent_projects():
#    result = datetime.datetime.now()
#    return jsonify({'recent_projects': str(result).strip()})


if __name__ == '__main__':
    app.run(port=5000)