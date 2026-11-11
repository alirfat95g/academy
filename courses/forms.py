from django import forms
from .models import Course


class CourseForm(forms.ModelForm):
    def sections(self):
        groups = [
            ("مشخصات دوره", ("title", "category", "slug", "description", "level")),
            ("هزینه و زمان‌بندی", ("price", "capacity", "duration", "start_date", "start_time")),
            ("نمایش در سایت", ("is_active",)),
        ]
        return [(label, [self[name] for name in names]) for label, names in groups]

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
