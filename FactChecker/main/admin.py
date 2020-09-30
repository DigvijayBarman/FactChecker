from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class NewsCSV(resources.ModelResource):
	class Meta:
		model = News
		fields = ['newsid', 'title', 'author', 'text', 'label', 'date']

class NewsAdmin(ImportExportModelAdmin):
	resource_class = NewsCSV

admin.site.register(News, NewsAdmin)