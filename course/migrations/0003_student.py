# Generated by Django 3.2.4 on 2021-06-08 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('date_of_birth', models.DateField()),
                ('adaress', models.CharField(max_length=300, null=True)),
                ('phone_number', models.CharField(max_length=20)),
                ('gander', models.CharField(choices=[('male', 'male'), ('female', 'famale')], max_length=6)),
            ],
            options={
                'verbose_name': 'student',
                'verbose_name_plural': 'students',
            },
        ),
    ]
