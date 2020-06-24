from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField,BooleanField
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