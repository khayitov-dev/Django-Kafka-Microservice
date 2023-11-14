import json
from django.http import JsonResponse
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from config.producer import producer
from monolith.services import UserService


from .models import User
from . import serializers as _serializer



class UserCreateApiView(APIView):
    """
    User Create views
    """
    http_method_names = ['post']
    
    def post(self, request):
        value = json.dumps(request.data).encode('utf-8')
        producer.produce("default", key="user_created", value=value)
        return JsonResponse(request.data)
    

class UserDetailsAPIView(generics.RetrieveAPIView):
    """
    User Detail views
    """
    queryset = User.objects.all()
    serializer_class = _serializer.UserSerializer
    lookup_field = "guid"


class UserUpdateApiView(generics.RetrieveUpdateAPIView):
    """
    User Update views
    """
    queryset = User.objects.all()
    serializer_class = _serializer.UserSerializer
    lookup_field = "guid"
    http_method_names = ['put', 'patch']


class UserDestroyApiView(generics.RetrieveDestroyAPIView):
    """
    User Delete views
    """
    queryset = User.objects.all()
    serializer_class = _serializer.UserSerializer
    lookup_field = "guid"
    http_method_names = ['delete']


class UserListApiView(APIView):
    """
    User List views
    """
    def get(self, request, *args, **kwargs):
        response = UserService.get("user-list/")
        return Response(response)