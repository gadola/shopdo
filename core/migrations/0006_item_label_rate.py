# Generated by Django 2.2.10 on 2020-05-03 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20200502_1306'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='label_rate',
            field=models.CharField(default='NEW', max_length=100),
            preserve_default=False,
        ),
    ]
