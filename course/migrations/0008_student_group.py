# Generated by Django 3.2.4 on 2021-06-09 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0007_alter_student_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='Group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='course.group'),
        ),
    ]
