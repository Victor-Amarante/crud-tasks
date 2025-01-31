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
