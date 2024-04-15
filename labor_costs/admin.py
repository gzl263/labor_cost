from django.contrib import admin

# Register your models here.
from .models import Employee, CostData_Year, CostData

admin.site.register(Employee)
admin.site.register(CostData_Year)
admin.site.register(CostData)
