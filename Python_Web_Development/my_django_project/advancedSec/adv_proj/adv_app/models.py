from django.db import models
from django.urls import reverse

# Create your models here.
class School(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=264,unique=True)
    principal = models.CharField(max_length=264)
    location = models.CharField(max_length=264)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('adv_app:detail',kwargs={'pk':self.pk})

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=264)
    age = models.PositiveIntegerField()
    school = models.ForeignKey(School,related_name='students',on_delete=models.PROTECT)

    def __str__(self):
        return self.name
