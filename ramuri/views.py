from django.shortcuts import render
from django.http import HttpResponse
from .models import Course
from django.views import generic
# Importing for a class-based view

# Create your views here.

def index(request):
    courses = Course.objects.all()
    context = {
        'course_list': courses
    }
    return render(request, 'ramuri/index.html', context)

def course_list(request):
    course = Course.objects.get(pk=1)
    template = "<html>" \
        "<body>The first course: `%s. `" \
        "</body>" \
        "</html>" % course.name
    return HttpResponse(content=template)


# Example of function view with logic

def course_function_view(request):
    if request.method == 'GET':
        course = Course.objects.get(pk=1)
        template = "<html>" \
            "<body>The first course: `%s. `" \
            "</body>" \
            "</html>" % course.name
        return HttpResponse(content=template)
    else:
        return HttpResponse(content="Request processed")
    
# Generic class based views - built-in views by Django

class CourseViewAsGeneric(generic.DetailView):
    model = Course
    template_name = 'ramuri/course-detail.html' # Provided template path