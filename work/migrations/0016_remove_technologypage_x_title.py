# Generated by Django 3.1.7 on 2021-03-11 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0015_technologypage_x_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='technologypage',
            name='x_title',
        ),
    ]