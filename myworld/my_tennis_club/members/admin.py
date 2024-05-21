from django.contrib import admin
from .models import *


def get_search_fields(self, request):
    search_fields = super().get_search_fields(request)
        # Customize the search fields here
    return search_fields
# Register your models here.
admin.site.register(CorpRegister)
admin.site.register(ppa)
admin.site.register(cds)
admin.site.register(goattendance)
admin.site.register(addattendance)
admin.site.register(Contact)
admin.site.register(TakeAttendance)
admin.site.register(document)
admin.site.register(Book)
