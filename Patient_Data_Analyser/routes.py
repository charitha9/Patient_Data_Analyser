from flask import Flask,render_template,url_for,redirect
from Patient_Data_Analyser import app,db
from Patient_Data_Analyser.forms import LoginForm
from flask_login import login_user,current_user,logout_user,login_required
from Patient_Data_Analyser.models import Hospital

@app.route("/")
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
            return redirect(url_for('home'))

        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))