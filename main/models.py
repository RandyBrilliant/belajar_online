from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image

# Create your models here.
class Student(models.Model):
    student                     = models.OneToOneField(User, on_delete=models.CASCADE)
    num_of_courses_completed    = models.IntegerField(null=True, blank=True)
    num_of_courses_enrolled     = models.IntegerField(null=True, blank=True)

class Course(models.Model):
    title           = models.CharField(max_length=200)
    description     = models.TextField(max_length=4000)
    price           = models.IntegerField()
    date_posted     = models.DateTimeField(default=timezone.now)
    instructor      = models.ForeignKey(User, on_delete=models.CASCADE)
    course_image    = models.ImageField(default="default_course.jpg", upload_to="course_img")
    preview_video   = models.URLField(max_length=500)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.course_image.path)

        if img.height > 578 or img.width > 324:
            output_size = (578, 324)
            img.thumbnail(output_size)
            img.save(self.course_image.path)

    def get_absolute_url(self):
        return reverse('course-created-for-you')



    @property
    def imageURL(self):
        try:
            url = self.course_image.url
        except:
            url = ''
        return url
