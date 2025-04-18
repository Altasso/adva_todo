from celery import shared_task
from .models import Task


@shared_task
def add_numbers(a, b):
    print(f'Считаем: {a} + {b} = {a + b}')
    return a + b


@shared_task
def delete_task(task_id):
    try:
        task = Task.objects.get(id=task_id)
        task.delete()
        print(f'Задача {task_id} удалена')
    except Task.DoesNotExist:
        print(f'Задача {task_id} не найдена')
