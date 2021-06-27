from flask import Flask, request
from replit import db



app = Flask('app')

@app.route('/')
def hello_world():
  return 'Hello, World!'



@app.route('/input_hardware')
def input_hardware():
  temp = request.args.get('temp')
  db['temp'] = temp
  return temp



app.run(host='0.0.0.0', port=8080)
