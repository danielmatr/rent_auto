from django.urls import include, path
from rest_framework.routers import DefaultRouter

from main import views
from main.views import AutoPostViewSet, CategoryListView

# router = DefaultRouter()
# router.register('', PostLikeViewSet)
urlpatterns = [
    path('categories/', CategoryListView.as_view()),
    path("rating/", views.AddStarRatingViewSet.as_view({'post': 'create'})),

    # path('', include(router.urls)),
]