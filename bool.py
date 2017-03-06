import os
from flask import Flask
from flask import request
app = Flask(__name__)

param = None

@app.route("/")
def hello():
    return "the current value of your boolean is " + str(param)


@app.route("/setvalue")
def setvalue():
    global param
    userval = request.args.get('value')
    if (userval == 'true' or userval == 'True' or userval == '1'):
        param = True
    elif (userval == 'false' or userval == 'False' or userval == '0'):
        param = False
    else:
        return "please provide a valid value: True for true or True or 1 and False for false False or 0"


    return "the new value of your boolean is " + str(param)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

