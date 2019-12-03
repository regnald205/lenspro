from django.contrib import admin
from .models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display=('employee_name','living','Hire_date')

admin.site.register(Employee,EmployeeAdmin)   
