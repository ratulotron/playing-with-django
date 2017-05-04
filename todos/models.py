from django.db import models
from django.contrib.auth.models import User


class Todolist(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, related_name="todolists", on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Todo(models.Model):
    todolist = models.ForeignKey(Todolist, related_name="todos", on_delete=models.CASCADE)
    text = models.CharField(max_length=500)

    def __str__(self):
        return self.text

