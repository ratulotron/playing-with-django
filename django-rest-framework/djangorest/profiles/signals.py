from django.db.models.signals import pre_save
from django.dispatch import receiver

# Models
from django.contrib.auth.models import User
from tasklist.models import Tasklist, Task

@receiver(pre_save, sender=Task)
def create_tasklist(sender, instance, using, **kwargs):
    if instance.tasklist is None:
        instance.tasklist = Tasklist.objects.get(pk=1)
