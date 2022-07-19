============================================
anton-web-tts Docs
============================================
---------------------------------------------------------------
This is official documentation of anton-web-tts software.
---------------------------------------------------------------


Introduction
============

Anton is an extension that allows you to convert your website to a listenable page. You can set it up on your website very easily.

Setup
=====

HTML5
-----
You need to use some HTML files to render your website. All you have to do is inserting this code to your head part of HTML:

::
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/mdbootstrap/4.20.0/js/mdb.min.js" integrity="sha512-XFd1m0eHgU1F05yOmuzEklFHtiacLVbtdBufAyZwFR0zfcq7vc6iJuxerGPyVFOXlPGgM8Uhem9gwzMI8SJ5uw==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
  <script src="https://efeakaroz.pythonanywhere.com/static/enject.js"></script>
  <script>document.body.innerHTML = document.body.innerHTML+"<button onclick='openLanguageSelector()' type='button' class='btn btn-primary btn-floating'><i class='fas fa-headphones'></i></button>"</script>
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>


After adding this piece of html code to your HTML's head section you will see a blue headphone icon bottom left of your page.



