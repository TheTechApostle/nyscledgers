from django.shortcuts import render, redirect
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import  status
from .serializers import CorpRegisterSerializer
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
from .form import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import *
import re
import csv
import datetime
from django.db.models import Q

from django.contrib.auth.forms import UserCreationForm
#logn here
from django.contrib.auth import authenticate, login, logout
# Create your views here.
import csv
from datetime import datetime




def members(request):
	if request.method == 'GET':
		form = LoginForm()
		return render(request,'index.html', {'form': form})
	elif (request.method == 'POST'):
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request, username=username, password=password)
			
			

		if user is not None:
			login(request, user)
			# h= request.user.courses
			return redirect('/nyscledger/dashboard/')
		else:
			messages.info(request, 'Username or password is incorrect!')
	form = LoginForm()
	
	return render(request, 'index.html', {'form': form})


def register(request):
	# context = {}
	if request.method == "POST":
		fn  = request.POST['firstname']
		ln  = request.POST['lastname']
		sc  = request.POST['statecode']
		sr  = request.POST['sor']
		st  = request.POST['statedeployed']
		cd  = request.POST['cds']
		pcds  = request.POST['pcds']
		ph  = request.POST['phone']
		pry  = request.FILES['profile']

		bv = CorpRegister(firstname=fn, lastname=ln, statecode=sc, sor=sr, statedeployed=st, cds=cd, pcds=pcds, phone=ph, profile=pry)

		bv.save()
		messages.success(request, 'Course Addedd successfully')
		mycds = cds.objects.all().count()
		dcds = cds.objects.all()
		context = {'mycds':mycds,'dcds':dcds}
		return render(request, 'register.html', context)
	else:
		mycds = cds.objects.all().count()
		dcds = cds.objects.all()
		context = {'mycds':mycds,'dcds':dcds}
		messages.error(request, 'Pls Check and Add Right Course')
		return render(request, 'register.html', context)
		 
	# 	form = corpReg(request.POST, request.FILES)
	# 	if form.is_valid():
	# 		vt = form.cleaned_data.get('statecode')
	# 		check = CorpRegister.objects.filter(statecode=vt)
	# 		if check.exists():
	# 			messages.error(request, 'Registration Failed')
	# 		else:
	# 			register = form.save(commit=False)
	# 			register.save()
				
	# 	messages.success(request, 'Registration Successful')
	# else:
	# 	form = corpReg()
	# 	context = {'form':form,'mycds':mycds,'dcds':dcds}
	# 	messages.error(request, 'Registration Failed')

	

# def goattendance(request):
# 	if request.method==POST:
# 		form =  attendance(request.POST, request.FILES)
# 		if form.is_valid():
# 			myvt = form.cleaned_data('statecode')
# 			check = attendance.objects.filter(statecode=statecode)

# 			if check.exists():
# 				messages.error(request, 'Attendance Failed to Add')
# 			else:
# 				register = form.save(commit=False)
# 				register.save()

# 	else:
# 		form = attendance()
# 	messages.error(request, 'Authetication failed')
# 	return render(request, 'goattendance.html', {'form':form})

# @unauthenticated_user
def adminReg(request):
	form = RegisterForm()
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user=form.save()
			username = form.cleaned_data.get('username')
			# group = Group.objects.get(name='student')
			# user.groups.add(group)
			# Student.objects.create(
			# 	user=user
			# )
	context = {'form':form}
	return render(request, 'adminReg.html', context)

# @unauthenticated_user

