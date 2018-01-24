from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from django.contrib import admin

from rest_framework import routers

from app.views import ToolViewSet

# this is DRF router for REST API viewsets
router = routers.DefaultRouter()

# register REST API endpoints with DRF router
router.register(r'tool', ToolViewSet, r"tool")

urlpatterns = [
    # default django admin interface
    path('admin/', admin.site.urls),
    
    # REST API root view (generated by DRF router)
    path('api/', include(router.urls)),
    
    # pure django views that don't use DRF
    # path('', index_view, {}, name='index'),
]

# in development django built-in server serves static and media content
# if not settings.PRODUCTION:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
