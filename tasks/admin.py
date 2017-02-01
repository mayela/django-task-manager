from mptt.admin import MPTTModelAdmin

from django.contrib import admin

from tasks.models import Task

@admin.register(Task)
class TaskAdmin(MPTTModelAdmin):
    list_display = ('id', 'subject', 'agent', 'status')
    fields = ('id', 'agent', 'subject', 'description', 'status', 'parent')

