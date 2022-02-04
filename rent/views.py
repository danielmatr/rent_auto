from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from rent.models import RentAuto
from rent.serializers import RentAutoSerializers


class RentAutoViewSet(viewsets.ModelViewSet):
    queryset = RentAuto.objects.all()
    serializer_class = RentAutoSerializers
    permission_classes = [IsAuthenticated, ]

    @action(detail=False, methods=['get'])
    def own(self, request, pk=None):
        queryset = self.get_queryset()
        queryset = queryset.filter(user=request.user)
        serializer = RentAutoSerializers(queryset, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)



