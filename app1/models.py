from django.db import models

class Student(models.Model):
    gender_cho = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    )
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)  
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=gender_cho)

    def __str__(self):
        return self.name
