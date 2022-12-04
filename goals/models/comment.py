from django.db import models
from django.utils import timezone

from goals.models.goal import Goal


class GoalComment(models.Model):

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    text = models.TextField(verbose_name='Текст')
    goal = models.ForeignKey(
        Goal,
        verbose_name='Цель',
        related_name='comments',
        on_delete=models.PROTECT
    )
    user = models.ForeignKey(
        'core.User',
        verbose_name='Автор',
        related_name='comments',
        on_delete=models.PROTECT
    )
    created = models.DateTimeField(verbose_name='Дата создания')
    updated = models.DateTimeField(verbose_name='Дата последнего обновления')

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.updated = timezone.now()
        return super().save(*args, **kwargs)
