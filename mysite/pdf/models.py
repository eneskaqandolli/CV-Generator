from django.db import models

# Create your models here.
class Detail(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    phone = models.CharField(max_length=250)
    about = models.TextField(max_length=550)
    degree = models.CharField(max_length=300)
    school = models.CharField(max_length=300)
    university = models.CharField(max_length=300)
    previous = models.TextField(max_length=550)
    skills = models.TextField(max_length=550)
    
    def __str__(self):
        return f"{self.name}'s CV"