from django.contrib import admin
from .models import StudentGrade,Student,Subject,Teacher

admin.site.register(Subject)
admin.site.register(Student)
admin.site.register(StudentGrade)
admin.site.register(Teacher)