def dashboard(request):
	
	messages.error(request, 'Registration Failed')
	mycds = cds.objects.all().count()
	dcds = cds.objects.all()
	myppa = ppa.objects.all().count()
	coR = CorpRegister.objects.all().count()
	coRz = CorpRegister.objects.all().order_by('cds','firstname').distinct()
	coRzcount = CorpRegister.objects.all().values('cds').order_by('cds').distinct().count()
	page = request.GET.get('page', 1)
	paginator = Paginator(coRz, 20)
	try:
		users = paginator.page(page)
	except PageNotAnInteger:
		users = paginator.page(1)
	except EmptyPage:
		users = paginator.page(paginator.num_pages)
	if request.method == "POST":
		form = corpReg(request.POST, request.FILES)
		if form.is_valid():
			vt = form.cleaned_data.get('statecode')
			check = CorpRegister.objects.filter(statecode=vt)
			if check.exists():
				messages.error(request, 'Data Exists, Register another Data')
			else:
				register = form.save(commit=False)
				register.save()
				
		messages.success(request, 'Registration Successful')
	else:
		form = corpReg()
	hist = addattendance.objects.all().count()
	context = {'corP':coR, 'coRz':users, 'ppa':myppa, 'cds':mycds, 'hist':hist,'form':form,'dcds':dcds}
	messages.error(request, 'Kindly Registration')
	return render(request, 'dashboard.html', context)


def attendance(request):
	addin = addattendance.objects.all()
	month = ['January','Febuary','March','April','May','June','July','August','Setember','October','November','December']
	mycds = cds.objects.all().count()
	myppa = ppa.objects.all().count()
	coR = CorpRegister.objects.all().count()
	coRz = CorpRegister.objects.values()
	hist = addattendance.objects.all().count()
	context = {'corP':coR, 'coRz':coRz, 'ppa':myppa,'hist':hist, 'cds':mycds, 'xd':range(1,32), 'm':month, 'y':range(2022,2090), 'addin':addin }
	if request.method == "POST":
		day = request.POST['day']
		month = request.POST['month']
		year = request.POST['year']
		purpose = request.POST['purpose']
		date_created = datetime.now()

		request.session['day'] = day
		request.session['month'] = month
		request.session['year'] = year
		
		docheck  = addattendance.objects.filter(day=day, month=month, year=year)
		if docheck:
			messages.success(request, 'Attendance already Exists Add Another')
			return HttpResponse('Oops Attendance already registered')
		else:
			
			dhj = CorpRegister.objects.all()
			for x in dhj:
				lname = x.lastname
				fname = x.firstname
				dcds= x.cds
				mprofile = x.profile
				status = 0
				day = day
				month = month
				year = year
				date_created = date_created
				userid = x.id
				userid = x.id
				st = x.statecode
				attendance = TakeAttendance(day=day, month=month, year=year, status=status, date_created = date_created, user_id=userid, id=userid, mystatecode=st, firstname=fname,lastname=lname,cds=dcds,profile=mprofile)
				attendance.save()
			goattendance = addattendance(day=day, month=month, year=year, purpose=purpose, date_created = date_created)
			goattendance.save()
			
			
			messages.success(request, 'Attendance Added Successfully')
			return HttpResponseRedirect(reverse('doattendance'))
			
	else:
		
		return render(request, 'attendance.html', context)



def  export_to_csv(request):
	CorpReg = CorpRegister.objects.all()
	response = HttpResponse('text/csv')
	response['content-disposition'] = 'attachment; filyename=corp_register.csv'
	writer = csv.writer(response)
	writer.writerow(['State Code','First Name', 'Last Name','CDS', 'PPA', 'status'])
	profile_fields = CorpReg.values_list('statecode','firstname', 'lastname','cds','ppa','status_active')

	for profile in profile_fields:
		writer.writerow(profile)
	return response


def deleteRegister(request, id):
	delCorp = CorpRegister.objects.get(id=id)
	delCorp.delete()

	return HttpResponseRedirect(reverse('dashboard'))

def deleteFile(request, id):
	delCorp = document.objects.get(id=id)
	delCorp.delete()

	return HttpResponseRedirect(reverse('documents'))


