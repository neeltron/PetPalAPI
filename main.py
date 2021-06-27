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
  url = request.args.get('url')
  db['temp'] = temp
  db['url'] = url
  return temp



@app.route('/output_app')
def output_app():
  temp = db['temp']
  url = db['url']
  dict = {"temperature": temp, "url": url}
  output = json.dumps(dict)
  return output



@app.route('/input_app')
def input_app():
  food = request.args.get('food')
  pic = request.args.get('pic')
  db['food'] = food
  db['pic'] = pic
  return "done"



@app.route('/output_hardware')
def output_hardware():
  food = db['food']
  pic = db['pic']
  return food + " " + pic



app.run(host='0.0.0.0', port=8080)
