from django.db import models

# Create your models here.
# students_app/models.py
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    grade = models.PositiveIntegerField()
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
