# from rest_framework import viewsets, response
from rest_framework_mongoengine import viewsets

from .models import Tool
from .serializers import ToolSerializer


class ToolViewSet(viewsets.ModelViewSet):
    '''
    Contains information about inputs/outputs of a single program
    that may be used in Universe workflows.
    '''
    lookup_field = 'id'
    serializer_class = ToolSerializer

    def get_queryset(self):
        return Tool.objects.all()


# class ToolViewSet(viewsets.ModelViewSet):
#     '''
#     Contains information about a command-line Unix program.
#     '''
#     queryset = Tool.objects.all()
#     lookup_field = 'id'
#     serializer_class = ToolSerializer
#
#     def destroy(self, request, *args, **kwargs):
#         instance = self.get_object()
#         self.get_serializer().destroy(instance)
#         print("Instance destroyed!")
#         return response.Response(status=status.HTTP_204_NO_CONTENT)
