from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_nested import routers
from .views import TasklistViewSet, TaskViewSet


router = routers.SimpleRouter()
router.register(r'tasklists', TasklistViewSet)

tasklists_router = routers.NestedSimpleRouter(router, r'tasklists', lookup='tasklist')
tasklists_router.register(r'tasks', TaskViewSet, base_name='tasklist-tasks')

urlpatterns = [
    # url(r'^tasklists/$', TasklistListView.as_view(), name="tasklist_create"),
    # url(r'^tasklists/(?P<pk>[0-9]+)/$',
    #     TasklistDetailView.as_view(), name="tasklist_details"),
    # url(r'^tasklists/(?P<pk>[0-9]+)/$', TasklistListView.as_view(), name="tasklist_create"),
    # url(r'^tasklists/(?P<pk>[0-9]+)/$',
    #     TasklistDetailView.as_view(), name="tasklist_details"),
    url(r'^', include(router.urls)),
    url(r'^', include(tasklists_router.urls)),
]

# Format suffix pattern helps to specify data format (raw json or html)
urlpatterns = format_suffix_patterns(urlpatterns)
