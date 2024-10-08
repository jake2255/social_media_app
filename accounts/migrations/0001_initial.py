# Generated by Django 5.0.7 on 2024-08-17 16:42

import django.db.models.deletion
import django_resized.forms
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.CharField(blank=True, max_length=100)),
                ('profile_pic', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, quality=-1, scale=None, size=[50, 50], upload_to='accounts/images/')),
                ('friends', models.ManyToManyField(blank=True, to='accounts.accountuser')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
