# Generated by Django 4.1.3 on 2022-12-18 22:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='article',
        ),
    ]