# Generated by Django 4.2.1 on 2023-05-15 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_student_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='дата создания'),
        ),
    ]
