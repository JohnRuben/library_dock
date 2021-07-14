from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    CATEGORY = (
        ('arts', 'Arts'),
        ('biography', 'Biography'),
        ('environment', 'Environment'),
        ('documentary', 'Documentary'),
        ('math', 'Math'),
        ('science', 'Science')
    )
    name = models.CharField(max_length=255, null=True)
    category = models.CharField(max_length=255, choices=CATEGORY, null=True)
    price = models.FloatField(null=True, blank=True, default='')
    qty = models.IntegerField(null=True, blank=True, default='')

    def __str__(self):
        return self.name


class Member(models.Model):
    GENDER = (
        ('male', 'Male'),
        ('female', 'Female')
    )
    teacher = models.BooleanField(default=False)
    student = models.BooleanField(default=False)
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True)
    gender = models.CharField(max_length=255, null=True, choices=GENDER)
    address = models.TextField(null=True)
    city = models.CharField(max_length=255, null=True)
    state = models.CharField(max_length=255, null=True)
    country = models.CharField(max_length=255, null=True)
    zip = models.IntegerField(null=True)
    email_id = models.EmailField(max_length=255, null=True, default='')
    profile_pic = models.ImageField(default="profile1.png", blank=True, null=True)
    phone = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name


class Lease(models.Model):
    STATUS = (
        ('issued', 'Issued'),
        ('returned', 'Returned')
    )
    # student = models.ForeignKey(Student, null=True, on_delete=models.SET_NULL, blank=True, default='')
    # teacher = models.ForeignKey(Teacher, null=True, on_delete=models.SET_NULL, blank=True, default='')
    member = models.ForeignKey(Member, null=True, on_delete=models.SET_NULL, blank=True, default='')
    book = models.ForeignKey(Book, null=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=255, null=False, choices=STATUS)
    lease_date = models.DateField(null=True)

    def __str__(self):
        return self.book.name




