# Generated by Django 3.0.7 on 2020-07-09 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mjstore_main', '0008_auto_20200708_2009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
