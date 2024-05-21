from django.urls import path
from . import views


urlpatterns =[   
	path('nyscledger/', views.members, name='members'),
	path('nyscledger/register/', views.register, name='register'),
	path('nyscledger/adminReg/', views.adminReg, name='adminReg'),
	path('nyscledger/dashboard/', views.dashboard, name='dashboard'),
	path('nyscledger/attendance/', views.attendance, name='attendance'),
	path('nyscledger/doattendance/', views.doattendance, name='doattendance'),
	path('nyscledger/export-to-csv/', views.export_to_csv, name='export_to_csv'),
	path('nyscledger/history-export-to-csv/', views.history_export_to_csv, name='history_export_to_csv'),
	path('nyscledger/deleteRegister/<int:id>', views.deleteRegister, name='deleteRegister'),
	path('nyscledger/deleteFile/<int:id>', views.deleteFile, name='deleteFile'),
	path('nyscledger/editregister/<int:id>', views.editregister, name='editregister'),
	path('nyscledger/submitAttendance/<int:id>', views.submitAttendance, name='submitAttendance'),
	path('nyscledger/getdone/<int:id>', views.getdone, name='getdone'),
	path('nyscledger/attendance_history/', views.attendance_history, name='attendance_history'),
	path('nyscledger/mycds/', views.mycds, name='mycds'),
	path('nyscledger/ll/', views.ll, name='ll'),
	
	path('nyscledger/documents/', views.documents, name='documents'),
	path('nyscledger/CorpRegister_list/', views.CorpRegister_list, name='CorpRegister_list'),
	path('nyscledger/CorpRegister_list/<int:id>', views.CorpRegister_details),
	path('nyscledger/import-csv/', views.import_csv, name='import_csv'),
	path('nyscledger/ppa_import_csv/', views.ppa_import_csv, name='ppa_import_csv'),
	path('nyscledger/success_page/', views.success_page, name='success_page'),
	path('nyscledger/mydashi/', views.mydashi, name='mydashi'),



]

