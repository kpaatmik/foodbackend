# Generated by Django 5.1.5 on 2025-01-15 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_foodlisting_visibilty_alter_foodlisting_expiry_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
