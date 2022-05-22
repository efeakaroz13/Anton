#Copyright (c) 2022, Efe Akaröz
#All rights reserved.

from flask import Flask,render_template,request,redirect
import requests

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/demo")
def demo():
	return render_template("demo.html")

app.run(debug=True)
