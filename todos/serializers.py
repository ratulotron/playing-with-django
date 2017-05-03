from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.relations import HyperlinkedIdentityField
from rest_framework_nested.relations import NestedHyperlinkedRelatedField
from todos.models import Todo, TodoList


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'text')


class TodoListSerializer(serializers.ModelSerializer):
    todos = TodoSerializer(many=True)
    class Meta:
        model = TodoList
        fields = ('id', 'name', 'todos')



class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups') # , 'lists')

    # lists = NestedHyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,   # Or add a queryset
    #     view_name='user-detail',
    #     lookup_url_kwarg={'user_pk': 'user_pk'}
    # )


