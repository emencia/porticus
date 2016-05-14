# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('porticus', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ressource',
            name='related',
            field=models.ManyToManyField(related_name='_ressource_related_+', to='porticus.Ressource', blank=True),
        ),
    ]
