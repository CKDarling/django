from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=264)
    last_name = models.CharField(max_length=264)
    email = models.EmailField(max_length=70, null=True, blank=True, unique=True)

    def __str__ (self):
        return self.first_name
