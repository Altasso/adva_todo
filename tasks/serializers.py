from celery import shared_task
from rest_framework import serializers
from .models import Task
from .tasks import delete_task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

    def create(self, validated_data):
        task = super().create(validated_data)
        delete_task.apply_async((task.id,), countdown=10)
        return task
