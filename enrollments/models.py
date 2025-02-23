from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Student(models.Model):  # Changed from EnrolledStudent to Student
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    courses = models.ManyToManyField(Course, related_name="students")  # ✅ Many-to-Many relationship


    def __str__(self):
        return self.name
