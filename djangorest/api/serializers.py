from rest_framework import serializers
from tasklist.models import Tasklist, Task

class TasklistSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Tasklist
        fields = ('id', 'name', 'owner')
        read_only_fields = ('date_created', 'date_modified')


class TaskSerializer(serializers.ModelSerializer):
    """Serializer to map the Tasks into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Task
        fields = ('id', 'description', 'deadline', 'date_created', 'date_modified', 'tasklist')
        read_only_fields = ('date_created', 'date_modified')