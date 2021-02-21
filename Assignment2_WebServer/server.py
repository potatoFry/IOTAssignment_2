import sys
import json
import numpy
import datetime
import decimal
import datetime
import gevent
import gevent.monkey
from gevent.pywsgi import WSGIServer
gevent.monkey.patch_all()

from flask import Flask, request, Response, render_template, jsonify, redirect

import dynamodb
import jsonconverter as jsonc
import sub_temp
import pub_moveWindow
import pub_sign
import sub_signValue

# Google Chart/Graph Functions
class GenericEncoder(json.JSONEncoder):
   def default(self, obj):
      if isinstance(obj, numpy.generic):
         return numpy.asscalar(obj)
      elif isinstance(obj, datetime.datetime):
         return obj.strftime('%Y-%m-%d %H:%M:%S')
      elif isinstance(obj, decimal.Decimal):
         return float(obj)
      else:
         return json.JSONEncoder.default(self, obj)

def data_to_json(data):
   json_data = json.dumps(data,cls=GenericEncoder)
   return json_data

app = Flask(__name__)

@app.route("/api/getdata",methods=['POST','GET'])
def apidata_getdata():
    if request.method == 'POST' or request.method == 'GET':
        try:
            data = {'chart_data': jsonc.data_to_json(dynamodb.get_data_from_dynamodb()),
             'title': "Visitor Data"}
            #print("TEMP DATA")
            #print("***")
            #print(jsonify(data))
            #print("***")
            return jsonify(data)

        except:
            import sys
            print(sys.exc_info()[0])
            print(sys.exc_info()[1])


@app.route("/api/getDHT", methods=['POST','GET'])
def getTemp():
    if request.method == 'POST' or request.method == 'GET':
        try:
            data = sub_temp.subTemp()
            #print("TEMP AND HUMID")
            #print("***")
            #print(data)
            #return data_to_json(data)
            return jsonify(data)

        except Exception as e:
            print(e)

def openWindow():
    print("opening window")
    pub_moveWindow.windowOpen()
    return "Opened"

def closeWindow():
    print("close window")
    pub_moveWindow.windowClose()
    return "Closed"

@app.route("/updatesign",methods=['GET', 'POST'])
def updateSign():
    print("Updating sign")
    row1 = request.form['row1']
    row2 = request.form['row2']
    pub_sign.publishSign(row1+":"+row2)
    return redirect("/sign")


#unlocks door
@app.route("/motor/<status>")
def writePin(status):
    if status == 'openWindow':
        response = openWindow()
    else:
        response = closeWindow()
    return response

@app.route("/readSign",methods=['GET', 'POST'])
def readSign():
    data = sub_signValue.subSign()
    print(type(data))
    data = data.decode("utf-8")
    dataList = data.split(":")
    data = {'row1':dataList[0], 'row2': dataList[1]}
    print(data)
    return jsonify(data)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/security")
def security():
    return render_template('security.html')

@app.route("/sign")
def sign():
    return render_template('sign.html')

@app.route("/index")
def verify():
    return render_template('index.html')

if __name__ == '__main__':
   try:
        http_server = WSGIServer(('0.0.0.0', 8001), app)
        app.debug = True
        print('Waiting for requests.. ')
        http_server.serve_forever()
   except Exception as e:
        print("Exception")
        print(e)
        print(sys.exc_info()[0])
        print(sys.exc_info()[0])
