from django.contrib import admin
from . import models
# Register your models here.

class IncidentAdmin(admin.ModelAdmin):
    list_display =['reportedby', 'date', 'internalseverity']



admin.site.register(models.ReportingModel, IncidentAdmin)
