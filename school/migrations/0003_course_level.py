# Generated by Django 4.2.4 on 2023-08-26 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_remove_tutor_course_course_tutors_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='level',
            field=models.CharField(choices=[('introductory', 'reception-1')], default='reception-1', max_length=22),
        ),
    ]
