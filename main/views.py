from django.shortcuts import render
from .models import Course
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView
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

class CourseCreateView(LoginRequiredMixin, CreateView):
    model = Course
    fields = ['title', 'description', 'price', 'course_image', 'preview_video']

    def form_valid(self, form):
        form.instance.instructor = self.request.user
        return super().form_valid(form)

def contactPage(request):
    return render(request, "main/contact-us.html",{})

def createdCoursePage(request):
    return render(request, "main/course-created.html",{})