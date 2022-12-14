# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
import datetime

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from datetime import datetime


class Student(models.Model):
    email = models.CharField(primary_key=True, max_length=100)  # This field type is a guess.
    first_name = models.CharField(max_length=100)  # This field type is a guess.
    last_name = models.CharField(max_length=100)  # This field type is a guess.
    phone = models.CharField(max_length=9)  # This field type is a guess.

    class Meta:
        db_table = 'student'

    def __str__(self):
        return self.email


class Team(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=2)

    def __str__(self):
        return '{0} {1}'.format(self.name, self.country)


class Person(models.Model):

    class Month(models.IntegerChoices):
        January = 1
        February = 2
        March = 3
        April = 4
        May = 5
        June = 6
        July = 7
        August = 8
        September = 9
        October = 10
        November = 11
        December = 12

    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    month_of_birth = models.IntegerField(choices=Month.choices, default=datetime.now().month)
    published_date = models.DateTimeField(
        'date published',
        auto_now_add=True)
    team = models.ForeignKey(Team, blank=True, null=True, on_delete=models.SET_NULL)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return '{0} {1}'.format(self.first_name, self.last_name)

    class Meta:
        verbose_name = 'Person'
        verbose_name_plural = 'Person'
        ordering = ['last_name']


# for user in User.objects.all():
#     Token.objects.get_or_create(user=user)
#
