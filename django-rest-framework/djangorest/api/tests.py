from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase
from tasklist.models import Tasklist


class ModelTestCase(TestCase):
    """This class defines the test suite for the tasklist model."""

    def setUp(self):
        """Define the test client and other test variables."""
        user = User.objects.create(username="nerd")
        self.bucketlist_name = "Write world class code"
        self.bucketlist = Tasklist(name=self.bucketlist_name, owner=user)

    def test_model_can_create_a_bucketlist(self):
        """Test the tasklist model can create a tasklist"""
        old_count = Tasklist.objects.count()
        self.bucketlist.save()
        new_count = Tasklist.objects.count()
        self.assertNotEqual(old_count, new_count)


class ViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        user = User.objects.create(username="nerd")

        # Initialize client and force it to use authentication
        self.client = APIClient()
        self.client.force_authenticate(user=user)

        # Since usermodel instance is not serialized, it uses ID/Pk
        self.bucketlist_data = {'name': 'Go to Ibiza', 'owner': user.id}
        self.response = self.client.post(
            reverse('create'),
            self.bucketlist_data,
            format="json")

    def test_api_can_create_a_bucketlist(self):
        """Test the api has bucket creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_authorization_is_enforced(self):
        """Test that the api has user authorization."""
        new_client = APIClient()    # Different from client initialized before testing
        res = new_client.get(
            reverse('details', kwargs={'pk': 3}), 
            format="json"
            )
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


    def test_api_can_get_a_bucketlist(self):
        """Test the api can get a given tasklist."""
        bucketlist = Tasklist.objects.get(id=1)
        response = self.client.get(
            reverse('details', kwargs={'pk': bucketlist.id}),
            format="json"
            )

        # Test that response is OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Test that the response contains something called tasklist
        self.assertContains(response, bucketlist)

    def test_api_can_update_bucketlist(self):
        """Test the api can update a given tasklist."""
        bucketlist = Tasklist.objects.get(id=1)
        change_bucketlist = {'name': 'Something new'}
        response = self.client.put(
            reverse('details', kwargs={'pk': bucketlist.id}),
            change_bucketlist, format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_can_delete_bucketlist(self):
        """Test the api can delete a tasklist."""
        bucketlist = Tasklist.objects.get(id=1)
        response = self.client.delete(
            reverse('details', kwargs={'pk': bucketlist.id}),
            format='json',
            follow=True
            )
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
