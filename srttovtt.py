import os

srtfile = open("static/speechEN223732531.srt","r")
vttwrite = open("static/speechEN223732531.vtt","w")
vttwrite.write("WEBVTT\n\n")
for srt in srtfile.readlines():
	try:
		int(srt)
	except:
		if srt.strip() == "\n":
			pass
		else:
			try:
				int(srt[0])
				vttwrite.write(srt.replace(",","."))
			except:
				vttwrite.write("- "+srt+"\n")


vttwrite.close()
