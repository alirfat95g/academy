from django.shortcuts import render

# Create your views here.
from .models import Course


def course_list(request):
    # courses = Course.objects.all()
    courses = Course.objects.select_related("category").all()
    context = {"courses": courses}
    return render(request, "courses/course_list.html", context=context)
