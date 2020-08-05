from django.shortcuts import render
from .models import Course
from django.views.generic import (
    ListView,
    DetailView
)

# Create your views here.
class CourseListView(ListView):
    model = Course
    template_name = 'main/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'courses'
    ordering = ['-date_posted']

class CourseDetailView(DetailView):
    model = Course

# def home(request):
#     courses = Course.objects.all()
#     context = {'courses': courses}
#     return render(request, "main/home.html", context)

class CoursesListView(ListView):
    model = Course
    template_name = 'main/courses.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'courses'
    ordering = ['-date_posted']

def contactPage(request):
    return render(request, "main/contact-us.html",{})
