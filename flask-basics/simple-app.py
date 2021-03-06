from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def index(name="Treehouse"):
	name = request.args.get('name', name)
	#return "Hello from {}".format(name)
	context = {
		'name':name
	}
	return render_template("index.html", **context)

@app.route('/concat/<num1>/<num2>')
def concat(num1, num2):
	return '{} + {} = {}'.format(num1, num2, num1+num2)

@app.route('/add/<int:num1>/<int:num2>')
@app.route('/add/<float:num1>/<float:num2>')
@app.route('/add/<int:num1>/<float:num2>')
@app.route('/add/<float:num1>/<int:num2>')
def add(num1, num2):
	#return '{} + {} = {}'.format(num1, num2, num1+num2)
	context = {
		'num1':num1,
		'num2':num2
	}
	return render_template("add.html", **context)

app.run(debug=True,port=8000,host='localhost')