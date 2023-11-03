# Generated by Django 4.2.7 on 2023-11-01 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gp', '0008_mentor_alter_student_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('mentorname', models.CharField(max_length=255)),
            ],
        ),
    ]