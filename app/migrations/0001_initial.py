# Generated by Django 4.1.2 on 2022-10-13 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('email', models.TextField(primary_key=True, serialize=False)),
                ('first_name', models.TextField()),
                ('last_name', models.TextField()),
                ('phone', models.TextField()),
            ],
            options={
                'db_table': 'student',
                'managed': False,
            },
        ),
    ]
