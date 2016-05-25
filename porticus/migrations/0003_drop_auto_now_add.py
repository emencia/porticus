# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('porticus', '0002_auto_20160514_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='creation_date',
            field=models.DateTimeField(verbose_name='creation date'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='creation_date',
            field=models.DateTimeField(verbose_name='creation date'),
        ),
        migrations.AlterField(
            model_name='ressource',
            name='creation_date',
            field=models.DateTimeField(verbose_name='creation date'),
        ),
    ]
