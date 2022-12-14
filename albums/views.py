from rest_framework.views import APIView, status, Response
from .models import Album
from .serializers import AlbumSerializer

from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.generics import ListCreateAPIView
from users.models import User


class AlbumView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset= Album.objects.all()
    serializer_class=AlbumSerializer

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user = user)