# Generated by Django 4.0.3 on 2022-04-15 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_remove_passwords_pass_word_passwords_key'),
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('application_name', models.CharField(max_length=500)),
                ('username', models.CharField(max_length=100)),
                ('key', models.CharField(max_length=500)),
            ],
        ),
    ]