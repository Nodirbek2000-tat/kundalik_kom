from django.shortcuts import render,redirect
from .models import Student,Teacher,Subject,StudentGrade
from .forms import StudentForm,SubjectForm,TeacherForm,GradeForm




def home_view(request):
    return render(request,'home.html')

def student_list(request):
    students=Student.objects.all()
    context={
        "students" : students
    }
    return render(request,"student_list.html",context)



def teacher_list(request):
    teachers=Teacher.objects.all()
    context={
        "teachers" : teachers
    }
    return render(request,"teacher_list.html",context)


def subject_list(request):
    subjects=Subject.objects.all()
    context={
        "subjects" : subjects
    }
    return render(request,"subjects_list.html",context)


def grades_list(request):
    grades=StudentGrade.objects.all()
    context={
        "grades" : grades
    }
    return render(request,"grades_list.html",context)


# Barcha malumotlarning har biriga yuklash qismi


def student_upload(request):
    if request.method == 'POST':
        form=StudentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('student_list') #malumotlar saqlangndan keyin bosh saxifaga redirect qilish
    else:
            form = StudentForm()
    context={'form':form}
    return render(request,"student_upload.html",context)


def subject_upload(request):
    if request.method == 'POST':
        form=SubjectForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('subjects_list') #malumotlar saqlangndan keyin bosh saxifaga redirect qilish
    else:
            form = SubjectForm()
    context={'forms':form}
    return render(request,"subject_upload.html",context)


def grade_upload(request):
    if request.method == 'POST':
        form=GradeForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('grade') #malumotlar saqlangndan keyin bosh saxifaga redirect qilish
    else:
            form = GradeForm()
    context={'formss':form}
    return render(request,"grade_upload.html",context)


def teacher_upload(request):
    if request.method == 'POST':
        form=TeacherForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('teacher_list') #malumotlar saqlangndan keyin bosh saxifaga redirect qilish
    else:
            form = TeacherForm()
    context={'formsss':form}
    return render(request,"teacher_upload.html",context)