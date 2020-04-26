# Generated by Django 2.2.5 on 2020-04-25 23:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('factory_manager', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Request_For_Repair',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(blank=True, choices=[('Выполнено', 'Выполнено'), ('Выполняется', 'Выполняется'), ('Выполнить невозможно', 'Выполнить невозможно'), ('Отправлено', 'Отправлено')], default='Отправлено', max_length=120, null=True)),
                ('comment', models.TextField()),
                ('date_request', models.DateTimeField(auto_now=True)),
                ('date_deadline', models.DateTimeField(auto_now=True)),
                ('boss_repair', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='boss_repair_repair', to=settings.AUTH_USER_MODEL)),
                ('cnc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='factory_manager.CNC')),
                ('worker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='worker_repair', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
