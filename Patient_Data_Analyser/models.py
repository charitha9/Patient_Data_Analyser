from Patient_Data_Analyser import db,login_manager
from flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
	return Hospital.query.get(int(user_id))

class Hospital(db.Model,UserMixin):
	id=db.Column(db.Integer,primary_key=True)
	username=db.Column(db.String(20),unique=True,nullable=False)
	password= db.Column(db.String(60),nullable=False)
	patient=db.relationship('Patient',backref='patient',lazy=True)

	def __repr__(self):
		return f"Hospital('{self.username}','{self.password}')"

class Patient(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	aadhar=db.Column(db.Integer,unique=True,nullable=False)
	admissiontime=db.Column(db.String(20))
	dischargetime=db.Column(db.String(30))
	hospitalid=db.Column(db.Integer)
	doctorid=db.Column(db.Integer)
	diseaseid=db.Column(db.Integer)
	remarks=db.Column(db.String(100))
	status=db.Column(db.String(100))
	user_id=db.Column(db.Integer, db.ForeignKey('hospital.id'), nullable=False)
