# Generated by Django 3.1.7 on 2021-03-11 10:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0010_auto_20210311_1009'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fullstackpage',
            old_name='description',
            new_name='full_stack_description',
        ),
    ]