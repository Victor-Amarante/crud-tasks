from django.shortcuts import render
from rest_framework import viewsets, filters, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from crud.models import Tasks
from crud.serializers import TasksSerializer


class TasksViewSet(viewsets.ModelViewSet):
  queryset = Tasks.objects.all()
  serializer_class = TasksSerializer
  filter_backends = [DjangoFilterBackend, filters.SearchFilter]
  filterset_fields = ['status']
  search_fields = ['title']
  pagination_class = PageNumberPagination
  
  def destroy(self, request, *args, **kwargs):
    instance = self.get_object()
    if instance:
        instance.delete()
        return Response({'message': 'Tarefa excluída com sucesso'}, status=status.HTTP_204_NO_CONTENT)
    return Response({'error': 'Tarefa não encontrada'}, status=status.HTTP_404_NOT_FOUND)
