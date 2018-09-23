from django.conf.locale import es
from django.shortcuts import render

from rest_framework import status  # , viewsets, , filters
from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework.authentication import TokenAuthentication
# from rest_framework.authtoken.serializers import AuthTokenSerializer
# from rest_framework.authtoken.views import ObtainAuthToken
# from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .estate_agent.module import Grab
from . import serializers  # ,  models, permissions


# Create your views here.


class RadioDestinationsApiView(APIView):
    """Gets list of compatible destination folders from local drive."""

    # serializer_class = serializers.RadioSerializer

    def get(self, request, format=None):
        """Returns an array of folder names."""

        folder_list = Grab.get_destination_folders()
        print(folder_list)

        return Response(folder_list)

    def post(self, request):
        """Create a hello message with our name."""

        serializer = serializers.RadioSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}!'.format(name)
            return Response({'message': message})
        else:
            return Response(
                    serializer.errors, status=status.HTTP_400_BAD_REQUEST)
