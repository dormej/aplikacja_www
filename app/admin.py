from django.contrib import admin

from app.models import Student, Person

# Register your models here.


class PersonAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'month_of_birth', 'published_date']


class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'country']


admin.site.register(Student)
admin.site.register(Person, PersonAdmin)
