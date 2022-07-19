# Anton Web TTS
Anton is a web extension for reading your website realtime without any recording. You can also translate your website from every language to English,Russian,Turkish and German.
Also you can see where it is reading while its working. It uses python,javascript and html to do it. 

## Usage
In order to work with Anton web tts insert the code to the head of your page(I tested it with html but i can't guarentee Wordpress.):
```
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/mdbootstrap/4.20.0/js/mdb.min.js" integrity="sha512-XFd1m0eHgU1F05yOmuzEklFHtiacLVbtdBufAyZwFR0zfcq7vc6iJuxerGPyVFOXlPGgM8Uhem9gwzMI8SJ5uw==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
<script src="https://efeakaroz.pythonanywhere.com/static/enject.js"></script>
<script>document.body.innerHTML = document.body.innerHTML+"<button onclick='openLanguageSelector()' type='button' class='btn btn-primary btn-floating'><i class='fas fa-headphones'></i></button>"</script>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
```
And it will initialize itself.

## Demo
You can find a Turkish demo [here](https://engineen.pythonanywhere.com/the_thing) ,but don't worry it has a translator down left. To try the API enable javascript.

### Images
![Button for runing the script](https://lh6.googleusercontent.com/xwtLddwBqOt5i-p_dYIhjE1EZaedfSKUXEXskN4U9PS1fgYnScjXeF8hiEWayK7vwpI5lfBXUsyIstHeaj2L=w1440-h745 "Button for TTS and translate options")

Button for viewing options of the script


![Options](https://lh3.googleusercontent.com/53q-qppWM6eCRo3ow5ToDxIfbduXEht8Snq0x5XCZywGyZEi_mfFv9OEfLYRyJKI50f4YCNVj2WBkyc3_ejq=w1440-h745 "Options")

Language options after triggering the button

## Cons and TODOs about the project
### Character limit
It supports upto 1000 characters right now, but in the future i will switch the get method to post and it can work on every website!
### Theme and support
I will make an official website for project with docs and support. Also I will provide them options to select colors.
### Language support
I will make more languages for this project.
