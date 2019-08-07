from flask import Flask, render_template

app = Flask(__name__)


## Variable Zone
listProgrammingLang = ['Python', 'Java', 'C', 'JavaScript']
webTitle = 'Flask Modern Web Development'
title = "Superdeveloper"


@app.route('/')
def hello_world():
    
    return render_template('index.html',
    header=title,
    listBahasaPemrograman=listProgrammingLang,
    judulWebsite=webTitle)
