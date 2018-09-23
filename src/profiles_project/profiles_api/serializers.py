from rest_framework import serializers
# from . import models

class RadioSerializer(serializers.Serializer):
    """Serializes a name field for testing out APIView"""

    name = serializers.CharField(max_length=10)
