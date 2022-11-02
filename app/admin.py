from django.contrib import admin
from django.db.models.functions import Lower

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
    list_display = ['first_name', 'last_name', 'month_of_birth', 'team', 'published_date']
    list_filter = ['team', 'published_date']
    fieldsets = [
        ('Personal Information', {'fields': ['first_name', 'last_name', 'month_of_birth']}),
        ('Team', {'fields': ['team']}),
        ('', {'fields': ['published_date']})
    ]
    readonly_fields = ['published_date']
    search_fields = ['last_name']

    @admin.display
    def get_full_team(self, obj):
        if obj.team is not None:
            return f"{obj.team.name} ({obj.team.country})"
        return "---"


admin.site.register(Person, PersonAdmin)
admin.site.register(Team, TeamAdmin)
