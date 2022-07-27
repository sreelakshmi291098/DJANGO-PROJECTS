# Generated by Django 3.2 on 2022-07-25 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=264, unique=True)),
                ('last_name', models.CharField(max_length=264, unique=True)),
                ('email_id', models.CharField(max_length=264, unique=True)),
                ('user_name', models.CharField(max_length=264, unique=True)),
                ('password', models.CharField(max_length=264, unique=True)),
                ('conform_password', models.CharField(max_length=264, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=264, unique=True)),
                ('Address', models.CharField(max_length=264, unique=True)),
                ('email_id', models.CharField(max_length=264, unique=True)),
                ('user_name', models.CharField(max_length=264, unique=True)),
                ('password', models.CharField(max_length=264, unique=True)),
                ('conform_password', models.CharField(max_length=264, unique=True)),
            ],
        ),
    ]
