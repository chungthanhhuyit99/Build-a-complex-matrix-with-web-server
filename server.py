#!/usr/bin/python
# coding: utf-8

import cherrypy
import subprocess
import string

text1 = """
<html><body>
<nav class="navbar navbar-inverse navbar-fixed-top">
<div class="container">
<div class="navbar-header">
<h3 class="text-muted">IOT</h3>
</div>
</div>
</nav>
<div class="jumbotron">
<div class="container" align=center>
<h1>LED Message Board</h1>
<div class="row extra-bottom-padding">
<img src="/images/led_150x150.jpg" alt="LED array">
</div>
<div class="row extra-bottom-padding">
<form method='get'action="do_it" >
<div class="form-group">
<label class="sr-only" for="message">Message</label>
<input type="text"  name="msg" placeholder="Display message">
</div>
<button type="submit">Display</button>
</form>
</div>
</div>
</div>
</body>
{}
</html>
"""
text="""<html>
          <head></head>
          <body>
            <form method="get" action="do_it">
              <input type="text" value="8" name="length" />
              <button type="submit">Give it now!</button>
            </form>
          </body>
        </html>"""
text2="""<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content m
ust come *after* these tags -->
    <title>Send Message</title>

    <!-- Bootstrap -->
    <link href="../static/css/bootstrap.min.css" rel="stylesheet">

    <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries
 -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
    <script src="https://oss.maxcdn.com/html5shiv/3.7.3/html5shiv.min.js"></script>
    <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    <![endif]-->

    <!--local style-->
    <style>
    .form-inline .form-group input {
	width:300px;
    }
    .row.extra-bottom-padding{
	   margin-bottom: 30px;
    }
    </style>

  </head>

  <body style="margin-top:50px">

    <nav class="navbar navbar-inverse navbar-fixed-top">
    <div class="container">
      <div class="navbar-header">
        <h3 class="text-muted">IoT</h3>
      </div>
    </div>
    </nav>

<div class="jumbotron">
  <div class="container" align=center>
  <h1>LED Message Board</h1>
    <div class="row extra-bottom-padding">
    <form  action="do_it" method="get">
      <div class="form-group">
        <label  for="message">Message</label>
        <input type="text"  name="msg" placeholder="Display message">
      </div>
      <button type="submit">Display</button>
    </form>
  </div>
  </div>

  </div>
  </body>
</html>"""

class PiButton(object):
    @cherrypy.expose
    def index(self):
        return text2

    @cherrypy.expose
    def do_it(self,msg):
        #command = "ls /"
        command = "python runtext.py "+msg
        result = subprocess.Popen(command, shell=True)
        return text2


if __name__ == "__main__":
    cherrypy.engine.autoreload.unsubscribe()
    cherrypy.config.update({'server.socket_host': "0.0.0.0", 'server.socket_port': 8181})
    cherrypy.quickstart(PiButton())