def doattendance(request):
	

	goattendance = addattendance.objects.values().last
	coRzif = CorpRegister.objects.all()
	emif = TakeAttendance.objects.all().distinct()

	# coRz = CorpRegister.objects.all().order_by('cds')
	
    
	io = cds.objects.all().distinct()
	
	day = request.session['day']
	month=request.session['month']
	year=request.session['year']
	coRzcount = TakeAttendance.objects.filter(day=day,month=month,year=year).values('cds').order_by('cds').distinct().count()
	Onstatuscount = TakeAttendance.objects.filter(day=day,month=month,year=year, status=1).count()
	Offstatuscount = TakeAttendance.objects.filter(day=day,month=month,year=year, status=0).count()
	coRz = TakeAttendance.objects.filter(day=day,month=month,year=year).order_by('cds','firstname').all()
	page = request.GET.get('page', 1)
	paginator = Paginator(coRz, coRzcount)
	try:
		users = paginator.page(page)
	except PageNotAnInteger:
		users = paginator.page(1)
	except EmptyPage:
		users = paginator.page(paginator.num_pages)
	for x in coRz:
		statusN = x.id
		st = x.statecode
		ct = TakeAttendance.objects.filter(user_id=statusN) 
		coRcz = TakeAttendance.objects.filter(day=day,month=month,year=year).order_by('firstname','cds')
	
	context = {'my':goattendance, 'coRz':users,'ct':ct,'coRcz':coRcz, 'cds':io,'coRzcount':coRzcount,'coRzif':coRzif, 'emif':emif, 'on':Onstatuscount,'off':Offstatuscount}
	if request.method == "POST":
		query_name = request.POST.get('search_query')
		if query_name:
			check = Q(firstname__icontains=query_name) | Q(lastname__icontains=query_name) | Q(statecode__icontains=query_name) | Q(cds__icontains=query_name)
			
			users = TakeAttendance.objects.filter(Q(firstname__icontains=query_name) | Q(lastname__icontains=query_name) | Q(statecode__icontains=query_name) | Q(cds__icontains=query_name),day=day,month=month,year=year).order_by('firstname','cds')
			
			return render(request, 'submitAttendance.html', {'coRz':users,'my':goattendance,'coRcz':coRcz, 'on':Onstatuscount,'off':Offstatuscount})
		else:
			print("NO Information to show")
			return render(request, 'doattendance.html',)
	
	return render(request, 'doattendance.html', context)


def submitAttendance(request,id):
	
	
	if request.session.get('day'):
		day = request.session.get('day')
	if request.session.get('month'):
		month = request.session.get('month')
	if request.session.get('year'):
		# year = "Year : {0} <br>".format(request.session.get('year'))
		year = request.session.get('year')

		response = {'day':day,'month':month,'year':year}
	get_details = TakeAttendance.objects.get(user_id=id, day=day, month=month, year=year)
	if get_details.status == 1:
		get_details.status = 0
		
		return HttpResponse('Attendance Already Added for this Statecode')
	if get_details:
		
		# is_private = request.POST.get('is_private', False);
		userid = get_details.id
		st = get_details.statecode
		mday = day
		mmonth = month
		myear = year
		date_created = datetime.now()
		sts = 1
		get_details.status= sts
		fname = get_details.firstname
		lname = get_details.lastname
		cds = get_details.cds
		profile = get_details.profile
		
		# mark = attendance.objects.filter(statecode=sts)
		if userid == get_details.id:
			# attendance = TakeAttendance(day=day, month=month, year=year, status=status, date_created = date_created, user_id=userid, statecode_id=userid, mystatecode=st, firstname=fname,lastname=lname,cds=cds,profile=profile)
			check = TakeAttendance.objects.filter(day=day, month=month, year=year, statecode=userid, status=sts, mystatecode=st)
			if check.exists():
				return HttpResponse('Attendance Already Added for this Statecode')
				return HttpResponseRedirect(reverse('doattendance'), {'marked'})
			else:
				get_details.save()
				marked = "marked"
				return HttpResponseRedirect(reverse('doattendance'))
				
				# del request.session.get['year']
		# mydata = attendance(statecode=st, user_id=userid, day=day, month=month, year=year, status=status)
		# mydata.save()
		# messages.success(request, 'User Added Successfully')
		# return HttpResponseRedirect(reverse('submitAttendance'))

		else:
			return render(request, 'submitAttendance.html', {'corz':check})

		
		

	

	return render(request, 'submitAttendance.html', {'get':get_details,'response':response,})


