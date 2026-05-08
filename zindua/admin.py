from django.contrib import admin
from .models import Instructor, Programme, Student

admin.site.register(Instructor)
admin.site.register(Programme)
admin.site.register(Student)