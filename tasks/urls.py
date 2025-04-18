from rest_framework.routers import DefaultRouter
from django.urls import path

from .views import TaskViewSet, test_celery

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = router.urls
urlpatterns += [
    path('test/', test_celery)
]