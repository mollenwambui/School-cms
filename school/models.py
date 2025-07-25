from django.db import models

# Create your models here.
#unique=True means no two students can have the same admission number.
#DateField stores only the date (no time).
#auto_now_add=True means Django will automatically set the date when the record is first created.
#The __str__ method defines what should be shown when you print the object or view it in the Django admin.



from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    admission_number = models.CharField(max_length=20, unique=True)
    date_of_birth = models.DateField()
    enrolled_date = models.DateField(auto_now_add=True)
    stream = models.CharField(max_length=50)  # e.g., "1 Red", "2 Blue"
    level = models.CharField(max_length=10, default="C")  # e.g., "A", "B+", "C-", "Fail"


    def __str__(self):
        return f"{self.first_name} {self.last_name}"
        
class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    staff_id = models.CharField(max_length=20, unique=True)
    subject = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    



# from .models import Classroom

class Subject(models.Model):

    subject_name = models.CharField(max_length=100)
    subject_code = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.subject_name} ({self.subject_code})"


class Classroom(models.Model):
    name = models.CharField(max_length=50)
    teacher = models.ForeignKey('Teacher', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name
    


class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    score = models.IntegerField()
    date_recorded = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.score

from django.utils import timezone

class StudentAttendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    present = models.BooleanField(default=True)

    class Meta:
        unique_together = ('student', 'date')

    def __str__(self):
        return f"{self.student.first_name} {self.student.last_name} - {self.date} - {'Present' if self.present else 'Absent'}"


class TeacherAttendance(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    present = models.BooleanField(default=True)

    class Meta:
        unique_together = ('teacher', 'date')

    def __str__(self):
        return f"{self.teacher.first_name} {self.teacher.last_name} - {self.date} - {'Present' if self.present else 'Absent'}"
