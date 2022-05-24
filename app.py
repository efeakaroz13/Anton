#Copyright (c) 2022, Efe Akaröz
#All rights reserved.

from flask import Flask,render_template,request,redirect
import requests
from textblob import TextBlob
from deep_translator import single_detection
import translators as ts
import random

#f2e29ae59187dddd8e935acfc34e6ba0

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/demo")
def demo():
	return render_template("demo.html")


@app.route("/tts")
def tts():
	engine = pyttsx3.init()
	voices = engine.getProperty('voices')

	#TR
	text = request.args.get("q")
	engine.setProperty('voice', 7)
	engine. setProperty("rate", 178)
	filename = 'speechEN{}.mp3'.format(random.randint(1,345346456)
	engine.save_to_file(text, filename))
	engine.runAndWait()
	return {
	"out":filename,
	"transcript":""
	}
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

@app.route("/pyscript")
def pyscript():
	return """
		<html>
		<head>
			<link rel="stylesheet" href="https://pyscript.net/alpha/pyscript.css" />
			<script defer src="https://pyscript.net/alpha/pyscript.js"></script>

		</head>
		<py-env>
		  - numpy
		  - requests
		  - pyttsx3
		</py-env>
		<body>

			<py-script>

				import pyttsx3
				engine = pyttsx3.init()
				engine.say('Sally sells seashells by the seashore.')
				engine.runAndWait()

				print("Hello World")
			</py-script>
		</body>
		</html>

	"""


app.run(debug=True)
