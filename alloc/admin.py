from django.contrib import admin
from django.contrib.auth.models import Group
from import_export.admin import ImportExportModelAdmin

# Register your models here.
from .models import Patient

# class ProjectAdmin(admin.ModelAdmin):
class PatientAdmin(ImportExportModelAdmin):
    list_display = ('id','manager', 'patient_id', 'name', 'email', 'doctor', 'date')
    list_per_page = 5
    search_fields = ('manager', 'patient_id', 'name', 'email', 'doctor', 'date')
    list_filter = ('manager', 'patient_id', 'name', 'email', 'doctor','date')
    
admin.site.register(Patient, PatientAdmin)
# admin.site.unregister(Group)
