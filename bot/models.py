from django.db import models


class TgUser(models.Model):
    chat_id = models.BigIntegerField(verbose_name='Номер чата.')
    user_ud = models.BigIntegerField(
        verbose_name='Пользовательский идентификатор.'
    )
    user = models.ForeignKey(
        'core.User',
        on_delete=models.PROTECT,
        null=True, blank=True,
        verbose_name='Пользователь.'
    )
    verification_code = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name='Код верификации.'
    )

    class Meta:
        verbose_name = 'Телеграмм_пользователь'
        verbose_name_plural = 'Телеграмм_пользователи'
