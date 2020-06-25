from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os

PHOTO_FOLDER=os.path.join('static','photos')

app =Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['UPLOAD_FOLDER'] =PHOTO_FOLDER
db = SQLAlchemy(app)
bcrypt= Bcrypt(app)
login_manager =LoginManager(app)
login_manager.login_view='login'
login_manager.login_message_category='info'
from Patient_Data_Analyser import routes
