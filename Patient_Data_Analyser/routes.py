from flask import Flask,render_template,url_for
from Patient_Data_Analyser import app,db

@app.route("/")
def home():
    return render_template('home.html')
