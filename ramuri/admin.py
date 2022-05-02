from django.contrib import admin

from ramuri.models import Course

# Register your models here.

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']
    search_fields = ['name']
    # Fields you want to filter:
    # list_filter = ['name']