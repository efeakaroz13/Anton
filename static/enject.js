


function getTextOfPage(){
	var body= document.body;
	return body.textContent.replace("TTS","").replace("word:","");
}

function openLanguageSelector(){
	document.cookie = "textContent="+getTextOfPage().replace('X🇫🇷🇬🇧🇹🇷🇩🇪','').replace('🇫🇷🇬🇧🇹🇷🇩🇪','').replace("\n","  ");
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

	window.location.assign("/translate?to=tr")
}
function translateEN(){
	window.location.assign("/translate?to=en")
}
function translateDE(){
	window.location.assign("/translate?to=de")
}
function translateFR(){
	window.location.assign("/translate?to=fr")
}