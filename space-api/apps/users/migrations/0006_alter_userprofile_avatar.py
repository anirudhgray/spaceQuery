# Generated by Django 3.2.9 on 2021-12-31 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20211231_0842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.CharField(blank=True, default='default', max_length=255, null=True),
        ),
    ]