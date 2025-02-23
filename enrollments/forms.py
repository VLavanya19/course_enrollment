from django import forms
from .models import Student, Course

class EnrollmentForm(forms.ModelForm):
    courses = forms.ModelMultipleChoiceField(
        queryset=Course.objects.all(),
        widget=forms.CheckboxSelectMultiple,  # ✅ Allows multiple course selection
    )

    class Meta:
        model = Student
        fields = ['name', 'email', 'courses']  # ✅ 'course' must be included
