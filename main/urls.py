from django.urls import path
from .views import (
    CourseListView,
    CourseDetailView,
    CoursesListView,
    CourseCreateView
)
from . import views

urlpatterns = [
    path('', CourseListView.as_view(), name="main-home"),
    path('courses/', CoursesListView.as_view(), name="courses-page"),
    path('courses/<int:pk>/', CourseDetailView.as_view(), name='course-detail'),
    path('courses/new/', CourseCreateView.as_view(), name='course-create'),
    path('courses/new/created', views.createdCoursePage, name='course-created-for-you'),
    path('contact-us/', views.contactPage, name="contact-us"),
]