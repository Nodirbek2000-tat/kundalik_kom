from django.urls import path
from .views import (home_view,student_list,teacher_list,subject_list,grades_list,student_upload,
                    subject_upload,grade_upload,teacher_upload)

urlpatterns=[
    path('',home_view,name="home"),
    path('student-list/',student_list,name="student_list"),
    path('teacher-list/',teacher_list,name="teacher_list"),
    path('subjects-list/',subject_list,name="subjects_list"),
    path('grades-list/',grades_list,name="grade"),



#     ENDILIIKDA FAQAT UPLOAD QISMI UCHUN YOZAMIZ
    path('student-upload/',student_upload,name='student_upload'),
    path('subject-upload/',subject_upload,name='subject_upload'),
    path('grade-upload/',grade_upload,name='grade_upload'),
    path('teacher-upload/',teacher_upload,name='teacher_upload'),
]