# Generated by Django 4.0.3 on 2022-04-17 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_remove_newuser_status_remove_newuser_u_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='Phone',
            field=models.CharField(max_length=12),
        ),
    ]
