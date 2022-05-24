/*
#Copyright (c) 2022, Efe Akaröz.
#All rights reserved.
*/

let speech = new SpeechSynthesisUtterance();
function textToSpeech(content){
	speech.lang = "tr-TR";
    speech.text = content;

    speech.volume = 0.9;
    speech.rate = 9.5;
    speech.pitch = 1;

    window.speechSynthesis.speak(speech); 
}
function getTextOfPage(){
	var body= document.body;
	return body.textContent.replace("\n",".").replace("TTS","");
}


function openSelectorMenu(){
	if (document.getElementById("menu").style.display == "none") {
		document.getElementById("menu").style.display = "";
	}else{
		document.getElementById("menu").style.display = "none";
	}
	
}
function french(){
	console.log("a")
	$.getJSON("/translate?"+"from=tr"+"&to=fr&"+"q="+getTextOfPage().replace("&","").replace("?","").replace("\n","."),function(out){
		console.log(out.out)
		const wordslist = []
		var splitter = out.out.split(".")
		for (var s = splitter.length - 1; s >= 0; s--) {
			wordslist.push(splitter[s])
		};
		document.body.innerHTML = "";
		for (var i = wordslist.length - 1; i >= 0; i--) {
			document.body.innerHTML = document.body.innerHTML+"<p>"+wordslist[i]+"</p>"
		};
		
	})
	
}
