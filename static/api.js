/*
#Copyright (c) 2022, Efe Akaröz.
#All rights reserved.
*/



function getTextOfPage(){
	var body= document.body;
	return body.textContent.replace("TTS","").replace("word:","");
}




var utterance = new SpeechSynthesisUtterance();
var wordIndex = 1;
var global_words = [];
utterance.lang = 'en-UK';
utterance.rate = 1;


function playbtn(lang){
    var text    = getTextOfPage()
    var words   = text.split(" ");
    utterance.lang = lang;
    global_words = words;
    // Draw the text in a div
    drawTextInPanel(words);
    spokenTextArray = words;
    utterance.text = text;
    speechSynthesis.speak(utterance);

};

utterance.onboundary = function(event){
	var e = getTextOfPage();
	var word = getWordAt(e,event.charIndex);
// Show Speaking word : x
	document.getElementById("word").innerHTML = word;
//Increase index of span to highlight
console.info(global_words[wordIndex]);

try{
	document.getElementById("word_span_"+wordIndex).style.backgroundColor = "#ec78f5";
	document.getElementById("word_span_"+wordIndex).style.color = "white";

}catch(e){}

wordIndex++;
};

utterance.onend = function(){
	document.getElementById("word").innerHTML = "";
    wordIndex = 1;
    document.getElementById("panel").innerHTML = "";
};

// Get the word of a string given the string and the index
function getWordAt(str, pos) {
    // Perform type conversions.
    str = String(str);
    pos = Number(pos) >>> 0;

    // Search for the word's beginning and end.
    var left = str.slice(0, pos + 1).search(/\S+$/),
        right = str.slice(pos).search(/\s/);

    // The last word in the string is a special case.
    if (right < 0) {
        return str.slice(left);
    }
    // Return the word, using the located bounds to extract it from the string.
    return str.slice(left, right + pos);
}

function drawTextInPanel(words_array){
console.log("Dibujado");
		document.body.innerHTML = document.body.innerHTML+"<div id='panel'></div>"
		var panel = document.getElementById("panel");
  	for(var i = 0;i < words_array.length;i++){
    	var html = '<span id="word_span_'+i+'">'+words_array[i]+'</span>&nbsp;';
    	panel.innerHTML += html;
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
