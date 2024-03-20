from django.db import models
from students.models import Student
from lectures.models import Lecture

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)
    exam_score = models.PositiveIntegerField()
    enrollment_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.student.name} - {self.lecture.name}"

# Create your models here.
