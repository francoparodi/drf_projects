from django.contrib import admin

# Register your models here.
from .models import Solution, ProcessLog

admin.site.register(Solution)
admin.site.register(ProcessLog)
