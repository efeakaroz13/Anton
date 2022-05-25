( async() =>{
	async function say(content){
		var msg = new SpeechSynthesisUtterance(content);

		msg.lang = "en-ZA"
		window.speechSynthesis.speak(msg);
	}
	async function doAll(){
		words = getAllText().split(".").reverse()
		console.log("a")
		document.body.innerHTML = document.body.innerHTML+"<p>Say 'stop TTS' for stop</p>"
		const texts = document.body

			window.SpeechRecognition =
		  	window.SpeechRecognition || window.webkitSpeechRecognition;

			const recognition = new SpeechRecognition();
			recognition.interimResults = true;
			recognition.lang = 'en-GB';

			let p = document.createElement("a");

			recognition.addEventListener("result", (e) => {
			  texts.appendChild(p);
			  const text = Array.from(e.results)
			    .map((result) => result[0])
			    .map((result) => result.transcript)
			    .join("");

			  p.innerText = text;
			  
			  if(text.includes("stop")){
			  	window.location.assign("/demo")
			  }
			  if (e.results[0].isFinal) {
			    if (text.includes("how are you")) {
			      p = document.createElement("p");
			      p.classList.add("replay");
			      p.innerText = "I am fine";
			      texts.appendChild(p);
			    }
			    if (
			      text.includes("what's your name") ||
			      text.includes("what is your name")
			    ) {
			      p = document.createElement("p");
			      p.classList.add("replay");
			      p.innerText = "My Name is Cifar";
			      texts.appendChild(p);
			    }
			    if (text.includes("open my YouTube")) {
			      p = document.createElement("p");
			      p.classList.add("replay");
			      p.innerText = "opening youtube channel";
			      texts.appendChild(p);
			      console.log("opening youtube");
			      window.open("https://www.youtube.com/channel/UCdxaLo9ALJgXgOUDURRPGiQ");
			    }
			    p = document.createElement("p");
			  }
			});

		recognition.addEventListener("end", () => {
		  recognition.start();
		});

		recognition.start();
		for (var i = words.length - 1; i >= 0; i--) {
			await say(words[i]);
			await changeItemVal(words[i])

			
		};
		window.location.assign("/demo")
	
	
	

	}
	async function changeItemVal(content){
		document.getElementById("viewer").value = content;
	}
	function getAllText(){
		allText = document.body.textContent;
		document.body.innerHTML = "";
		return allText
	}
	 document.getElementById("idButton").onclick=async ()=>{
            await doAll();
        };


})();
