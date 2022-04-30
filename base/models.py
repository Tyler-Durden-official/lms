from django.db import models
from django.contrib.auth.models import User
from datetime import datetime,timedelta

from matplotlib.style import available


class Book(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    book_id = models.PositiveIntegerField()
    category = models.CharField(max_length=50)
    availability = models.IntegerField(default=0)

    def __str__(self):
        return str(self.name) + ' [' + str(self.book_id) + ']'

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # name = models.CharField(max_length=30)
    branch = models.CharField(max_length=10)
    roll_no = models.CharField(max_length=3, blank=True)
    phone = models.CharField(max_length=10, blank=True)
    image = models.ImageField(upload_to="", blank=True)

    def __str__(self):
        return str(self.user) + " ["+str(self.branch)+']' +  " ["+str(self.roll_no)+']'


def expiry():
    return datetime.today() + timedelta(days=14)

class IssuedBook(models.Model):
    student_id = models.CharField(max_length=100, blank=True) 
    book_id = models.CharField(max_length=13)
    issued_date = models.DateField(auto_now=True)
    expiry_date = models.DateField(default=expiry)
