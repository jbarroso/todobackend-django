from todos.serializers import TodoSerializer
from todos.models import Todos
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

class TodoList(generics.ListCreateAPIView):
    queryset = Todos.objects.all()
    serializer_class = TodoSerializer

    def perform_create(self, serializer):
        serializer.save()

    def delete(self, request, format=None):
        Todos.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todos.objects.all()
    serializer_class = TodoSerializer