def getdone(request,id):
	
	
	if request.session.get('day'):
		day = request.session.get('day')
	if request.session.get('month'):
		month = request.session.get('month')
	if request.session.get('year'):
		# year = "Year : {0} <br>".format(request.session.get('year'))
		year = request.session.get('year')

		response = {'day':day,'month':month,'year':year}
	get_details = TakeAttendance.objects.get(user_id=id, day=day, month=month, year=year)
	if get_details.status == 1:
		get_details.status = 0
		
		return HttpResponse('Attendance Already Added for this Statecode')
	if get_details:
		
		# is_private = request.POST.get('is_private', False);
		userid = get_details.id
		st = get_details.statecode
		mday = day
		mmonth = month
		myear = year
		date_created = datetime.now()
		sts = 1
		get_details.status= sts
		fname = get_details.firstname
		lname = get_details.lastname
		cds = get_details.cds
		profile = get_details.profile
		
		# mark = attendance.objects.filter(statecode=sts)
		if userid == get_details.id:
			# attendance = TakeAttendance(day=day, month=month, year=year, status=status, date_created = date_created, user_id=userid, statecode_id=userid, mystatecode=st, firstname=fname,lastname=lname,cds=cds,profile=profile)
			check = TakeAttendance.objects.filter(day=day, month=month, year=year, statecode=userid, status=sts, mystatecode=st)
			if check.exists():
				return HttpResponse('Attendance Already Added for this Statecode')
				return HttpResponseRedirect(reverse('ll'), {'marked'})
			else:
				get_details.save()
				marked = "marked"
				return HttpResponseRedirect(reverse('doattendance'))
				
				# del request.session.get['year']
		# mydata = attendance(statecode=st, user_id=userid, day=day, month=month, year=year, status=status)
		# mydata.save()
		# messages.success(request, 'User Added Successfully')
		# return HttpResponseRedirect(reverse('submitAttendance'))

		else:
			return render(request, 'submitAttendance.html', {'corz':check})

		
		

	

	return render(request, 'submitAttendance.html', {'get':get_details,'response':response,})


def ll(request):
	return render(request,'ll.html')

def attendance_history(request):
	addin = addattendance.objects.all()
	month = ['January','Febuary','March','April','May','June','July','August','Setember','October','November','December']
	mycds = cds.objects.all().count()
	myppa = ppa.objects.all().count()
	coR = CorpRegister.objects.all().count()
	hist = addattendance.objects.all().count()
	coRz = CorpRegister.objects.values()
	
	Acount = "hello"
	

	
	context = {'corP':coR, 'coRz':coRz,'hist':hist, 'ppa':myppa, 'cds':mycds, 'xd':range(1,32), 'm':month, 'y':range(2024,2090), 'addin':addin}
	if request.method == "POST":
		day = request.POST['day']
		month = request.POST['month']
		year = request.POST['year']
		purpose = request.POST['purpose']
		date_created = datetime.now()

		request.session['day'] = day
		request.session['month'] = month
		request.session['year'] = year
		
		docheck  = addattendance.objects.filter(day=day, month=month, year=year)
		if docheck:
			
			lol_count = TakeAttendance.objects.filter(day=day, month=month, year=year, status=1).count()
			df_exclude_count = TakeAttendance.objects.filter(day=day, month=month, year=year, status=0).count()
			lol = TakeAttendance.objects.filter(day=day, month=month, year=year, status=1)
			mylol = TakeAttendance.objects.filter(day=day, month=month, year=year).all()
			df_exclude = TakeAttendance.objects.filter(day=day, month=month, year=year, status=0)
			lold = TakeAttendance.objects.select_related('statecode').all()
			loly = TakeAttendance.objects.filter(day=day, month=month, year=year, status=1).first()
			context = {'corP':coR, 'coRz':coRz, 'ppa':myppa, 'cds':mycds, 'xd':range(1,32), 'm':month, 'y':range(2024,2090), 'addin':addin,'coRcz':lol, 'coRczc':loly,'Pcount':lol_count,'Acount':Acount,'hist':hist, 'lold':lold, 'df_exclude_count':df_exclude_count,'df_exclude':df_exclude}
			messages.success(request, 'Attendance Successfully Fetch')
			resonse = 'attendance_history.html'	
			
			return render(request, 'attendance_history.html', context)
			# messages.success(request, 'Attendance already Exists Add Another')
		else:
			month = ['January','Febuary','March','April','May','June','July','August','Setember','October','November','December']
			messages.success(request, 'No Attendance Registered this Specific Date')
			return render(request, 'attendance_history.html', context)
	else:
		
		context = {'corP':coR, 'coRz':coRz, 'ppa':myppa, 'cds':mycds, 'xd':range(1,32), 'm':month, 'y':range(2024,2090), 'addin':addin, 'Acount':Acount,'hist':hist}	
		return render(request, 'attendance_history.html', context)

