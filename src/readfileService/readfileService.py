import time
from flask import Flask, request
from readFile import readFILE

app = Flask(__name__)

@app.route('/readfile', methods=["POST"])
def readfile():
    jsonRes = request.get_json()
    userID = jsonRes['userid']
    lan = jsonRes['type']
    filename = jsonRes['filename']

    userID = str(userID.decode('utf-8'))
    lan = str(lan.decode('utf-8'))
    filename = str(filename.decode('utf-8'))

    code = readFILE(lan, userID, filename)
    return str(code)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5006, debug=True, threaded=True)
