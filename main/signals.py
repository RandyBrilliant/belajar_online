from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Student

@receiver(post_save, sender=User)
def create_student(sender, instance, created, **kwargs):
    if created:
        Student.objects.create(student=instance)

@receiver(post_save, sender=User)
def save_student(sender, instance, **kwargs):
    instance.student.save()