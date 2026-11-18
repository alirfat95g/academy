from django import forms
from .models import Course


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = [
            "title",
            "category",
            "slug",
            "description",
            "level",
            "price",
            "capacity",
            "duration",
            "start_date",
            "start_time",
            "is_active",
        ]
