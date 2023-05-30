from rest_framework import serializers

from Core.user.serializers import UserSerializer
from Core.user.models import User

class RegisterSerializer(UserSerializer):
    password = serializers.CharField(max_length=128, min_length=8, write_only=True, required=True)

    class Meta:
        model = User
        fields = ['id', 'name', 'bio', 'avatar', 'email', 'username', 'first_name', 'last_name', 'password']
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)