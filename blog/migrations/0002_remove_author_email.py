# Generated by Django 5.1.4 on 2024-12-26 17:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='email',
        ),
    ]
