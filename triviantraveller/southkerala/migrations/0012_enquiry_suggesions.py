# Generated by Django 3.2.6 on 2021-10-18 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('southkerala', '0011_hotels'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('enq_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250)),
                ('email_id', models.EmailField(max_length=250)),
                ('enquiry', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Suggesions',
            fields=[
                ('sugg_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250)),
                ('suggesion', models.TextField()),
            ],
        ),
    ]
