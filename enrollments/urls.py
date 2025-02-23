from django.urls import path
from .views import CourseListView, StudentListView, enroll_student, enrollment_success

urlpatterns = [
    path('courses/', CourseListView.as_view(), name='course_list'),
    path('students/', StudentListView.as_view(), name='enrolled_students'),
    path('enroll/', enroll_student, name='enroll'),
    path('success/', enrollment_success, name='enrollment_success'),
]
