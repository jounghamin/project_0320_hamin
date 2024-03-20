from django.db import models
from instructors.models import Instructor


class Lecture(models.Model):
    name = models.CharField(max_length=100)
    content_num = models.IntegerField
    instructor= models.ForeignKey(Instructor, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name