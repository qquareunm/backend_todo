from django.db import models

# Create your models here.
class TodoList(models.Model):
    name = models.CharField(null=False, max_length=255, blank=False)


    class Meta:
        verbose_name = 'Todo list'
        verbose_name_plural = 'Todo list'

class Todo(models.Model):
    name = models.CharField(null=False, max_length=255, blank=False)
    todo_list = models.ForeignKey(TodoList, null=False, on_delete=models.RESTRICT)

    class Meta:
        verbose_name = 'Todo'
        verbose_name_plural = 'Todos'

