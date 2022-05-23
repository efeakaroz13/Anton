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
	return body.textContent.replace("\n","..").replace("TTS","");
}


function openSelectorMenu(){
	document.getElementById("menu").style.display = "";
}
