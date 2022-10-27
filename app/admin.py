from django.contrib import admin
from django.db.models.functions import Lower

from app.models import Student, Person, Team


# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'country']
    list_filter = ['country']


class PersonAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'team', 'month_of_birth', 'published_date']
    list_filter = ['team', 'published_date']

    @admin.display
    def get_full_team(self, obj):
        if obj.team is not None:
            return f"{obj.team.name} ({obj.team.country})"
        return "---"


# admin.site.register(Student)
admin.site.register(Person, PersonAdmin)
admin.site.register(Team, TeamAdmin)

