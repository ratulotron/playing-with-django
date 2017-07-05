from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateEntryView, EntryDetailsView

urlpatterns = {
    url(r'^$', CreateEntryView.as_view(), name="create"),
    url(r'^(?P<pk>[0-9]+)/$',
        EntryDetailsView.as_view(), name="details"),
}

# Format suffix pattern helps to specify data format (raw json or html)
urlpatterns = format_suffix_patterns(urlpatterns)
