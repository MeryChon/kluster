# Generated by Django 3.2.9 on 2021-11-12 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0002_auto_20211111_1934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userfeedback',
            name='image',
            field=models.ImageField(default=None, upload_to=''),
            preserve_default=False,
        ),
    ]
