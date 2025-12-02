from django.contrib import admin
from .models import Project, Experience

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title',)


# Experience admin
@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'role', 'date', 'location')
    search_fields = ('title', 'role', 'location')
    list_filter = ('date',)