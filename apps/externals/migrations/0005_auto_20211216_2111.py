# Generated by Django 3.2.9 on 2021-12-16 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('externals', '0004_alter_external_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='external',
            name='image',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='external',
            name='link',
            field=models.URLField(),
        ),
    ]
