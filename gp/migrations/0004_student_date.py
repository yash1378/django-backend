# Generated by Django 4.2.7 on 2023-11-01 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gp', '0003_remove_student_classs_remove_student_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='date',
            field=models.DateTimeField(default='2021-01-01', verbose_name='date published'),
        ),
    ]
