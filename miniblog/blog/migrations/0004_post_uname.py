# Generated by Django 3.1.6 on 2021-03-11 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210311_1118'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='uname',
            field=models.CharField(default='Tulsi', max_length=150),
        ),
    ]
