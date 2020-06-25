from flask import Flask,render_template,url_for,redirect
from Patient_Data_Analyser import app,db
from Patient_Data_Analyser.forms import LoginForm,User,Query
from flask_login import login_user,current_user,logout_user,login_required
from Patient_Data_Analyser.models import Hospital,Patient
import os

@app.route("/")
def homepage():
    p1=os.path.join(app.config['UPLOAD_FOLDER'],'doctor5.jfif')
    p2=os.path.join(app.config['UPLOAD_FOLDER'],'doctor2.png')
    p3=os.path.join(app.config['UPLOAD_FOLDER'],'doctor3.jfif')
    return render_template('homepage.html',image=p1,image2=p2,image3=p3)

@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user=Hospital.query.filter_by(username=form.username.data).first()
        if user.password == form.password.data:
            login_user(user,remember=form.remember.data)
            return redirect(url_for('user'))

        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('homepage'))

dict1={"name":"srinath" ,"class":"12"}
dict2={"name":"bigboss" ,"class":"12"}
dict3={"name":"srinath" ,"class":"12"}
_list=[dict1,dict2,dict3]

@app.route("/table")
def table():
    return render_template('table.html',list=_list)

@app.route("/user")
def user():
    form=User()
    form1=Query()
    if form.validate_on_submit():
        h=Patient(aadhar=form.aadhar.data,admissiontime=form.admissiontime.data,dischargetime=form.dischargetime.data,hospitalid=form.hospitalid.data,doctorid=form.doctorid.data,diseaseid=form.diseaseid.data,remarks=form.remarks.data,status=form.status.data,user_id=current_user.id)
        db.session.add(h)
        db.session.commit()
        return redirect(url_for('homepage'))
    return render_template('user.html',form=form,form1=form1)