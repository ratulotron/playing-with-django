from rest_framework import generics, permissions, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from tasklist.models import Tasklist, Task
from .serializers import TasklistSerializer, TaskSerializer
from .permissions import IsOwner


class TaskViewSet(viewsets.ViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def list(self, request, tasklist_pk=None):
        tasks = self.queryset.filter(tasklist=tasklist_pk)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Task.objects.all()
        task = get_object_or_404(queryset, pk=pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data)


class TasklistViewSet(viewsets.ViewSet):
    """
    This class defines the create behavior of our rest api.
    
    get:
    Return a list of all the existing entries.
    
    post:
    Creates a new entry in tasklist.
    """
    queryset = Tasklist.objects.all()
    serializer_class = TasklistSerializer
    permission_classes = (
        permissions.IsAuthenticated,
        IsOwner
        )

    def perform_create(self, serializer):
        """Save the post data when creating a new tasklist."""
        serializer.save(owner=self.request.user)


# class TasklistDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Tasklist.objects.all()
#     serializer_class = TasklistSerializer
#     permission_classes = (
#         permissions.IsAuthenticated,
#         IsOwner
#         )
#
#     # def perform_create(self, serializer):
#     #     """Save the post data when creating a new tasklist."""
#     #     serializer.save(owner=self.request.user)
#
#
# class TaskListView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer
#     permission_classes = (
#         permissions.IsAuthenticated,
#         IsOwner
#         )
#
#     def perform_create(self, serializer):
#         """Save the post data when creating a new tasklist."""
#         serializer.save(owner=self.request.user)


# class EntryDetailsView(generics.RetrieveUpdateDestroyAPIView):
#     """This class handles the http GET, PUT and DELETE requests.
#
#     get:
#     Fetches the details of a single entry in the bucket list.
#
#     put:
#     Updates a single entry with the data suplied.
#
#     delete:
#     Deletes a single entry
#     """
#
#     queryset = Tasklist.objects.all()
#     serializer_class = TasklistSerializer
#     permission_classes = (
#         permissions.IsAuthenticated,
#         IsOwner)
