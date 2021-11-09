# Generated by Django 3.2.9 on 2021-11-09 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0002_auto_20211109_0557'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='insuranceprovider',
            name='image_url',
        ),
        migrations.RemoveField(
            model_name='insuranceprovider',
            name='logo_image_url',
        ),
        migrations.AddField(
            model_name='insuranceprovider',
            name='name_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='insuranceprovider',
            name='provider_image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='insuranceprovider',
            name='provider_logo',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='insuranceprovider',
            name='key',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]