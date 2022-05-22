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

function voiceover(){
	textToSpeech(getTextOfPage());

}
/* Highlight reading*/

