# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0003_timer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timer',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
