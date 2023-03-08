from django.db import models

# Create your models here.
class ToDo(models.Model):
    title = models.CharField(verbose_name='Название задачи', max_length=255)
    is_complete = models.BooleanField(default=False, verbose_name='Завершено')

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'

    def __str__(self):
        return f'{self.title}'