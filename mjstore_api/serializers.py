from django.contrib.auth.models import User

from rest_framework import serializers


class SimpleUserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=30, allow_blank=True)
    email = serializers.EmailField()
    last_login = serializers.DateTimeField()

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.last_login = validated_data.get('last_login', instance.last_login)
        instance.save()
        return instance


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'last_login']
