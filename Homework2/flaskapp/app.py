from flask import Flask,request,render_template,jsonify
import pymongo
import redis
import json
from pymongo import MongoClient

r = redis.Redis(host='cache', port=6379, db=0)

app = Flask("Calc")

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/process', methods= ['POST'])
def process():
  r.incr('hits', amount=1)
  input1  = float(request.form['input1'])
  input2 = float(request.form['input2'])
  output = str(input1 + input2)
  return jsonify({"output":"Result: " + output})

@app.route('/hits', methods=['GET'])
def hits():
    hits = int(r.get('hits').decode('utf-8'))
    return json.dumps({'hits': hits})

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8000)