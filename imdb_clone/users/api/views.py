from rest_framework import viewsets

from users.models import Group, User
from .serializers import  UserSerializer



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer