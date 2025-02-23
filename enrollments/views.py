from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.urls import reverse_lazy
from .models import Course, Student
from .forms import EnrollmentForm

class CourseListView(ListView):
    model = Course
    template_name = 'enrollments/course_list.html'
    context_object_name = 'courses'
    
class StudentListView(ListView):
    model = Student
    template_name = 'enrolled_students.html'  # This needs to be created
    context_object_name = 'students'

def enroll_student(request):
    if request.method == "POST":
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.save()  # ✅ Save student first
            form.save_m2m()  # ✅ Save the many-to-many relationship
            return redirect(reverse_lazy("enrollment_success"))  # ✅ Redirect after success
    else:
        form = EnrollmentForm()
    
    return render(request, "enroll.html", {"form": form})

def enrollment_success(request):
    return render(request, 'enrollments/success.html')


