# Generated by Django 4.2.7 on 2023-11-01 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gp', '0005_alter_student_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='classs',
            field=models.CharField(default='DefaultClass', max_length=200),
        ),
        migrations.AddField(
            model_name='student',
            name='mentor',
            field=models.CharField(default='DefaultMentor', max_length=200),
        ),
        migrations.AddField(
            model_name='student',
            name='subject',
            field=models.CharField(default='DefaultSubject', max_length=200),
        ),
    ]
