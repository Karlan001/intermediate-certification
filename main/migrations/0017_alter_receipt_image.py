# Generated by Django 5.1.5 on 2025-02-05 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_alter_receipt_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipt',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Изображение'),
        ),
    ]
