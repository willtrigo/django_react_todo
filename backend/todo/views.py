"""Todo view settings."""
from rest_framework import viewsets
from .serializers import TodoSerializer
from .models import Todo


class TodoView(viewsets.ModelViewSet):
    """Todo view."""

    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
