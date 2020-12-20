from flask import Flask,request,render_template,jsonify
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/process',methods= ['POST'])
def process():
  input1  = float(request.form['input1'])
  input2 = float(request.form['input2'])
  output = str(input1 + input2)
  return jsonify({"output":"Result: " + output})