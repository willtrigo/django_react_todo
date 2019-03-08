"""Todo serializer settings."""
from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    """Serializer Todo."""

    class Meta:
        """Init serializer todo."""

        model = Todo
        fields = ('id', 'title', 'description', 'completed')
