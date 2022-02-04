from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view, openapi
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
# from main.views import AutoViewSet
from main.views import AutoPostViewSet

schema_view = get_schema_view(
    openapi.Info(
        title='Authentication API',
        default_version='v1',
        description='Test Description',
    ),
    public=True
)
router = DefaultRouter()
router.register('auto-list', AutoPostViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('auto-list/', include('main.urls')),
    path('chat/', include('chat.urls')),
    path('swagger/', schema_view.with_ui()),
    path('', include(router.urls)),
    path('p/', include('comment.urls')),
    path('rent/', include('rent.urls')),
    # path('chat/', include('chat.urls')),
]
