from .models import StudentGrade,Student,Subject,Teacher
from django import forms


class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=['first_name','last_name','address','class_name','birth_date']


class SubjectForm(forms.ModelForm):
    class Meta:
        model=Subject
        fields=['name','teacher']


class GradeForm(forms.ModelForm):
    class Meta:
        model=StudentGrade
        fields=['name','subject','rate']


class TeacherForm(forms.ModelForm):
    class Meta:
        model=Teacher
        fields=['first_name','last_name']