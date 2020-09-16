import requests
from flask import Flask, render_template, json, request
import sys
import ast
import mysql.connector
from getMonitor import getMonitorIP
from mysql.connector import Error


reload(sys)
sys.setdefaultencoding('utf-8')

app = Flask(__name__)

def retrieveMonitors():
    languages = []
    try:
        conn = mysql.connector.connect(host='localhost',
                                       port='3306',
                                       database='cloudcompiler',
                                       user='root',
                                       password='lab@cc2')
        if conn.is_connected():
            cursor = conn.cursor();
            cursor.execute("SELECT * FROM pcip")
            monitorip = cursor.fetchall()
        # print (monitorip)
    except Error as e:
        print(e)

    finally:
        conn.close()
    return monitorip

def getMonitorStatus(monitorIP):
    monitorfile_url = 'http://' + str(monitorIP)+":5007"
    r = requests.post(monitorfile_url+'/monitor')
    result = ast.literal_eval(str(r.text))
    return result

@app.route('/master', methods=["POST","GET"])
def master():
    jsonRes = request.get_json()
    _action = jsonRes['action']

    if _action=="compile":
        pcramdetails = []
        pcip = retrieveMonitors()
        for i, ip in enumerate(pcip):
            monitor_details = getMonitorStatus(ip[1])
            ava_ram = monitor_details['ava_ram']
            pcramdetails.append([ip[1], ava_ram])

        compileIP = getMonitorIP(pcramdetails)

        code = jsonRes['code']
        language = jsonRes['language']
        inp = jsonRes['input']
        username = jsonRes['username']
        filename = 'example'

        language = str(language.decode('utf-8'))
        code = str(code.decode('utf-8'))
        inp = str(inp.decode('utf-8'))

        compiler_url = "http://" + compileIP + ":5004"

        r = requests.post(compiler_url+'/compile', data=json.dumps({'getCode':code, \
                                                                    'type':language, \
                                                                    'input':inp, \
                                                                    'userid':username, \
                                                                    'filename':filename}), \
                                                                    headers={'Content-Type' : 'application/json'})
        return r.text

    elif _action=="savefile":
        pcstrgdetails = []
        pcip = retrieveMonitors()
        for i, ip in enumerate(pcip):
            monitor_details = getMonitorStatus(ip[1])
            ava_storage = monitor_details['ava_storage']
            pcstrgdetails.append([ip[1], ava_storage])
        storageIP = getMonitorIP(pcstrgdetails)

        code = jsonRes['code']
        language = jsonRes['language']
        inp = jsonRes['input']
        username = jsonRes['username']
        filename = jsonRes['filename']

        language = str(language.decode('utf-8'))
        code = str(code.decode('utf-8'))
        inp = str(inp.decode('utf-8'))

        savefile_url = "http://" + storageIP + ":5005"

        r = requests.post(savefile_url+'/savefile', data=json.dumps({'getCode':code, \
                                                                    'type':language, \
                                                                    'input':inp, \
                                                                    'userid':username, \
                                                                    'filename':filename}), \
                                                                    headers={'Content-Type' : 'application/json'})
        return '{0}&{1}'.format(str(r.text), storageIP)
    elif _action=="read":

        language = jsonRes['language']
        username = jsonRes['username']
        filename = jsonRes['filename']
        ip = jsonRes['ip']

        readfile_url = "http://" + str(ip) + ":5006"
        r = requests.post(readfile_url+'/readfile', data=json.dumps({'type':language, \
                                                                    'userid':username, \
                                                                    'filename':filename}), \
                                                                    headers={'Content-Type' : 'application/json'})
        return str(r.text)
    else:
        return "Sorry, wrong request"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True, threaded=True)