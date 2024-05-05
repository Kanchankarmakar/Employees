from django.contrib import admin
from .models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'name', 'department', 'email', 'dob')
    search_fields = ('name', 'department', 'email')
    list_filter = ('department', 'dob')
