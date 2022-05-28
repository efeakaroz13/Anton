import requests
from bs4 import BeautifulSoup

url = input("Enter URL:")

page = requests.get(url)
soup = BeautifulSoup(page.content,"html.parser")

texts = soup.findAll(text=True)
visible_texts = filter(tag_visible, texts)  
the_text = u" ".join(t.strip() for t in visible_texts)

outWrite = open(input("filename:"),"w")
outWrite.write(soup.prettify().replace("<head>","""
	<head>
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
	<script src="https://cdnjs.cloudflare.com/ajax/libs/mdbootstrap/4.20.0/js/mdb.min.js" integrity="sha512-XFd1m0eHgU1F05yOmuzEklFHtiacLVbtdBufAyZwFR0zfcq7vc6iJuxerGPyVFOXlPGgM8Uhem9gwzMI8SJ5uw==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
	<script src="https://efeakaroz.pythonanywhere.com/static/enject.js"></script>
	<meta charset="UTF-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css" integrity="sha512-KfkfwYDsLkIlwQp6LFnl8zNdLGxu9YAA1QvwINks4PhcElQSvqcyVLLD9aMhXd13uQjoXtEKNosOWaZqXgel0g==" crossorigin="anonymous" referrerpolicy="no-referrer" />

	<link rel="preconnect" href="https://fonts.googleapis.com">
	<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
	<link href="https://fonts.googleapis.com/css2?family=Koulen&display=swap" rel="stylesheet">


	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/mdbootstrap/4.20.0/css/mdb.min.css" integrity="sha512-hj9rznBPdFg9A4fACbJcp4ttzdinMDtPrtZ3gBD11DiY3O1xJfn0r1U5so/J0zwfGOzq9teIaH5rFmjFAFw8SA==" crossorigin="anonymous" referrerpolicy="no-referrer" />

	<script>




		function getTextOfPage(){
			var body= document.body;
			return body.textContent.replace("TTS","").replace("word:","");
		}

		function openLanguageSelector(){
			try{
				document.getElementById("popup").style.display = "";
			}
			catch{
				document.body.innerHTML = document.body.innerHTML+"<div style='position:absolute;left:20%;top:15%;right:20%;width:60%;height:300px;background:#36aeeb;border-radius:10px;padding-top:100px;border:1px solid #fff' id='popup'><center><button onclick='closeTheThing()' style='position:absolute;top:1%;left:1%;background:none;color:white;border:0px'>X</button><button class='btn btn-outline-light'style='background:#fff;' onclick='translateFR()'>🇫🇷</button><button style='background:#fff;' class='btn btn-outline-primary' onclick='translateEN()'>🇬🇧</button><button style='background:#fff;'class='btn btn-outline-danger' onclick='translateTR()'>🇹🇷</button><button style='background:#fff;'class='btn btn-outline-warning' onclick='translateDE()'>🇩🇪</button></center></div>"
			}
		}
		function closeTheThing(){
			document.getElementById("popup").style.display = "none"
		}



		function translateTR(){
			window.location.assign("https://efeakaroz.pythonanywhere.com/translate?q="+getTextOfPage().replace('X🇫🇷🇬🇧🇹🇷🇩🇪','').replace('🇫🇷🇬🇧🇹🇷🇩🇪','')+"&to=tr")
		}
		function translateEN(){
			window.location.assign("https://efeakaroz.pythonanywhere.com/translate?q="+getTextOfPage().replace('X🇫🇷🇬🇧🇹🇷🇩🇪','').replace('🇫🇷🇬🇧🇹🇷🇩🇪','')+"&to=en")
		}
		function translateDE(){
			window.location.assign("https://efeakaroz.pythonanywhere.com/translate?q="+getTextOfPage().replace('X🇫🇷🇬🇧🇹🇷🇩🇪','').replace('🇫🇷🇬🇧🇹🇷🇩🇪','')+"&to=de")
		}
		function translateFR(){
			window.location.assign("https://efeakaroz.pythonanywhere.com/translate?q="+getTextOfPage().replace('x🇫🇷🇬🇧🇹🇷🇩🇪','').replace('🇫🇷🇬🇧🇹🇷🇩🇪','')+"&to=fr")
		}
		setTimeout(() => { document.body.innerHTML = document.body.innerHTML+"<button onclick='openLanguageSelector()' type='button' class='btn btn-primary btn-floating btn-lg' style='position:fixed;left:20px;bottom:20px' ><i class='fas fa-headphones'></i></button>" }, 500);
	</script>

	"""))