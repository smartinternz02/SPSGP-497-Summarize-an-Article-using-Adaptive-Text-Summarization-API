from flask import Flask, request, render_template 
import numpy as np
import re
import requests

app = Flask(__name__)

def check(typ,output):
    url = "https://textanalysis-text-summarization.p.rapidapi.com/text-summarizer"
    #payload = "{\"url\": \""+output+"\",\"text\": \"\",\"sentnum\": 8}"
    payload='''{"url":"'''+output+'''","text":"","sentnum":8}'''
    print(payload)
    headers = {
    'content-type': "application/json",
    'x-rapidapi-key': "537649ff73msh477f6855911bb13p129cf4jsnd5cb001617b2",
    'x-rapidapi-host': "textanalysis-text-summarization.p.rapidapi.com"
    } 
    response = requests.request("POST", url, data=payload, headers=headers)
    return response.json()["sentences"]
    
#home page 
@app.route('/') 
def home(): 
    return render_template('home.html') 

#summarizer page 
@app.route('/summarizer')
def summarizer():
    return render_template('summarizer.html')
    
#Results screen 
@app.route('/summarize',  methods=['POST'])
def summarize():
    typ="text"
    output = request.form.get("article") 
    print(output) 
    essay = ''.join(check(typ,output)) 
    return render_template('summary.html',essay=essay)
    
if __name__ == "__main__": 
    app.run()