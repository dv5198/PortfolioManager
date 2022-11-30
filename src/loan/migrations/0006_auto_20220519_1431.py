# Generated by Django 2.2.28 on 2022-05-19 09:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0005_auto_20220516_1735'),
    ]

    operations = [
        migrations.AddField(
            model_name='loan',
            name='loan_status',
            field=models.CharField(default=django.utils.timezone.now, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='loan',
            name='user',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
