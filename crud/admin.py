from django.contrib import admin
from crud.models import Tasks


@admin.register(Tasks)
class TasksAdmin(admin.ModelAdmin):
  list_display = ('title', 'description', 'status', 'due_date')
