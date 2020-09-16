import time
from flask import Flask, request
from monitor import monitorStatus

app = Flask(__name__)

@app.route('/monitor',methods = ['POST'])
def monitor():
    return str(monitorStatus())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5007, debug=True, threaded=True)
