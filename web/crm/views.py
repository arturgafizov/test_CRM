from django.shortcuts import render
from rest_framework.generics import ListAPIView
from . import serializers
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your views here.


class UsersListView(ListAPIView):
    serializer_class = serializers.UserListSerializer
    permission_classes = []

    def get_queryset(self):
        return User.objects.all()
