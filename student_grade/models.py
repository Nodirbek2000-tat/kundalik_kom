from django.db import models


class Student(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    class_name=models.CharField(max_length=100)
    birth_date=models.DateField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name}  {self.last_name}"


class Teacher(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name}  {self.last_name}"


class Subject(models.Model):
    name=models.CharField(max_length=100)
    teacher=models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.teacher}"


class StudentGrade(models.Model):
    name=models.ForeignKey(Student, on_delete=models.SET_NULL, null=True)
    subject=models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True)
    rate=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.subject} - {self.rate}"
