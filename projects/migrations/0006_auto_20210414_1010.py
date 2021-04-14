# Generated by Django 3.1.7 on 2021-04-14 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_auto_20210414_1006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='slug',
            field=models.CharField(blank=True, max_length=256, unique=True),
        ),
    ]
