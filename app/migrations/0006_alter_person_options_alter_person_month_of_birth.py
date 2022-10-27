# Generated by Django 4.1.2 on 2022-10-20 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_person_published_date_alter_person_month_of_birth'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'ordering': ['last_name']},
        ),
        migrations.AlterField(
            model_name='person',
            name='month_of_birth',
            field=models.CharField(choices=[(1, 'January'), (2, 'February'), (3, 'March'), (4, 'April'), (5, 'May'), (6, 'June'), (7, 'July'), (8, 'August'), (9, 'September'), (10, 'October'), (11, 'November'), (12, 'December')], default='1', max_length=2),
        ),
    ]
