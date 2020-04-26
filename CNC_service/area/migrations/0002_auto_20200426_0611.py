# Generated by Django 2.2.5 on 2020-04-26 03:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('area', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request_for_boss_repair',
            name='area',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='factory_manager.Area'),
        ),
        migrations.AlterField(
            model_name='request_for_boss_repair',
            name='boss_area',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='boss_area_boss_repair', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='request_for_boss_repair',
            name='boss_repair',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='boss_repair_boss_repair', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='request_for_boss_repair',
            name='cnc',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='factory_manager.CNC'),
        ),
    ]
