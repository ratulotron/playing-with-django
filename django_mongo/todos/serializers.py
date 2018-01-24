from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework.relations import HyperlinkedIdentityField
from rest_framework_nested.relations import NestedHyperlinkedRelatedField
from todos.models import Todo, Todolist


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'text', 'user')


class TodolistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todolist
        fields = ('id', 'name')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    todolists = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
     )

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'groups', 'todolists')