from django.contrib import admin
from .models import Company, Language, Employee

# Register your models here.
admin.site.register(Company)
admin.site.register(Language)
admin.site.register(Employee)