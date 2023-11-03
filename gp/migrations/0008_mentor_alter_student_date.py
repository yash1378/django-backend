# Generated by Django 4.2.7 on 2023-11-01 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gp', '0007_alter_student_classs_alter_student_email_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('number', models.PositiveIntegerField()),
                ('college', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('handle', models.PositiveIntegerField()),
                ('total', models.PositiveIntegerField()),
                ('on', models.PositiveIntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='student',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
