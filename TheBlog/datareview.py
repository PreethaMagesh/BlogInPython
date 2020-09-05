#!C:/Users/DELL/AppData/Local/Programs/Python/Python37/Python
print("Content-Type:text/html")
print()
import cgi 
import mysql.connector
import webbrowser

con=mysql.connector.connect(user='root',password='python123',host='localhost',database='webpython')
cmd= "select * from blog"
cur=con.cursor()
cur.execute(cmd)
result = cur.fetchall()

p=[]
for row in result:  

    a = ("</br><h1>%s"%row[0])
    p.append(a)
    b = ("</br><h4>%s"%row[1])
    p.append(b)
    c = ("</br><h4>---  Written by %s ---"%row[2])
    p.append(c)
    d = ("</br><h4> Date: %s"%row[3])
    p.append(d)
    e = ("</br></br></br><h5>%s</br></br></br></br>"%row[4])
    p.append(e)

contents = '''<!DOCTYPE html>
<html  >
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="generator" content="Mobirise v5.0.29, mobirise.com">
  <meta name="viewport" content="width=device-width, initial-scale=1, minimum-scale=1">
  <link rel="shortcut icon" href="assets/images/mbr-121x121.png" type="image/x-icon">
  <meta name="description" content="">
  
  
  <title>Home</title>
  <link rel="stylesheet" href="assets/web/assets/mobirise-icons2/mobirise2.css">
  <link rel="stylesheet" href="assets/tether/tether.min.css">
  <link rel="stylesheet" href="assets/bootstrap/css/bootstrap.min.css">
  <link rel="stylesheet" href="assets/bootstrap/css/bootstrap-grid.min.css">
  <link rel="stylesheet" href="assets/bootstrap/css/bootstrap-reboot.min.css">
  <link rel="stylesheet" href="assets/dropdown/css/style.css">
  <link rel="stylesheet" href="assets/formstyler/jquery.formstyler.css">
  <link rel="stylesheet" href="assets/formstyler/jquery.formstyler.theme.css">
  <link rel="stylesheet" href="assets/datepicker/jquery.datetimepicker.min.css">
  <link rel="stylesheet" href="assets/socicon/css/styles.css">
  <link rel="stylesheet" href="assets/theme/css/style.css">
  <link rel="preload" as="style" href="assets/mobirise/css/mbr-additional.css"><link rel="stylesheet" href="assets/mobirise/css/mbr-additional.css" type="text/css">
  
  
  
  
</head>
<body>
  
  <section class="menu cid-s48OLK6784" once="menu" id="menu1-h">
    
    <nav class="navbar navbar-dropdown navbar-fixed-top navbar-expand-lg">
        <div class="container">
            <div class="navbar-brand">
                <span class="navbar-logo">
                    <a href="index.html#top">
                        <img src="assets/images/mbr-121x121.png" alt="The Blog" style="height: 3.8rem;">
                    </a>
                </span>
                <span class="navbar-caption-wrap"><a class="navbar-caption text-black display-7" href="index.html#top">The Blog</a></span>
            </div>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
                <div class="hamburger">
                    <span></span>
                    <span></span>
                    <span></span>
                    <span></span>
                </div>
            </button>
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav nav-dropdown nav-right" data-app-modern-menu="true"><li class="nav-item"><a class="nav-link link text-black display-4" href="index.html">Home<br></a></li><li class="nav-item"><a class="nav-link link text-black display-4" href="index.html#testimonials1-k">About<br></a></li><li class="nav-item"><a class="nav-link link text-black display-4" href="index.html#form7-l">Write<br></a></li><a class="nav-link link text-black display-4" href="webbrowser.html">Read<br></a></li></ul>
                
                
            </div>
        </div>
    </nav>

</section>

<section class="form7 cid-s8pIJcBC7g" id="form7-l">
    
    
    <div class="container">
        <div class="mbr-section-head">
            <h3 class="mbr-section-title mbr-fonts-style align-center mb-0 display-2"><strong>Blog Data</strong></h3>     
        </div>
        <div class="align-center container">
                %s
        </div>
        </div>
    </div>
</section>
<section class="footer3 cid-s8pJsoofRV" once="footers" id="footer3-m">
    <div class="container">
        <div class="media-container-row align-center mbr-white">
            <div class="row social-row">
                <div class="social-list align-right pb-2">
                <div class="soc-item">
                     <div class="soc-item">
                        <a href="https://www.instagram.com/p/CEWPD23FxXi/?igshid=1luzllmfsrw55" target="_blank">
                            <span class="socicon-instagram socicon mbr-iconfont mbr-iconfont-social"></span>
                        </a>
                    
                    </div></div>
            </div>
            <div class="row row-copirayt">
                <p class="mbr-text mb-0 mbr-fonts-style mbr-white align-center display-7">
                    © Copyright 2020 The Blog
                </p>
            </div>
        </div>
    </div>
</section>


  <script src="assets/web/assets/jquery/jquery.min.js"></script>
  <script src="assets/popper/popper.min.js"></script>
  <script src="assets/tether/tether.min.js"></script>
  <script src="assets/bootstrap/js/bootstrap.min.js"></script>
  <script src="assets/smoothscroll/smooth-scroll.js"></script>
  <script src="assets/parallax/jarallax.min.js"></script>
  <script src="assets/dropdown/js/nav-dropdown.js"></script>
  <script src="assets/dropdown/js/navbar-dropdown.js"></script>
  <script src="assets/touchswipe/jquery.touch-swipe.min.js"></script>
  <script src="assets/formstyler/jquery.formstyler.js"></script>
  <script src="assets/formstyler/jquery.formstyler.min.js"></script>
  <script src="assets/datepicker/jquery.datetimepicker.full.js"></script>
  <script src="assets/theme/js/script.js"></script>
'''%(p)

filename = 'webbrowser.html'
def main(contents, filename):
    output = open(filename,"w")
    output.write(contents)
    output.close()
main(contents, filename)    
webbrowser.open(filename)

print("<a href='webbrowser.html'> click to proceed </a>")

