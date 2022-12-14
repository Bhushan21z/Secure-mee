# Generated by Django 4.0.3 on 2022-04-17 13:41

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_alter_newuser_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='newuser',
            name='Status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='newuser',
            name='u_id',
            field=models.CharField(blank=True, default=uuid.uuid4, max_length=100, unique=True),
        ),
    ]
