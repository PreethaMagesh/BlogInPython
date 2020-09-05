#!C:/Users/DELL/AppData/Local/Programs/Python/Python37/Python
print("Content-Type:text/html")
print()
import cgi

print("<h1> Python part of saving data to database </h1>")
print("<hr/>")
print("<body bgcolor= 'white'>")

form=cgi.FieldStorage()

Title=form.getvalue("Title")
Subtitle=form.getvalue("Subtitle")
Name=form.getvalue("Name")
Date=form.getvalue("Date")
description=form.getvalue("description")

import mysql.connector
con=mysql.connector.connect(user='root',password='python123',host='localhost',database='webpython')
cur=con.cursor()
cur.execute("insert into blog values(%s,%s,%s,%s,%s)",(Title,Subtitle,Name,Date,description))
con.commit()
cur.close()
con.close()
print("<h3> records saved !! </h3>")
print("<a href='http://localhost/Theblog/index.html'> click to go back </a>")
