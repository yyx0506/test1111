# Generated by Django 2.2.3 on 2019-07-11 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20190710_1446'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='type',
            field=models.IntegerField(default=0),
        ),
    ]