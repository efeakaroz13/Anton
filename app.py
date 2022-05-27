#Copyright (c) 2022, Efe Akaröz
#All rights reserved.

from flask import Flask,render_template,request,redirect,abort
import requests
from textblob import TextBlob
from deep_translator import single_detection
import translators as ts
import random
import pyttsx3
import os


requires = """
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
	<script src="https://cdnjs.cloudflare.com/ajax/libs/mdbootstrap/4.20.0/js/mdb.min.js" integrity="sha512-XFd1m0eHgU1F05yOmuzEklFHtiacLVbtdBufAyZwFR0zfcq7vc6iJuxerGPyVFOXlPGgM8Uhem9gwzMI8SJ5uw==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
	<script src="https://efeakaroz.pythonanywhere.com/static/enject.js"></script>
	<script>document.body.innerHTML = document.body.innerHTML+"<button onclick='openLanguageSelector()' type='button' class='btn btn-primary btn-floating'><i class='fas fa-headphones'></i></button>"</script>
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
"""

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
	lang  = request.args.get("lang")
	if lang == "tr":
		#TR
		engine = pyttsx3.init()
		voices = engine.getProperty('voices')
		lang  = request.args.get("lang")
		text = request.args.get("q")
		engine.setProperty('voice', voices[42].id)
		engine. setProperty("rate", 178)
		filename = './static/speechTR{}.mp3'.format(random.randint(1,345346456))
		engine.save_to_file(text, filename)
		engine.runAndWait()
		os.system(f"autosub {filename} -S tr -D tr")
		os.system(f"ffmpeg -loop 1 -i image.jpg -i {filename} -c:v libx264 -tune stillimage -c:a aac -b:a 192k -pix_fmt yuv420p -shortest {filename.replace('.mp3','.mp4')}")
		srtfile = open(filename.replace("mp3","srt"),"r")
		vttwrite = open(filename.replace("mp3","vtt"),"w")
		vttwrite.write("WEBVTT\n\n")
		for srt in srtfile.readlines():
			try:
				int(srt)
			except:
				

				try:
					int(srt[0])
					vttwrite.write(srt.replace(",","."))
				except:
					if srt.strip() == "":
						pass
					else:
						vttwrite.write("- "+srt+"\n")

		os.system("rm {}".format(filename.replace(".mp3","srt")))
		return {
			"out":filename.replace("mp3","mp4"),
			"transcript":filename.replace("mp3","vtt")
		}
	if lang == "fr":
		#FR
		engine = pyttsx3.init()
		voices = engine.getProperty('voices')
		lang  = request.args.get("lang")
		text = request.args.get("q")
		engine.setProperty('voice', voices[37].id)
		engine. setProperty("rate", 150)
		filename = './static/speechFR{}.mp3'.format(random.randint(1,345346456))
		engine.save_to_file(text, filename)
		engine.runAndWait()
		os.system(f"autosub {filename} -S fr -D fr")
		os.system(f"ffmpeg -loop 1 -i image.jpg -i {filename} -c:v libx264 -tune stillimage -c:a aac -b:a 192k -pix_fmt yuv420p -shortest {filename.replace('.mp3','.mp4')}")
		srtfile = open(filename.replace("mp3","srt"),"r")
		vttwrite = open(filename.replace("mp3","vtt"),"w")
		vttwrite.write("WEBVTT\n\n")
		for srt in srtfile.readlines():
			try:
				int(srt)
			except:
				

				try:
					int(srt[0])
					vttwrite.write(srt.replace(",","."))
				except:
					if srt.strip() == "":
						pass
					else:
						vttwrite.write("- "+srt+"\n")

		os.system("rm {}".format(filename.replace(".mp3","srt")))
		return {
			"out":filename.replace("mp3","mp4"),
			"transcript":filename.replace("mp3","vtt")
		}

	if lang == "de":

		#DE
		engine = pyttsx3.init()
		voices = engine.getProperty('voices')
		lang  = request.args.get("lang")
		text = request.args.get("q")
		engine.setProperty('voice',voices[4].id)
		engine. setProperty("rate", 150)
		filename = './static/speechDE{}.mp3'.format(random.randint(1,345346456))
		engine.save_to_file(text, filename)
		engine.runAndWait()
		os.system(f"autosub {filename} -S de -D de")
		os.system(f"ffmpeg -loop 1 -i image.jpg -i {filename} -c:v libx264 -tune stillimage -c:a aac -b:a 192k -pix_fmt yuv420p -shortest {filename.replace('.mp3','.mp4')}")
		srtfile = open(filename.replace("mp3","srt"),"r")
		vttwrite = open(filename.replace("mp3","vtt"),"w")
		vttwrite.write("WEBVTT\n\n")
		for srt in srtfile.readlines():
			try:
				int(srt)
			except:
				

				try:
					int(srt[0])
					vttwrite.write(srt.replace(",","."))
				except:
					if srt.strip() == "":
						pass
					else:
						vttwrite.write("- "+srt+"\n")

		os.system("rm {}".format(filename.replace(".mp3","srt")))
		return {
			"out":filename.replace("mp3","mp4"),
			"transcript":filename.replace("mp3","vtt")
		}

	if lang == "en":
		#EN
		engine = pyttsx3.init()
		voices = engine.getProperty('voices')
		lang  = request.args.get("lang")
		text = request.args.get("q")
		engine.setProperty('voice', voices[7].id)
		engine. setProperty("rate", 150)
		filename = './static/speechEN{}.mp3'.format(random.randint(1,345346456))
		engine.save_to_file(text, filename)
		engine.runAndWait()
		os.system(f"autosub {filename} -S en -D en")
		os.system(f"ffmpeg -loop 1 -i image.jpg -i {filename} -c:v libx264 -tune stillimage -c:a aac -b:a 192k -pix_fmt yuv420p -shortest {filename.replace('.mp3','.mp4')}")
		os.system("rm {}".format(filename))

		srtfile = open(filename.replace("mp3","srt"),"r")
		vttwrite = open(filename.replace("mp3","vtt"),"w")
		vttwrite.write("WEBVTT\n\n")
		for srt in srtfile.readlines():
			try:
				int(srt)
			except:
				

				try:
					int(srt[0])
					vttwrite.write(srt.replace(",","."))
				except:
					if srt.strip() == "":
						pass
					else:
						vttwrite.write("- "+srt+"\n")


		vttwrite.close()
		os.system("rm {}".format(filename.replace(".mp3","srt")))
		return {
			"out":filename.replace("mp3","mp4"),
			"transcript":filename.replace("mp3","vtt")
		}
