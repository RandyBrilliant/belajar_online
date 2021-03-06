# Generated by Django 2.2.14 on 2020-08-05 15:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_of_courses_completed', models.IntegerField(blank=True, null=True)),
                ('num_of_courses_enrolled', models.IntegerField(blank=True, null=True)),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=4000)),
                ('price', models.IntegerField()),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('course_image', models.ImageField(default='default_course.jpg', upload_to='course_img')),
                ('preview_video', models.URLField(max_length=500)),
                ('instructor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
