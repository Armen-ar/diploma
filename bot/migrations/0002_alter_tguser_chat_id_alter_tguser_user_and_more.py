# Generated by Django 4.0.1 on 2022-12-18 12:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bot', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tguser',
            name='chat_id',
            field=models.BigIntegerField(verbose_name='Номер чата.'),
        ),
        migrations.AlterField(
            model_name='tguser',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь.'),
        ),
        migrations.AlterField(
            model_name='tguser',
            name='user_ud',
            field=models.BigIntegerField(verbose_name='Пользовательский идентификатор.'),
        ),
        migrations.AlterField(
            model_name='tguser',
            name='verification_code',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Код верификации.'),
        ),
    ]
