# Generated by Django 5.0.2 on 2024-06-14 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(unique=True)),
                ('file1', models.FileField(upload_to='data_files/')),
                ('file2', models.FileField(upload_to='data_files/')),
            ],
        ),
    ]
