# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Student(models.Model):
    email = models.CharField(primary_key=True, max_length=100)  # This field type is a guess.
    first_name = models.CharField(max_length=100)  # This field type is a guess.
    last_name = models.CharField(max_length=100)  # This field type is a guess.
    phone = models.CharField(max_length=9)  # This field type is a guess.

    class Meta:
        db_table = 'student'

    def __str__(self):
        return self.email
