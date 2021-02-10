# Generated by Django 3.1.1 on 2020-12-15 06:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contacts',
            name='phone',
        ),
        migrations.CreateModel(
            name='ContactNotification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=100)),
                ('message', models.TextField(blank=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('is_seen', models.BooleanField(default=False)),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receive', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='send', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