@app.route("/textLangDetect")
def textLangDetect():
	q = request.args.get("q")


	lang = single_detection(q, api_key='f2e29ae59187dddd8e935acfc34e6ba0')

	return {"lang": lang}

@app.route("/translate")
def translation():

	to_ = request.args.get("to")
	q = request.args.get("q")
	out ={ "out":ts.google(q, to_language=to_)}
	return redirect("/session/tts?q="+out["out"]+"&lang="+to_)

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

@app.route("/viewer/<filename>")
def viewer(filename):
	return f"""
		<html>
			<video id="video" controls preload="metadata" width="500">
			   <source src="/static/{filename}" type="video/mp4">
			   <track label="English" kind="subtitles" srclang="en" src="/static/{filename.replace('mp4','vtt')}" default>
			</video>
			<script>
			document.getElementById("video").webkitRequestFullscreen();
			document.getElementById("video").requestFullscreen();
			document.getElementById("video").msRequestFullscreen();
			document.getElementById("video").mozRequestFullScreen();
			</script>

		</html>
	"""

@app.route("/session/tts")
def ttsSession():
	q = request.args.get("q")
	lang = request.args.get("lang")
	if lang == "tr":
		lang = "tr-TR"
	if lang == "en":
		lang = "en-UK"
	if lang == "fr":
		lang = "fr-FR"
	if lang == "de":
		lang = "de-DE"
	if lang != None:


		return render_template("demo.html",lang=lang,q=q)
	else:
		return abort(500)
@app.route("/simple.page")
def jsthing():
	return render_template("sample.html")


app.run(debug=True)
