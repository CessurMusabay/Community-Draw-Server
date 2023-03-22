from .models import Pixel, User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('password', 'username')

    def create(self, validated_data):
        return User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
        )


class PixelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pixel
        fields = ('x', 'y', 'color')

    def create(self, validated_data):
        pixel = Pixel.objects.filter(x=validated_data['x'], y=validated_data['y'])
        if pixel.count() > 0:
            pixel[0].delete()

        return Pixel.objects.create(
            x=validated_data['x'],
            y=validated_data['y'],
            color=validated_data['color'],
            user=self.context['user']
        )
