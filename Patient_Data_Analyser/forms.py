from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField,BooleanField,DateField,IntegerField
from wtforms.validators import DataRequired ,Length,Email,ValidationError
from flask_login import current_user
from flask_wtf.file import FileField, FileAllowed


class LoginForm(FlaskForm):
	

	username= StringField('Username',
	 validators=[DataRequired(),Length(min=2,max=20)])

	password=PasswordField('Password',
		validators=[DataRequired()])

	remember= BooleanField('Remember Me')

	submit =SubmitField('Login')

class User(FlaskForm):
	aadhar =IntegerField('Aadhar',validators=[DataRequired()])
	admissiontime =DateField('Admission Date')
	dischargetime=DateField('Discharge Date')
	hospitalid=IntegerField('Hospital Id')
	doctorid=IntegerField('Doctor Id')
	diseaseid=IntegerField('Disease Id')
	remarks=StringField('Remarks')
	status=StringField('status')
	submit=SubmitField('Upload')

class Query(FlaskForm):
	aadhar=IntegerField('Aadhar',validators=[DataRequired()])
	submit=SubmitField('Search')