from django.db import models
class Student(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    date = models.DateTimeField()
    _class = models.CharField(max_length=200)  # Add default value
    subject = models.CharField(max_length=200)  # Add default value
    mentor = models.CharField(max_length=200)  # Add default value

    def __str__(self):
        return self.name
    
class Mentor(models.Model):
    name = models.CharField(max_length=255)
    phone = models.PositiveIntegerField()
    college = models.CharField(max_length=255)
    date = models.DateField()
    handle = models.PositiveIntegerField()
    total = models.PositiveIntegerField()
    on = models.PositiveIntegerField()

    def __str__(self):
        return self.name
    
class Owner(models.Model):
    ownername = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)


    def __str__(self):
        return self.email

class MentorCred(models.Model):
    mentorname = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)


    def __str__(self):
        return self.email

class RenrollData(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)  # You may use a PhoneNumberField if you have a phone number validation library installed.
    email = models.EmailField(unique=True)
    date = models.DateField()
    _class = models.CharField(max_length=10)
    subject = models.CharField(max_length=10)
    mentor = models.CharField(max_length=255)
    renrollment = models.PositiveIntegerField()

    def __str__(self):
        return self.name
