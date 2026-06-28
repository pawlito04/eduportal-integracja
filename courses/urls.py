from django.urls import path
from . import views

app_name = "courses"

urlpatterns = [
    path("", views.course_list, name="course_list"),
    path("my-courses/", views.my_courses, name="my_courses"),
    path("course/<int:pk>/", views.course_detail, name="course_detail"),
    path("course/<int:pk>/enroll/", views.enroll_course, name="enroll_course"),
    path("course/<int:pk>/continue/", views.continue_course, name="continue_course"),
    path("course/<int:pk>/certificate/", views.course_certificate, name="course_certificate"),
    path("lesson/<int:pk>/", views.lesson_detail, name="lesson_detail"),
    path("lesson/<int:pk>/complete/", views.complete_lesson, name="complete_lesson"),
]