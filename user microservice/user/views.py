from rest_framework import generics, status
from rest_framework.response import Response

from .models import User
from . import serializers as _serializer

from confluent_kafka import Consumer

# conf = {
#     'bootstrap.servers': "pkc-6ojv2.us-west4.gcp.confluent.cloud:9092",
#     'security.protocol': "SASL_SSL",
#     'sasl.username': "DTWX3U2LLHWUJAV2",
#     'sasl.password': "TCdwZgOCrk9XGeNhqqqTNLd1snJciKTN3kMOXxaGHBFPfw/jQvZgbt5psGWoEnHD",
#     'sasl.mechanism': "PLAIN",
#     'group.id': "myGroup",
#     'auto.offset.reset': 'earliest'
# }

# consumer = Consumer(conf)


class UserCreateApiView(generics.CreateAPIView):
    """
    User Create views
    """
    serializer_class = _serializer.UserSerializer
    http_method_names = ['post']
    
    
    def post(self, request=None, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)
        if valid:
            serializer.save()
            status_code = status.HTTP_201_CREATED

            response = {
                'success': True,
                'statusCode': status_code,
                'message': 'User successfully Created!',
                'user': serializer.data
            }

            return Response(response, status=status_code)


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


class UserListApiView(generics.ListAPIView):
    """
    User List views
    """
    queryset = User.objects.all()
    serializer_class = _serializer.UserSerializer
    
    



