# Generated by Django 3.2.6 on 2021-10-04 06:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('southkerala', '0005_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='images',
        ),
    ]
