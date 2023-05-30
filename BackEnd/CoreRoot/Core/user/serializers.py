from rest_framework import serializers
from django.conf import settings

from Core.abstract.serializers import AbstractSerializer
from Core.user.models import User


class UserSerializer(AbstractSerializer):

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if not representation['avatar']:
            representation['avatar'] = settings.DEFAULT_AVATAR_URL
            return representation
        if settings.DEBUG:  # debug enabled for dev
            request = self.context.get('request')
            representation['avatar'] = request.build_absolute_uri(representation['avatar'])
        return representation

    class Meta:
        model = User
        # List of all the fields that can be included in a request or a response
        fields = ['id', 'username', 'name', 'first_name', 'last_name', 'bio', 'avatar', 'email', 'is_active',
                  'created', 'updated']
        # List of all the fields that can only be read by the user
        read_only_field = ['is_active']