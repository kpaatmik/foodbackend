# Generated by Django 5.1.5 on 2025-01-15 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodlisting',
            name='location',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