def editregister(request, id):
	get_id = CorpRegister.objects.get(id=id)
	gh = CorpRegister.objects.get(id=id)
	pa = ppa.objects.all().order_by('name').values()
	ca = cds.objects.all().order_by('name').values()
	context = {'get_id':get_id,'ppa':pa, 'cds':ca}
	# myprofile = get_id.profile
	
	# request.session['profile'] = myprofile
	

	if request.method == "POST":
		get_id.firstname = request.POST['firstname']
		get_id.lastname = request.POST['lastname']
		get_id.statecode = request.POST['statecode']
		get_id.cds = request.POST['cds']
		get_id.ppa = request.POST['ppa']
		get_id.status_active = request.POST['status_active']
		# if request.FILES['profile'] == '':

			# return HttpResponse('what')

			# get_id.profile = myprofile
		get_id.save()
		return render(request, 'editregister.html', context)
		
	
	return render(request, 'editregister.html', context)



def  history_export_to_csv(request):
	if request.session.get('day'):
		day = request.session.get('day')
	if request.session.get('month'):
		month = request.session.get('month')
	if request.session.get('year'):
		year = request.session.get('year')
	myAttendance = TakeAttendance.objects.all().filter(day=day, month=month, year=year)
	response = HttpResponse('text/csv')
	response['content-disposition'] = 'attachment; filename=corp_register.csv'
	writer = csv.writer(response)
	# date = day,month,year
	# mydate = date
	writer.writerow(['State Code','First Name', 'Last Name','CDS', 'status', 'day','month','year'])
	profile_fields = myAttendance.values_list('mystatecode','firstname', 'lastname','cds','status','day','month','year')

	for profile in profile_fields:
		writer.writerow(profile)
	return response


def documents(request):
	# if request.method == "POST":
	# 	forms = DocumentFile(request.POST, request.FILES)

	# 	if form.is_valid():
	# 		document = form.save(commit=False)
	# 		document.save()

	doc = document.objects.all()
	docy = document.objects.all().count()
	context = {'doc':doc,'docy':docy}
	# context = {'form':forms}

	return render(request, 'documents.html', context)



@api_view(['GET','POST'])
def CorpRegister_list(request):

	if request.method =="GET":
		corp = CorpRegister.objects.all()
		serializer = CorpRegisterSerializer(corp, many=True)
		return JsonResponse({'serializer':serializer.data}, safe=False)

	if request.method =="POST":
		serializer = CorpRegisterSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()

			return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET','PUT','DELETE'])
def CorpRegister_details(request, id):

	try:
		corp = CorpRegister.objects.get(pk=id)
	except CorpRegister.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == "GET":
		serializer = CorpRegisterSerializer(corp)
		return Response(serializer.data)
	elif request.method == "PUT":
		serializer = CorpRegisterSerializer(corp, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)

		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	elif request.method=="DELETE":
		pass



