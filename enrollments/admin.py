from django.contrib import admin
from .models import Course, Student  # ✅ Use 'Student' instead

admin.site.register(Course)
admin.site.register(Student)
