from django.contrib import admin
from system.models import *

class applicationsAdmin(admin.ModelAdmin):

	list_display = ("applicantName","caseType", "description","status","photoShootingDate")
	search_fields = ['applicantName']


admin.site.register(application,applicationsAdmin)
admin.site.register(caseType)
admin.site.register(caseStatus)

# Register your models here.
