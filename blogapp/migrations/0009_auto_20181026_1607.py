# Generated by Django 2.1.2 on 2018-10-26 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0008_auto_20181026_0028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='moderation',
            field=models.BooleanField(default=False, verbose_name='модерация'),
        ),
    ]