# Generated by Django 3.1.3 on 2021-11-07 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('task_id', models.IntegerField()),
                ('status', models.BooleanField(default=False)),
                ('file_name', models.CharField(max_length=255, null=True)),
                ('frontend_name', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='UniqueTaskId',
            fields=[
                ('task_id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
    ]
