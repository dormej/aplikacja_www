from django.contrib import admin
from django.db.models.functions import Lower
from rest_framework.authtoken.admin import TokenAdmin

from app.models import Person, Team


# Register your models here.
class PersonInline(admin.TabularInline):
    model = Person
    extra = 2


class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'country']
    list_filter = ['country']
    inlines = [PersonInline]


class PersonAdmin(admin.ModelAdmin):
    list_display = ['owner', 'first_name', 'last_name', 'month_of_birth', 'team', 'published_date']
    list_filter = ['team', 'published_date']
    fieldsets = [
        ('Personal Information', {'fields': ['first_name', 'last_name', 'month_of_birth']}),
        ('Team', {'fields': ['team']}),
        ('Owner', {'fields': ['owner']}),
        ('', {'fields': ['published_date']})
    ]
    readonly_fields = ['published_date']
    search_fields = ['last_name']

    @admin.display
    def get_full_team(self, obj):
        if obj.team is not None:
            return f"{obj.team.name} ({obj.team.country})"
        return "---"


TokenAdmin.raw_id_fields = ['user']

admin.site.register(Person, PersonAdmin)
admin.site.register(Team, TeamAdmin)
