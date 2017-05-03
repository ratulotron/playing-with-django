from django.contrib import admin
from todos.models import Todo, TodoList


class TodoAdmin(admin.ModelAdmin):
    pass


class TodoListAdmin(admin.ModelAdmin):
    pass

admin.site.register(Todo, TodoAdmin)
admin.site.register(TodoList, TodoListAdmin)
