# Generated by Django 4.0.3 on 2022-04-17 12:59

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_store'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Status', models.BooleanField(default=False)),
                ('u_id', models.CharField(blank=True, default=uuid.uuid4, max_length=100, unique=True)),
                ('Name', models.CharField(max_length=100)),
                ('Phone', models.IntegerField(unique=True)),
                ('Email', models.EmailField(max_length=254)),
                ('Password', models.CharField(max_length=100)),
            ],
        ),
    ]
