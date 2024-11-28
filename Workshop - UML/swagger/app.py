from flask import Flask,request
from flask_cors import CORS
import json

#------------------------------------------------------

app = Flask(__name__)

#------------------------------------------------------

CORS(app)

#------------------------------------------------------

@app.route("/add", methods=['POST'])
def add():
    
    data = json.loads(request.data)
   
    return str(data["a"] + data["b"])

#------------------------------------------------------

@app.route("/sub", methods=['POST'])
def sub():
    
    data = json.loads(request.data)
   
    return str(data["a"] - data["b"])

#------------------------------------------------------

@app.route("/mul", methods=['POST'])
def mul():
    
    data = json.loads(request.data)
   
    return str(data["a"] * data["b"])

#------------------------------------------------------

@app.route("/div", methods=['POST'])
def div():
    
    data = json.loads(request.data)
   
    return str(data["a"] / data["b"])

#------------------------------------------------------

@app.route("/docs", methods=['GET'])
def read_file():

    with open("Workshops/Workshop - UML/swagger/swagger.yaml", "r") as f:

        response = f.read()
   
    return response

#------------------------------------------------------

if __name__ == '__main__':

    app.run()

#------------------------------------------------------