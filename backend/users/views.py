from rest_framework import serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from social_django.utils import psa


class SocialSerializer(serializers.Serializer):
    """
    Serializer which accepts an OAuth2 access token.
    """
    access_token = serializers.CharField(
        allow_blank=False,
        trim_whitespace=True,
    )


@api_view(['POST'])
@permission_classes([AllowAny])
@psa()
def auth(request, backend):
    serializer = SocialSerializer(data=request.data)
    if serializer.is_valid():
        return Response({"token": "valid"})
    return Response({"token": "invalid"})
