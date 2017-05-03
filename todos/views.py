from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import viewsets
from todos.models import TodoList, Todo
from todos.serializers import UserSerializer, TodoSerializer, TodoListSerializer
from rest_framework_extensions.mixins import NestedViewSetMixin



class UserViewSet(viewsets.ModelViewSet):
    # queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request,):
        queryset = User.objects.filter()
        serializer = UserSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = User.objects.filter()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user, context={'request': request})


class TodoListViewSet(viewsets.ViewSet):
    # queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def list(self, request, user_pk=None):
        queryset = TodoList.objects.filter(user=user_pk)
        serializer = TodoListSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, user_pk=None):
        queryset = TodoList.objects.filter(pk=pk, user=user_pk)
        todo_list = get_object_or_404(queryset, pk=pk)
        serializer = TodoListSerializer(todo_list)
        return Response(serializer.data)


class TodoViewSet(viewsets.ViewSet):
    # queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def list(self, request, user_pk=None, todo_list_pk=None):
        queryset = Todo.objects.filter(todo_list__user=user_pk, todo_list=todo_list_pk)
        serializer = TodoSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, user_pk=None, todo_list_pk=None):
        queryset = Todo.objects.filter(pk=pk, todo_list=todo_list_pk, todo_list__user=user_pk)
        todo = self.queryset.get(pk=pk)
        serializer = TodoSerializer(todo)
        return Response(serializer.data)



