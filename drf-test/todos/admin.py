from django.contrib import admin
from todos.models import Todo, Todolist


class TodoAdmin(admin.ModelAdmin):
    pass


class TodolistAdmin(admin.ModelAdmin):
    pass

admin.site.register(Todo, TodoAdmin)
admin.site.register(Todolist, TodolistAdmin)
