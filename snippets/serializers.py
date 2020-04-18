from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Snippet


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Snippet
        fields = ['url', 'id', 'title', 'code', 'linenos', 'language', 'style', 'owner']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(queryset=Snippet.objects.all(), many=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'snippets']
