# Generated by Django 3.1.7 on 2021-04-03 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20210403_0745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='slug',
            field=models.CharField(blank=True, max_length=256, unique=True),
        ),
    ]
