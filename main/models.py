from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class course(models.Model):
    title           = models.CharField(max_length=200)
    description     = models.TextField(max_length=4000)
    price           = models.IntegerField()
    date_posted     = models.DateTimeField(default=timezone.now)
    instructor      = models.ForeignKey(User, on_delete=models.CASCADE)
    course_image    = models.ImageField(default="default.jpg", upload_to="course_img")

