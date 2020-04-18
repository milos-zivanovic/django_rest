from rest_framework import serializers
from django.contrib.auth.models import Group, User


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']
        extra_kwargs = {
            'url': {'view_name': 'quickstart:user-detail'},
        }


class GroupSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Group
        fields = ['url', 'name']
        extra_kwargs = {
            'url': {'view_name': 'quickstart:group-detail'},
        }
