# Generated by Django 3.2.6 on 2021-10-02 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('southkerala', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='category',
            field=models.CharField(choices=[('beach', 'BEACH'), ('culture and heritage', 'CULTURE AND HERITAGE'), ('hill stations', 'HILL STATIONS'), ('museum', 'MUSEUM'), ('temples', 'TEMPLES')], default='beach', max_length=22),
        ),
    ]
