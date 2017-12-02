from django.db import models
from django.contrib.auth.models import User


class Tasklist(models.Model):
    """A list of tasks."""
    name = models.CharField(max_length=255, blank=False, unique=True)
    owner = models.ForeignKey(User,
                              related_name='tasklist',
                              on_delete=models.CASCADE)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)


class Task(models.Model):
    """A single task."""
    description = models.CharField(max_length=255, blank=False)
    deadline = models.DateTimeField(auto_now_add=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    tasklist = models.ForeignKey(Tasklist,
                                 related_name='tasklist',
                                 on_delete=models.CASCADE,
                                 null=True)

    # Task.object.save()

    def __str__(self):
        """Return the description of the task."""
        return "{}".format(self.description)