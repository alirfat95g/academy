from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_http_methods, require_safe

from .forms import CourseForm
from .models import Course


def visible_courses(user):
    courses = Course.objects.select_related("category")
    if user.is_staff:
        return courses
    return courses.filter(is_active=True)


@require_safe
def course_list(request):
    courses = visible_courses(request.user)
    return render(request, "courses/course_list.html", {"courses": courses})


@require_safe
def course_detail(request, pk):
    course = get_object_or_404(visible_courses(request.user), pk=pk)
    return render(request, "courses/course_detail.html", {"course": course})


@staff_member_required
@require_http_methods(["GET", "POST"])
def course_create(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save()
            return redirect("course_detail", pk=course.pk)
    else:
        form = CourseForm()
    return render(
        request,
        "courses/course_form.html",
        {"form": form, "heading": "ثبت دوره"},
    )
