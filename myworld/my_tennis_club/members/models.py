from django.db import models
from datetime import date
# Create your models here.

class cds(models.Model):
	name = models.CharField(verbose_name="CDS Name", max_length=50, blank=False)
	pic = models.CharField(verbose_name="President in Charge", max_length=50, blank=False)
	pfcds = models.CharField(verbose_name="Purpose of CDS", max_length=150, blank=False)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name= "cdss"
		verbose_name_plural="cds"

class CorpRegister(models.Model):
	id = models.AutoField(primary_key=True)
	postCds  = (
		('Excos','Excos'),
		('Member','Member')
	)
	active_status = (
		('active','active'),
		('not active', 'not active')
	) 
	firstname = models.CharField(verbose_name="First Name", max_length=100, null=False, blank=False)
	lastname = models.CharField(verbose_name="Last Name", max_length=100, null=False, blank=False)
	statecode = models.CharField(verbose_name="State Code", max_length=100, null=False, blank=False)
	mystatecode = models.CharField(verbose_name="corpers Statecode",max_length=50, null=True, blank=False)
	sor = models.CharField(verbose_name="State of Origin", max_length=100, null=False, blank=False)
	statedeployed = models.CharField(verbose_name="State Deployed", max_length=100, null=False, blank=False)
	cds = models.CharField(verbose_name="CDS", max_length=100, null=False, blank=False)
	batch = models.CharField(verbose_name="Batch", max_length=100, null=False, blank=False)
	pcds = models.CharField(verbose_name="Post in CDS", max_length=100, null=False, blank=False, choices=postCds)
	ppa = models.CharField(verbose_name="PPA", max_length=100, null=False, blank=False)
	# pcds = models.CharField(verbose_name="Post in CDS", max_length=100, null=False, blank=False)
	phone = models.CharField(verbose_name="Phone Number", max_length=100, null=False, blank=False)
	profile = models.ImageField(max_length=255, null=True, blank=True, upload_to="corper_profile/")
	status_active = models.CharField(max_length=50, null=True, blank=True, choices=active_status, verbose_name="Status Remark")
	date_created = models.DateField(verbose_name = "Date Created", default=date.today)


	def __str__(self):
		return self.firstname + ' ' + self.statecode
	

class ppa(models.Model):
	myCat  = (
		('Government','Government'),
		('Private','Private'),
		('Others','Others')
	)
	name = models.CharField(verbose_name="PPA Name", max_length=100, null=False, blank=False)
	category = models.CharField(verbose_name="PPA TYPE", max_length=100, null=False, blank=False, choices = myCat)
	address = models.CharField(verbose_name="PPA Address", max_length=100, null=False, blank=False)
	# corpNO = models.CharField(verbose_name="PPA Address", max_length=100, null=False, blank=False)
	
	empNo = models.CharField(verbose_name="Employer Phone No", max_length=100, null=False, blank=False)

	def __str__(self):
		return self.name
	



class goattendance(models.Model):
	
	# # corper = models.OneToOneField(CorpRegister, on_delete=models.CASCADE)
	# statecode_id = models.ForeignKey(CorpRegister, db_column="statecode_id", on_delete=models.CASCADE)
	statecode = models.CharField(verbose_name="State Code", max_length=50, null=False, blank=False, unique=True)
	user_id = models.IntegerField(verbose_name="user id", null=False, blank=False,)
	
	year = models.IntegerField(verbose_name="Year", null=False, blank=False)
	month = models.CharField(verbose_name="Month",max_length=50, null=False, blank=False)
	day = models.IntegerField(verbose_name="Day", null=False, blank=False)
	date_created = models.DateField(verbose_name = "Date Created", default=date.today)
	status = models.IntegerField(verbose_name="Status", null=False, blank=False)

	def __str__(self):
		return self.statecode
	
	# class Meta:
	# 	managed = False
	# 	verbose_name_plural = "goattendance"
	# 	verbose_name="goattendancess"
	# 	db_table= "goattendance"


class addattendance(models.Model):
	day = models.CharField(verbose_name="Day", max_length=50, null=False, blank=False)
	month = models.CharField(verbose_name="month", max_length=50, null=False, blank=False)
	year = models.CharField(verbose_name="year", max_length=50, null=False, blank=False)
	purpose = models.CharField(verbose_name="purpose", max_length=50, null=False, blank=False)
	date_created = models.DateField(verbose_name = "Date Created", default=date.today)

	def __str__(self):
		return self.day + "/" + self.month + "/" + self.year


