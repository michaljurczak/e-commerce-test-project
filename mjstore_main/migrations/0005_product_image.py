# Generated by Django 3.0.7 on 2020-06-30 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mjstore_main', '0004_auto_20200629_2025'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
