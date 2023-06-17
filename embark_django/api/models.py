from django.db import models
from django import forms
from django.contrib.auth.models import User


class UserInformation(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="user_information"
    )
    phone_number = models.IntegerField()
    address = models.TextField()
    age = models.PositiveSmallIntegerField()
    gender = models.CharField(
        max_length=10, choices=(("male", "male"), ("female", "female"))
    )
