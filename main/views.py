from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, viewsets, status
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from main.serializers import *
from main.service import get_client_ip, PaginationMovies, MovieFilter



class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny, ]


class AutoPostViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AutoPost.objects.all()
    serializer_class = AutoPostSerializer
    pagination_class = PageNumberPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_class = MovieFilter

    def get_queryset(self):
        post = AutoPost.objects.filter(draft=False).annotate(
            rating_user=models.Count("ratings",
                                     filter=models.Q(ratings__ip=get_client_ip(self.request)))
        ).annotate(
            middle_star=models.Sum(models.F('ratings__star')) / models.Count(models.F('ratings'))
        )
        return post

    @action(detail=False, methods=['get'])
    def search(self, request, pk=None):
        q = request.query_params.get('q')  # = request.GET
        queryset = self.get_queryset()
        queryset = queryset.filter(Q(title__icontains=q))
        serializer = AutoPostSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class AutoPostImageView(generics.ListAPIView):
    queryset = AutoPostImage.objects.all()
    serializer_class = AutoPostImageSerializer


class AddStarRatingViewSet(viewsets.ModelViewSet):
    """Добавление рейтинга фильму"""
    serializer_class = CreateRatingSerializer
    permission_classes = [IsAuthenticated, ]
    def perform_create(self, serializer):
        serializer.save(ip=get_client_ip(self.request))


# class PostLikeViewSet(viewsets.ModelViewSet):
#     queryset = AutoPost.objects.all()
#     serializer_class = AutoPostSerializer
#     permission_classes = [IsAuthenticated, ]
#
#     def get_permissions(self):
#         if self.action in ['list', 'retrieve']:
#             permissions = []
#         elif self.action == 'like':
#             permissions = [IsAuthenticated, ]
#         return [permissions() for permissions in permissions]
#
#     @action(detail=True, methods=['POST'])
#     def like(self, requests, *args, **kwargs):
#         post = self.get_object()
#         like_obj, _ = Like.objects.get_or_create(post=post, user=requests.user)
#         like_obj.like = not like_obj.like
#         like_obj.save()
#         status = 'Поставил лайк'
#         if not like_obj.like:
#             status = 'Убрал лайк'
#         return Response({'status': status})
#
#     def get_serializer_context(self):
#         return {'request': self.request}