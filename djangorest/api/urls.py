from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView, DetailsView

urlpatterns = {
    url(r'^bucketlists/$', CreateView.as_view(), name="create"),
    url(r'^bucketlists/(?P<pk>[0-9]+)/$',
        DetailsView.as_view(), name="details"),
}

# Format suffix pattern helps to specify data format (raw json or html)
urlpatterns = format_suffix_patterns(urlpatterns)
