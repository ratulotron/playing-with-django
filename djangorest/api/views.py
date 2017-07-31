from rest_framework import generics, permissions

from bucketlist.models import Bucketlist
from .permissions import IsOwner
from .serializers import BucketlistSerializer


class CreateEntryView(generics.ListCreateAPIView):
    """
    This class defines the create behavior of our rest api.
    
    get:
    Return a list of all the existing entries.
    
    post:
    Creates a new entry in bucketlist.
    """
    permission_classes = (
        permissions.IsAuthenticated, 
        IsOwner
        )

    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save(owner=self.request.user)


class EntryDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests.
    
    get:
    Fetches the details of a single entry in the bucket list.

    put:
    Updates a single entry with the data suplied.

    delete:
    Deletes a single entry
    """

    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer
    permission_classes = (
        permissions.IsAuthenticated,
        IsOwner)
