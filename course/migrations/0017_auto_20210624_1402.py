# Generated by Django 3.2.4 on 2021-06-24 14:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('course', '0016_student_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='branch',
            name='manger',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='branch',
            name='creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='branches', to=settings.AUTH_USER_MODEL),
        ),
    ]
