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
    grade = models.CharField(max_length=5)  # e.g., "A", "B+", "C-", "Fail"


    def __str__(self):
        return f"{self.first_name} {self.last_name}"
        
class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    staff_id = models.CharField(max_length=20, unique=True)
    subject = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"




