import requests
from bs4 import BeautifulSoup
from flask import Flask,render_template,request,redirect,make_response
import webbrowser



url = input("url:")
lang = input("lang(tr-TR,fr-FR,en-EN,de-DE):")
outWrite = open(input("filename:"),"w")

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

response = make_response("Done!")
response.set_cookie("textContent",the_text)



outWrite.write("""
	<head>
	    <meta charset="UTF-8">
	    <meta http-equiv="X-UA-Compatible" content="IE=edge">
	    <meta name="viewport" content="width=device-width, initial-scale=1.0">
	    <title>Anton by Efe Akaröz</title>
	</head>
	<button  onclick="playbtn('"""+lang+"""')"  id="playbtn">TTS</button>


	<div class="texts"> </div>
	<p>"""+the_text+"""</p>
	<p>word:<a href="" id="word"></a></p>
	<script src="/static/api.js"></script>
	""")
return response




