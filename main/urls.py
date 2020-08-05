from django.urls import path
from .views import (
    CourseListView,
    CourseDetailView,
    CoursesListView
)
from . import views

urlpatterns = [
    path('', CourseListView.as_view(), name="main-home"),
    path('courses/', CoursesListView.as_view(), name="courses-page"),
    path('courses/<int:pk>/', CourseDetailView.as_view(), name='course-detail'),
    path('contact-us/', views.contactPage, name="contact-us"),
]