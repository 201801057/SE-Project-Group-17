# Generated by Django 3.1.6 on 2021-03-11 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_university'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='university',
            field=models.CharField(default='daiict', max_length=150),
        ),
    ]