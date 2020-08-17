from django.shortcuts import render,redirect
from .models import Teacher,Student,Principal,Question,Answers
from .forms import UserForm,TeacherForm,PrincipalForm
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from datetime import date
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from itertools import chain 

# Create your views here.
def index(request):
	return render(request,'index.html')

def teacher_register(request):
	if request.method=='POST':
		user = User.objects.create_user(request.POST.get('username'), request.POST.get('email'), request.POST.get('password'))
		#user.save()
		user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
		detail = Teacher(user=user,email=request.POST.get('email'),level=1,mobile_no=request.POST.get('mobile_no')
			,class_id=request.POST.get('class_id'))
		detail.save()
		#login(request, user)
		return render(request, 'index.html')
	else:
		return render(request, 'teacherreg.html')

def principal_register(request):
	if request.method=='POST':
		detail=UserForm(username=request.POST.get('username'),password=request.POST.get('password'))
		detail.save()
		user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
		detail = Principal(email=request.POST.get('email'),level=2,mobile_no=request.POST.get('mobile_no'))
		detail.save()
		login(request, user)
		return render(request, 'login.html',)
	else:
		return render(request, 'principalreg.html')

def user_login(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        level = request.POST['level']
        #return HttpResponse('user')
        if level==1:
        	detail=Teacher.objects.filter(user=request.user)
        	return render(request, 'teacherPage.html', {'detail': details})
        user = authenticate(username=username, password=password)
        #return HttpResponse(user)
        if user is not None:
            if user.is_active:
                #return HttpResponse('hjgj')
                #login(request, user)
                if level=='1':
                    details = Teacher.objects.filter(user=request.user)
                    return render(request, 'teacherPage.html', {'detail': details})
                else:
                    details = Principal.objects.filter(user=request.user)
                    return HttpResponse('gkjgkjS')
                    return render(request, 'principal_dashboard.html', {'detail': details})
            #     if level==1:
            #         return HttpResponse('ugjh')
            #         details = Teacher.objects.filter(user=request.user)
            #         if 1==details['level']:
            #             return render(request, 'teacher_dashboard.html', {'detail': details})
            #         else:
            #             return render(request, 'login.html', {'error_message': 'You are not authorized'})
            #     else:
            #         details = Principal.objects.filter(user=request.user)
            #         if 2==level:
            #             return render(request, 'principal_dashboard.html', {'detail': details})
            #         else:
            #             return render(request, 'login.html', {'error_message': 'You are not authorized'})
            # else:
            #     return render(request, 'login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'login.html', {'error_message': 'Invalid login'})
    return render(request, 'login.html')

def forma(request):
 	if request.method=="POST":
 		name=request.POST.get("studentname")
 		#return HttpResponse(name)
 		today = date.today()
 		for i in range(1,4):
 			if request.POST.get("exampleRadios"+str(i))=="yes":
 				a=1
 			else:
 				a=0

 			q=Answers(sname=name,choice=a,description=request.POST.get("desc"+str(i)),date=today.strftime("%d/%m/%Y"))
 			q.save()
 		return render(request, 'teacherPage.html')
 	else:
 		student = Student.objects.all()
 		ques = Question.objects.all()
 		l=[]
 		k=[]
 		for i in student:
 			l.append(i.name)
 		for i in ques:
 			k.append(i.query)
 		return render(request, 'form.html',{'names':l,'ques':k})

def cfg():
	dic = {   '01/02/2020': [['a',1,0,1,0,0],['b',0,1,1,0,0],['c',1,1,1,0,1],['d',1,0,1,0,0],['e',0,1,0,1,0]],
	          '10/03/2020': [['a',1,1,1,0,1],['b',0,1,0,0,0],['c',0,1,1,1,0],['d',1,0,0,1,0],['e',1,1,0,0,0]],
	           '21/04/2020': [['a',0,0,1,0,1],['b',1,0,1,1,0],['c',0,1,0,1,1],['d',1,0,0,1,1],['e',0,1,1,1,1]],
	           '15/05/2020': [['a',1,0,1,1,0],['b',0,1,1,0,0],['c',1,0,1,0,1],['d',1,1,1,0,1],['e',0,0,1,0,0]]
	      }
	tot = []
	fig, ax = plt.subplots(2, 2, sharex='col', sharey='row')
	ctr = 0
	p = [(0,0),(0,1),(1,0),(1,1)]
	for items in dic.items():
		if ctr>3:
			break
		(i,j) = p[ctr]
		ctr = ctr+1
		(date,l) = items
		df = pd.DataFrame(l)
		df = df.rename(columns={0: "name"})
		name = 'a'
		select_student = df.loc[df['name'] == name]
		select_student = select_student.loc[:, df.columns != 'name']
		tot.append(list(select_student.iloc[0]))
		ax[i][j].bar(select_student.columns,list(select_student.iloc[0]),label = 'Yes',color = 'c')
		ax[i][j].set_title(date)
	#ax.savefig('1.png')
	k=1
	for items in dic.items():
		(date,l) = items
		df = pd.DataFrame(l)
		df = df.rename(columns={0: "name"})
		select_student = df.loc[:, df.columns != 'name']
		add = df.loc[:, df.columns != 'name'].sum(axis=0)
		y = list(add)
		plt.bar(select_student.columns,y,label = 'Yes',color = 'c') # r color is Red
		plt.xlabel('Questions')
		plt.ylabel('Answers')
		plt.title('Student Analysis')
		plt.legend()
		plt.savefig('./static/assets/{}.png'.format(k))
		k+=1
		plt.clf()
	df = pd.DataFrame(l)
	df = df.rename(columns={0: "name"})
	name = 'a'
	select_student = df.loc[df['name'] == name]
	select_student = select_student.loc[:, df.columns != 'name']
	plt.bar(select_student.columns,select_student.iloc[0],label = 'Yes',color = 'r') # r color is Red
	plt.xlabel('Questions')
	plt.ylabel('Answers')
	plt.title('Student Analysis')
	plt.legend()
	plt.savefig('./static/assets/{}.png'.format(k))

def vis(request):
	ans=Answers.objects.all()
	#cfg()
	d={}
	s={}
	for i in ans:
		if i.date in d:
			c=i.sname
			b=[]
			e=1
			for j in d[i.date]:
				if c in j:
					e=0
					if i.choice:
						j.append(1)
					else:
						j.append(0)
					b.append(j)
				else:
					b.append(j)
			if e==1:
				f = [i.sname]
				if i.choice:
					f.append(1)
				else:
					f.append(0)
				d[i.date].append(f)
			else:
				d[i.date]=b
		else:
			a=[]
			b=[i.sname]
			if i.choice:
				b.append(1)
			else:
				b.append(0)
			a.append(b)
			d[i.date]=a

	#return HttpResponse(d.keys(),d.values())
	cfg()
	return render(request,'viewClass.html')
