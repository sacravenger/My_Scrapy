# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scrapeyelp', '0003_auto_20150924_1619'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='reviews',
            table='scrape_data',
        ),
    ]
