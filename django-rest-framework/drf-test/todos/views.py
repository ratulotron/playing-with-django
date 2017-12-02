from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework.response import Response
from rest_framework import viewsets
from todos.models import Todolist, Todo
from todos.serializers import UserSerializer, TodoSerializer, TodolistSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

    # def list(self, request,):
    #     queryset = User.objects.filter()
    #     serializer = UserSerializer(queryset, many=True, context={'request': request})
    #     return Response(serializer.data)
    #
    # def retrieve(self, request, pk=None):
    #     queryset = User.objects.filter()
    #     user = get_object_or_404(queryset, pk=pk)
    #     serializer = UserSerializer(user, context={'request': request})
    #     return Response(serializer.data)


class TodolistViewSet(viewsets.ViewSet):
    queryset = Todolist.objects.all()
    serializer_class = TodolistSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def list(self, request, user_pk=None):
        queryset = Todolist.objects.filter(user=user_pk)
        serializer = TodolistSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None, user_pk=None):
        queryset = Todolist.objects.filter(pk=pk, user=user_pk)
        todolist = get_object_or_404(queryset, pk=pk)
        serializer = TodolistSerializer(todolist)
        return Response(serializer.data)


class TodoViewSet(viewsets.ViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def list(self, request, user_pk=None, todolist_pk=None):
        queryset = Todo.objects.filter(todolist__user=user_pk, todolist=todolist_pk)
        serializer = TodoSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, user_pk=None, todolist_pk=None):
        queryset = Todo.objects.filter(pk=pk, todolist=todolist_pk, todolist__user=user_pk)
        todo = self.queryset.get(pk=pk)
        serializer = TodoSerializer(todo)
        return Response(serializer.data)



