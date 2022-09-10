from distutils.command.upload import upload
from statistics import quantiles
from turtle import onclick
from unicodedata import name
from django.db import models
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class PhoneCode(Base):
    name = models.CharField(max_length=50, null=True, blank=True)
    code = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.name

Gender = (
    ("","------"),
    ("male","Male"),
    ("female","Female"),
    ("other","Other")
)

class UserProfile(Base):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, null=True, blank=True)
    image = models.ImageField(upload_to="profile/", null=True, blank=True)
    phone_code = models.ForeignKey(PhoneCode, on_delete=models.SET_NULL, null=True, blank=True)
    mobile = models.IntegerField(null=True, blank=True)
    gender = models.CharField(Gender, max_length=50, null=True, blank=True)
    verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.user
    
    @property
    def fname(self):
        return str(self.name).split(" ")[0]

    @property
    def lname(self):
        return str(self.name).split(" ")[-1]


class Category(Base):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Books(Base):
    unique_id = models.CharField(max_length=10, null=True, blank=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    author = models.CharField(max_length=50, null=True, blank=True)
    quantity = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def availability(self):
        available = False
        try:
            book_quantity = int(self.quantity)
            landing = Landing.objects.filter(book__id=self.id, returned=False).count()
            if landing < book_quantity:
                available = True
        except Exception as e:
            print(e)
        return available

    @property
    def landing(self):
        landing = Landing.objects.filter(book__id=self.id, returned=False).count()
        return landing

    @property
    def available(self):
        total = 0
        try:
            book_quantity = int(self.quantity)
            landing = Landing.objects.filter(book__id=self.id, returned=False).count()
            total = book_quantity - landing
        except Exception as e:
            print(e)
        return total


class Landing(Base):
    user = models.ForeignKey(UserProfile, null=True, blank=True)
    book = models.ForeignKey(Books, null=True, blank=True)
    returned = models.BooleanField(default=False)

    def __str__(self):
        return self.book
    
