import requests
import feedparser
import sqlite3
import smtplib,ssl
from datetime import datetime as dt
link="https://security.access.redhat.com/data/meta/v1/rhsa.rss"
feed=feedparser.parse("rhsa.rss")

""" for entries in feed.entries:
    print("Entry name:{}".format(entries.title))
    print("Entry link:{}".format(entries.link))
    r=requests.get(entries.link)
    print("The response code of the link is:{}".format(r.status_code))
    entries_name=entries.title.split(":")[0:2]
    entries_name=''.join(entries_name)
    with open("{}.html".format(entries_name),'w',encoding="utf-8") as html_file:
        html_file.write(r.text)
        print("Html file '{}.html' created for the topic {}".format(entries_name,entries.title))
    break """

conn=sqlite3.connect('my_database.db')
cursor=conn.cursor()

cursor.execute("select name from rss_log order by ID DESC limit 1;")
last_value=cursor.fetchone()[0]

date=dt.now().strftime("%d-%m-%y")
if feed.entries[0].title != last_value:
    print("New update is:{}".format(feed.entries[0].title))
    query="insert into rss_log (Name,date) values('{}','{}');".format(feed.entries[0].title,date)
    cursor.execute(query)
    print("New entry added")
else:
    print("Still old update:{}".format(last_value))
document=open("index.html","w",encoding="utf-8")
data = """\
<html>
    <head>
        <title>RHEL OS Updates</title>
        <link rel="stylesheet" href="css/styles.css">
        <link rel="stylesheet" href="css/bootstrap.css">
        <script src="js/mind.js"></script>
    </head>

    <body id="body">
        <center>
            <h1>RHEL New Update for week {} </h1>
            <table id="resizable-table" border="1" cellpadding="5" cellspacing="0"
                   class="table table-sm table-hover">
                <tr>
                    <th>#</th>
                    <th>RHSA Name</th>
                    <th>Description</th>
                    <th>Link</th>
                    <th>Published Date</th>
                    <th><button type="button" id="mode" class="btn btn-light btn-sm" onclick="set_mode()"></button><break></th>
                </tr>
""".format(date)
document.write(data)
temp=0
for entries in feed.entries:
    temp+=1
    document.write("<tr>")
    document.write("<td>{}</td>".format(temp))
    document.write("<td>{}</td>".format(entries.title))
    document.write("<td>{}</td>".format(entries.description))
    document.write('<td><a href={0} target="_blank">{0}</a></td>'.format(entries.link))
    document.write("<td>{}</td>".format(entries.published))
    document.write("<td></td>")
    document.write("<td></td>")
    document.write("</tr>")
ending_data = """\
                <script>
                        let dark_mode=document.getElementById("mode");
                        if (window.matchMedia("(prefers-color-scheme: dark)").matches){
                            dark_mode.textContent="☀️";
                            dark_mode.setAttribute("class","btn btn-light btn-sm");
                        }else{
                            dark_mode.textContent="🌙";
                            dark_mode.setAttribute("class","btn btn-dark btn-sm")
                        }
                    </script>
                    </table>
            </center>
        </body>
    </html>
"""
document.write(ending_data)
document.close()
print("Html file index.html created")
cursor.close()
conn.commit()
conn.close()