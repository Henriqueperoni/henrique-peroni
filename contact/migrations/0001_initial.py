# Generated by Django 3.1.7 on 2021-04-05 08:55

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('phone_number', phone_field.models.PhoneField(blank=True, max_length=20)),
                ('message', models.TextField(max_length=1500)),
            ],
        ),
    ]