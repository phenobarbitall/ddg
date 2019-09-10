# Create your views here.

from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from service.serializers import UserSerializer


class UserList(generics.ListAPIView):
    """
        Список профилей пользователей
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserRetrieve(generics.RetrieveAPIView):
    """
        Профиль пользователя
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UsernameList(APIView):
    """
        Список username зарегистрированных пользователей
    """

    def get(self, request, format=None):
        return Response(User.objects.all().values_list('username', flat=True))


class UserCount(APIView):
    """
        Количество зарегистрированных пользователей
    """

    def get(self, request, format=None):
        return Response(User.objects.all().count())
