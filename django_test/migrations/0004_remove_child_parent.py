# Generated by Django 3.1.1 on 2020-09-16 08:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_test', '0003_child_parent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='child',
            name='parent',
        ),
    ]