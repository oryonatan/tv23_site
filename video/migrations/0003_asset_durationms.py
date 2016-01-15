from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0002_snippet'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset',
            name='durationms',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
