from django.db import models
from django.contrib.auth.models import User

class Teacher(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	email=models.EmailField()	
	level=models.IntegerField(default=1)
	mobile_no=models.IntegerField()
	class_id=models.CharField(max_length=2,primary_key=True)
	USERNAME_FIELD='username'

	def __str__(self):
		return self.user.username

class Student(models.Model):
	student=models.ForeignKey(Teacher,on_delete=models.CASCADE)
	name=models.CharField(max_length=20,primary_key=True)
	mobile_no=models.IntegerField()
	#student_id=models.AutoField(primary_key=True)

	def __str__(self):
		return self.name

class Principal(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	level=models.IntegerField(default=2)
	email=models.EmailField()	
	mobile_no=models.IntegerField()
	USERNAME_FIELD='username'

	def __str__(self):
		return self.user.username

class Question(models.Model):
	Question_id=models.IntegerField(primary_key=True)
	query=models.CharField(max_length=150)
	category = models.CharField(max_length=20, default='analytics')
	def __str__(self):
		a=str(self.Question_id)
		return a+" "+self.category
	
class Answers(models.Model):
	# qid=models.IntegerField()
	sname = models.CharField(max_length=20)
	choice=models.BooleanField()
	description=models.CharField(max_length=250)
	date = models.CharField(max_length=50,default="0")