def import_csv(request):
    if request.method == 'POST':
        form = CSVImportForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file'].read().decode('ISO-8859-1').splitlines()
            csv_reader = csv.DictReader(csv_file)

            for row in csv_reader:
                CorpRegister.objects.create(
	                firstname=row['firstname'],
	                lastname=row['lastname'],
	                cds=row['cds'],
	                pcds=row['pcds'],
	                sor=row['sor'],
	                statedeployed=row['statedeployed'],
	                statecode=row['statecode'],
	                ppa=row['ppa'],
	                batch=row['batch'],
	                phone=row['phone'],
	                status_active=row['status_active'],
	                profile=row['profile']
            	)

            return redirect('success_page')  # Redirect to a success page
    else:
        form = CSVImportForm()

    return render(request, 'book.html', {'form': form})


def ppa_import_csv(request):
    # if request.method == 'POST':
    #     form = CSVImportFormPPA(request.POST, request.FILES)
    #     if form.is_valid():
    #         csv_file = request.FILES['csv_file'].read().decode('ISO-8859-1').splitlines()
    #         csv_reader = csv.DictReader(csv_file)

    #         for row in csv_reader:
    #             ppa.objects.create(
	                
	               
	#                 name = row['name'],
	#                 category = row['category'],
	#                 address = row['address'],
	#                 empNo = row['empNo'],
    #         	)

    #         return redirect('success_page')  # Redirect to a success page
    # else:
    #     form = CSVImportFormPPA()
  
	coR = CorpRegister.objects.all().count()
	users = CorpRegister.objects.all().order_by('cds','firstname')
	mycds = cds.objects.all().count()
	hist = addattendance.objects.all().count()
	dcds = cds.objects.all()
	myppa = ppa.objects.all().count()
	if request.method == 'POST':
		lil = request.POST['searchppa']
		dyppa = ppa.objects.all().order_by('name').distinct()
		users = CorpRegister.objects.filter(ppa=lil).all()
		context = {'dyppa':dyppa,'coRz':users,'cds':mycds,'ppa':myppa,'corP':coR,'hist':hist}
		return render(request, 'ppa.html', context)
	else:
		dyppa = ppa.objects.all().order_by('name').distinct()
		context = {'dyppa':dyppa,'coRz':users, 'cds':mycds,'ppa':myppa, 'corP':coR,'hist':hist}
		return render(request, 'ppa.html', context)


def success_page(request):
	return render(request, 'success_page.html')



def mycds(request):
	mycds = cds.objects.all().count()
	myppa = ppa.objects.all().count()

	context = {'cds':mycds,'ppa':myppa}

	return render(request, 'mycds.html', context)


def mydashi(request):
	messages.error(request, 'Registration Failed')
	mycds = cds.objects.all().count()
	dcds = cds.objects.all()
	myppa = ppa.objects.all().count()
	coR = CorpRegister.objects.all().count()
	
	coRz = CorpRegister.objects.all().order_by('cds','firstname').distinct()
	coRzcount = CorpRegister.objects.all().values('cds').order_by('cds').distinct().count()
	page = request.GET.get('page', 1)
	paginator = Paginator(coRz, 20)
	try:
		users = paginator.page(page)
	except PageNotAnInteger:
		users = paginator.page(1)
	except EmptyPage:
		users = paginator.page(paginator.num_pages)
	if request.method == "POST":
		form = corpReg(request.POST, request.FILES)
		if form.is_valid():
			vt = form.cleaned_data.get('statecode')
			check = CorpRegister.objects.filter(statecode=vt)
			if check.exists():
				messages.error(request, 'Data Exists, Register another Data')
			else:
				register = form.save(commit=False)
				register.save()
				
		messages.success(request, 'Registration Successful')
	else:
		form = corpReg()
	hist = addattendance.objects.all().count()
	context = {'corP':coR, 'coRz':users, 'ppa':myppa, 'cds':mycds, 'hist':hist,'form':form,'dcds':dcds}
	messages.error(request, 'Kindly Registration')
	return render(request, 'mydashi.html', context)