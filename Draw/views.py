from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from .serializers import Pixel, PixelSerializer, UserSerializer
from rest_framework import status, response
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django_ratelimit.decorators import ratelimit


@api_view(['GET'])
def verify_token(request):
    return response.Response({}, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_pixels(request):
    queryset = Pixel.objects.all()
    serializer = PixelSerializer(queryset, many=True)
    return response.Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.create(serializer.validated_data)
        return response.Response(serializer.data, status=status.HTTP_200_OK)
    return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@ratelimit(key='ip', rate='1/3m')
def set_pixel(request):
    serializer = PixelSerializer(data=request.data, context={'user': request.user})
    if serializer.is_valid():
        serializer.create(serializer.validated_data)
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)('pixels', {
            'type': 'send.message',
            'text': serializer.data
        })
        return response.Response(serializer.data, status=status.HTTP_200_OK)
    return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
