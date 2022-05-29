import requests
from bs4 import BeautifulSoup
from flask import Flask,render_template,request,redirect,make_response
import webbrowser
from azure_translator import Translator



url = input("url:")
lang = input("lang(tr,fr,en,de):")
outWrite = open(input("filename:"),"w")
fromlang = input("from language(fr...):")

page = requests.get(url)
soup = BeautifulSoup(page.content,"html.parser")
from bs4.element import Comment

def tag_visible(element):
    if element.parent.name in ['h1', 'h2', 'p',"h6", 'h5', 'b']:
        return True
    if isinstance(element, Comment):
        return False
    return False


def text_from_html(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)  
    return u" ".join(t.strip() for t in visible_texts)

the_text = text_from_html(page.content)

if lang == "fr":
	lang = "fr-FR"
	import requests, uuid, json

	# Add your key and endpoint
	key = "fb5196570b0b41ef802982e310d54158"
	endpoint = "https://api.cognitive.microsofttranslator.com"

	# Add your location, also known as region. The default is global.
	# This is required if using a Cognitive Services resource.
	location = "canadacentral"

	path = '/translate'
	constructed_url = endpoint + path

	params = {
	    'api-version': '3.0',
	    'from': fromlang,
	    'to': 'fr'
	}

	headers = {
	    'Ocp-Apim-Subscription-Key': key,
	    'Ocp-Apim-Subscription-Region': location,
	    'Content-type': 'application/json',
	    'X-ClientTraceId': str(uuid.uuid4())
	}

	# You can pass more than one object in body.
	body = [{
	    'text': the_text
	}]

	request = requests.post(constructed_url, params=params, headers=headers, json=body)
	response = request.json()
	the_text =  json.loads(json.dumps(response, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': ')))[0]["translations"][0]["text"]


if lang == "en":
	lang = "en-EN"
	import requests, uuid, json

	# Add your key and endpoint
	key = "fb5196570b0b41ef802982e310d54158"
	endpoint = "https://api.cognitive.microsofttranslator.com"

	# Add your location, also known as region. The default is global.
	# This is required if using a Cognitive Services resource.
	location = "canadacentral"

	path = '/translate'
	constructed_url = endpoint + path

	params = {
	    'api-version': '3.0',
	    'from': fromlang,
	    'to': 'en'
	}

	headers = {
	    'Ocp-Apim-Subscription-Key': key,
	    'Ocp-Apim-Subscription-Region': location,
	    'Content-type': 'application/json',
	    'X-ClientTraceId': str(uuid.uuid4())
	}

	# You can pass more than one object in body.
	body = [{
	    'text': the_text
	}]

	request = requests.post(constructed_url, params=params, headers=headers, json=body)
	response = request.json()
	the_text =  json.loads(json.dumps(response, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': ')))[0]["translations"][0]["text"]


if lang == "de":
	lang = "de-DE"
	import requests, uuid, json

	# Add your key and endpoint
	key = "fb5196570b0b41ef802982e310d54158"
	endpoint = "https://api.cognitive.microsofttranslator.com"

	# Add your location, also known as region. The default is global.
	# This is required if using a Cognitive Services resource.
	location = "canadacentral"

	path = '/translate'
	constructed_url = endpoint + path

	params = {
	    'api-version': '3.0',
	    'from': fromlang,
	    'to': 'de'
	}

	headers = {
	    'Ocp-Apim-Subscription-Key': key,
	    'Ocp-Apim-Subscription-Region': location,
	    'Content-type': 'application/json',
	    'X-ClientTraceId': str(uuid.uuid4())
	}

	# You can pass more than one object in body.
	body = [{
	    'text': the_text
	}]

	request = requests.post(constructed_url, params=params, headers=headers, json=body)
	response = request.json()
	the_text =  json.loads(json.dumps(response, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': ')))[0]["translations"][0]["text"]


if lang == "tr":
	lang = "tr-TR"
	import requests, uuid, json

	# Add your key and endpoint
	key = "fb5196570b0b41ef802982e310d54158"
	endpoint = "https://api.cognitive.microsofttranslator.com"

	# Add your location, also known as region. The default is global.
	# This is required if using a Cognitive Services resource.
	location = "canadacentral"

	path = '/translate'
	constructed_url = endpoint + path

	params = {
	    'api-version': '3.0',
	    'from': fromlang,
	    'to': 'tr'
	}

	headers = {
	    'Ocp-Apim-Subscription-Key': key,
	    'Ocp-Apim-Subscription-Region': location,
	    'Content-type': 'application/json',
	    'X-ClientTraceId': str(uuid.uuid4())
	}

	# You can pass more than one object in body.
	body = [{
	    'text': the_text
	}]

	request = requests.post(constructed_url, params=params, headers=headers, json=body)
	response = request.json()
	the_text =  json.loads(json.dumps(response, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': ')))[0]["translations"][0]["text"].replace("    "," ").replace("  "," ")




#translate azure


outWrite.write("""
	<head>
	    <meta charset="UTF-8">
	    <meta http-equiv="X-UA-Compatible" content="IE=edge">
	    <meta name="viewport" content="width=device-width, initial-scale=1.0">
	    <title>Anton by Efe Akaröz</title>
	    <style>
		div{
			word-wrap: break-word; white-space: pre-wrap;
		}
		</style>
	</head>
	<a class="nav"  style="position:fixed;top:1px;left:1px;style:background:#ffffff;border-bottom:1px solid #000;margin-bottom:10px;height:50px;width:100%;">
		<img class="logo-mobile logo-image logo-image-dark" src="https://www.grossessepositif.com/wp-content/uploads/2022/05/12.png" width="125" height="35" alt="Grossesse Positif">
	</a><br><br><br><br>
	<button  onclick="playbtn('"""+lang+"""')"  id="playbtn">TTS</button>


	<div class="texts"> </div>
	<p >"""+the_text+"""</p>
	<p>word:<a href="" id="word"></a></p>
	<script src="https://efeakaroz.pythonanywhere.com/static/api.js"></script>
	
	""")





