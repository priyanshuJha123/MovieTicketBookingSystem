from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    contact=models.CharField(max_length=10,null=True)
    address=models.CharField(max_length=100,null=True)
    like=models.CharField(max_length=100,null=True)
    gen=models.CharField(max_length=100,null=True)
    dob=models.DateField(max_length=100,null=True)
    image = models.FileField(null=True)
    def __str__(self):
        return self.user.username

class Certificate(models.Model):
    name=models.CharField(max_length=10,null=True)
    description=models.TextField(null=True)

    def __str__(self):
        return self.name

class Movie_Type(models.Model):
    name=models.CharField(max_length=10,null=True)
    description=models.TextField(null=True)

    def __str__(self):
        return self.name

class Language(models.Model):
    name=models.CharField(max_length=10,null=True)
    description=models.TextField(null=True)

    def __str__(self):
        return self.name

class Movie(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE, null=True)
    type = models.ForeignKey(Movie_Type, on_delete=models.CASCADE, null=True)
    certificate = models.ForeignKey(Certificate, on_delete=models.CASCADE, null=True)
    name=models.CharField(max_length=100,null=True)
    duration = models.CharField(max_length=100,null=True)
    director = models.CharField(max_length=100,null=True)
    casting = models.CharField(max_length=100,null=True)
    release_date = models.DateField(null=True)
    trailer=models.TextField(null=True)
    description=models.TextField(null=True)
    image=models.FileField(null=True)

    def __str__(self):
        return self.name

class Movie_Time(models.Model):
    time1 =  models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.time1

class Set_Timing(models.Model):
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE,null=True)
    date1 = models.CharField(max_length=100,null=True)
    time1 = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.movie.name+" "+self.date11+" "+self.time1

class Booking(models.Model):
    set_time = models.ForeignKey(Set_Timing, on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=100, null=True)
    user = models.CharField(max_length=100, null=True)
    user1 = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    time = models.DateTimeField(null=True)
    seat = models.CharField(max_length=100,null=True)
    price = models.CharField(max_length=100,null=True)
    ticket = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.set_time.movie.name+" "+self.user