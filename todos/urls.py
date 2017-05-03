from django.conf.urls import url, include
from todos.views import (
    UserViewSet,
    TodoListViewSet,
    TodoViewSet
)
from rest_framework_nested import routers


# \users\
# \users\{pk}
# \users\{users_pk}\lists\
# \users\{users_pk}\lists\{pk}
# \users\{users_pk}\lists\{pk}\todos\
# \users\{users_pk}\lists\{pk}\todos\{pk}


# Create a router and register our viewsets with it.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet, base_name='users')

user_router = routers.NestedSimpleRouter(router, r'users', lookup='user')
user_router.register(r'lists', TodoListViewSet, base_name='lists')

lists_router = routers.NestedSimpleRouter(user_router, r'lists', lookup='list')
lists_router.register(r'todos', TodoViewSet, base_name='todos')



# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
     url(r'^', include(router.urls)),
    url(r'^', include(user_router.urls)),
    url(r'^', include(lists_router.urls)),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