class Contact(models.Model):
	phone = models.CharField(verbose_name="phone", max_length=50, null=False)
	address = models.CharField(verbose_name="address", max_length=50, null=False)

	def __str__(self):
		return self.phone


class Employee(models.Model):
	active_status = (
		('active','active'),
		('not active', 'not active')
	) 
	user_id = models.IntegerField(verbose_name="user id", null=False, blank=False,)
	# statecode = models.ForeignKey(CorpRegister, on_delete=models.SET_NULL, null=True,)
	statecode =models.CharField(verbose_name="corpers Statecode",max_length=50, null=True, blank=False)
	mystatecode = models.CharField(verbose_name="corpers Statecode",max_length=50, null=True, blank=False)
	year = models.IntegerField(verbose_name="Year", null=False, blank=False)
	month = models.CharField(verbose_name="Month",max_length=50, null=False, blank=False)
	day = models.IntegerField(verbose_name="Day", null=False, blank=False)
	# purpose = models.CharField(max_length=100,verbose_name="Purpose", null=False, blank=False)
	date_created = models.DateField(verbose_name = "Date Created", default=date.today)
	status = models.IntegerField(verbose_name="Status", null=False, blank=False)
	firstname = models.CharField(max_length=100,verbose_name="Firstname", null=False, blank=False)
	lastname = models.CharField(max_length=100,verbose_name="Lastname", null=False, blank=False)
	cds = models.CharField(max_length=50, verbose_name="cds", null=False, blank=False)
	profile = models.ImageField(max_length=50, verbose_name="profile", null=False, blank=False,upload_to="corper_profile")
	status_active = models.CharField(max_length=50, null=True, blank=True, verbose_name="Status Remark")
	date_created = models.DateField(verbose_name = "Date Created", default=date.today)

    
    

	# contact = models.OneToOneField(CorpRegister, on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.mystatecode}    {self.day} {self.month}   {self.status}'


	class Meta:
		managed = True
		db_table = 'Employee'


class TakeAttendance(models.Model):
	active_status = (
		('active','active'),
		('not active', 'not active')
	) 
	user_id = models.IntegerField(verbose_name="user id", null=False, blank=False,)
	# statecode = models.ForeignKey(CorpRegister, on_delete=models.SET_NULL, null=True,)
	statecode =models.CharField(verbose_name="corpers Statecode",max_length=50, null=True, blank=False)
	mystatecode = models.CharField(verbose_name="corpers Statecode",max_length=50, null=True, blank=False)
	year = models.IntegerField(verbose_name="Year", null=False, blank=False)
	month = models.CharField(verbose_name="Month",max_length=50, null=False, blank=False)
	day = models.IntegerField(verbose_name="Day", null=False, blank=False)
	# purpose = models.CharField(max_length=100,verbose_name="Purpose", null=False, blank=False)
	date_created = models.DateField(verbose_name = "Date Created", default=date.today)
	status = models.IntegerField(verbose_name="Status", null=False, blank=False)
	firstname = models.CharField(max_length=100,verbose_name="Firstname", null=False, blank=False)
	lastname = models.CharField(max_length=100,verbose_name="Lastname", null=False, blank=False)
	cds = models.CharField(max_length=50, verbose_name="cds", null=False, blank=False)
	profile = models.ImageField(max_length=50, verbose_name="profile", null=False, blank=False,upload_to="corper_profile")
	status_active = models.CharField(max_length=50, null=True, blank=True, verbose_name="Status Remark")
	date_created = models.DateField(verbose_name = "Date Created", default=date.today)

    
    

	# contact = models.OneToOneField(CorpRegister, on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.mystatecode}    {self.day} {self.month}   {self.status}'


	


class document(models.Model):
	name = models.CharField(max_length=100,verbose_name="Document Name", null=False, blank=False)
	purpose = models.CharField(max_length=100,verbose_name="Purpose", null=False, blank=False)
	documenttype = models.ImageField(verbose_name="profile", null=False, blank=False,upload_to="documents")


	def __str__(self):
		return self.name




class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    isbn = models.CharField(max_length=13)


    def __str__(self):
    	return self.title






	



