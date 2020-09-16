import shutil
from flask import Flask, request
from saveFile import saveFILE
from compileCode import getCompile

app = Flask(__name__)

@app.route('/compile', methods=["POST"])
def compile():
    timeout = 10
    jsonRes = request.get_json()
    code = jsonRes['getCode']
    lan = jsonRes['type']
    userID = jsonRes['userid']
    filename = jsonRes['filename']
    inp = jsonRes['input']

    code = str(code.decode('utf-8'))
    lan = str(lan.decode('utf-8'))
    userID = str(userID.decode('utf-8'))
    filename = str(filename.decode('utf-8'))
    inp = str(inp.decode('utf-8'))

    getpath = saveFILE(code, lan, userID, filename, inp)
    compilation_status = getCompile(getpath,lan, timeout)
    #shutil.rmtree('../compile/'+str(userID))
    return str(compilation_status)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004, debug=True, threaded=True)
