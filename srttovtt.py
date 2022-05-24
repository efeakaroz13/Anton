import os

srtfile = open("speech.srt","r")
vttwrite = open("speech.vtt","w")
vttwrite.write("WEBVTT\n")
for srt in srtfile.readlines():
	try:
		int(srt)
	except:
		try:
			int(srt[0])
			vttwrite.write(srt.replace(",",".")+"\n")
		except:
			vttwrite.write("- "+srt+"\n")

vttwrite.close()
