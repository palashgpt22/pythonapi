import os
import json
from flask import Flask
from flask import request, jsonify

app = Flask(__name__)

myDict = {}

@app.route('/bool/<keyname>')
def getvalue(keyname):
    result = {}
    global myDict
    if (keyname != None and keyname != ""):
	if keyname in myDict:
		result['status'] = "success"
		result['value'] = myDict[keyname]
	else: 
		result['status'] = "failure"
    else:
	result['status'] = "failure"

    return jsonify(result)


@app.route('/bool', methods = ['POST'])
def setvalue():
    global myDict
    result = {}
    jsonObj = request.get_json()
    if ('keyname' in jsonObj and 'valuename' in jsonObj):
    	keyname = jsonObj['keyname']
    	valuename = jsonObj['valuename']
    	if (keyname != None and valuename != None):
		myDict[keyname] = valuename
		result['status'] = "success"
	else:
		result['status'] = "failure"
    else:
	result['status'] = "failure"

    return jsonify(result)
    
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
