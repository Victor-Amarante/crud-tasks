from django.urls import path
from rest_framework.routers import SimpleRouter
from crud.views import TasksViewSet


router = SimpleRouter()
router.register('tasks', TasksViewSet)
