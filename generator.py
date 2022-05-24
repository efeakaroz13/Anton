import pyttsx3
import requests
import os
from flask import Flask,request,render_template

app = Flask(__name__)

@app.route("/",methods=["POST","GET"])
def index():
	engine = pyttsx3.init()
	voices = engine.getProperty('voices')
	if request.method == "POST":
		#TR
		text = request.form.get("mytextarea")
		engine.setProperty('voice', 42)
		engine. setProperty("rate", 178)
		engine.save_to_file(text, 'speechTR.mp3')
		engine.runAndWait()

	

	return render_template("generate.html",voices=voices)

app.run(debug=True,port=3000)