from django.conf.urls import url, include
from todos.views import (
    UserViewSet,
    TodolistViewSet,
    TodoViewSet
)
# from rest_framework import routers
from rest_framework_nested import routers


# \users\
# \users\{pk}
# \users\{users_pk}\todolists\
# \users\{users_pk}\todolists\{pk}
# \users\{users_pk}\todolists\{pk}\todos\
# \users\{users_pk}\todolists\{pk}\todos\{pk}


# Create a router and register our viewsets with it.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet, base_name='users')

user_router = routers.NestedSimpleRouter(router, r'users', lookup='user')
user_router.register(r'todolists', TodolistViewSet, base_name='todolists')

todolists_router = routers.NestedSimpleRouter(user_router, r'todolists', lookup='todolist')
todolists_router.register(r'todos', TodoViewSet, base_name='todos')


# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^', include(user_router.urls)),
    url(r'^', include(todolists_router.urls)),

    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
