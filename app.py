#Copyright (c) 2022, Efe Akaröz
#All rights reserved.

from flask import Flask,render_template,request,redirect
import requests
from textblob import TextBlob
from deep_translator import single_detection
import translators as ts

#f2e29ae59187dddd8e935acfc34e6ba0

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/demo")
def demo():
	return render_template("demo.html")

@app.route("/textLangDetect")
def textLangDetect():
	q = request.args.get("q")


	lang = single_detection(q, api_key='f2e29ae59187dddd8e935acfc34e6ba0')

	return {"lang": lang}

@app.route("/translate")
def translation():
	from_ = request.args.get("from")
	to_ = request.args.get("to")
	q = request.args.get("q")
	out ={ "out":ts.google(q, from_language=from_, to_language=to_)}
	return out



app.run(debug=True)
