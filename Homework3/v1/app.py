from flask import Flask,request,render_template,jsonify
import redis
import json
from pymongo import MongoClient
from bson.json_util import dumps

r = redis.Redis(host='cache', port=6379, db=0)

app = Flask("Calc")

client = MongoClient("mongodb:27017")
db = client.test
collection = db.results

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/process', methods= ['POST'])
def process():
  r.incr('hits', amount=1)
  input1  = float(request.form['input1'])
  input2 = float(request.form['input2'])
  output = str(input1 + input2)
  collection.insert({"Result": output})
  return jsonify({"output":"Result: " + output})

#displays number of calculations done
@app.route('/hits', methods=['GET'])
def hits():
  hits = int(r.get('hits').decode('utf-8'))
  return json.dumps({'hits': hits})

#displays previously computed results stored in mongodb
@app.route('/mongo', methods=['GET'])
def show_collection():
  return dumps(db.results.find())

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)