from django.urls import include, path
from rest_framework.routers import DefaultRouter

from rent.views import RentAutoViewSet

router = DefaultRouter()
router.register('i', RentAutoViewSet)
urlpatterns = [
    path('', include(router.urls)),
]