from flask import Flask, request
from replit import db
import json



app = Flask('app')

@app.route('/')
def hello_world():
  return 'Hello, World!'



@app.route('/input_hardware')
def input_hardware():
  temp = request.args.get('temp')
  db['temp'] = temp
  return temp



@app.route('/output_app')
def output_app():
  temp = db['temp']
  dict = {"temperature": temp}
  output = json.dumps(dict)
  return output



@app.route('/input_app')
def input_app():
  food = request.args.get('food')
  pic = request.args.get('pic')
  water = request.args.get('water')
  db['food'] = food
  db['pic'] = pic
  db['water'] = water
  return "done"



app.run(host='0.0.0.0', port=8080)
