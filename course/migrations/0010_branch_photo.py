# Generated by Django 3.2.4 on 2021-06-16 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0009_alter_branch_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='branch',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='branches/'),
        ),
    ]
