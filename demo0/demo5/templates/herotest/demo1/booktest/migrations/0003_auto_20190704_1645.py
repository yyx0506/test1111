# Generated by Django 2.2.3 on 2019-07-04 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0002_auto_20190702_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='heroinfo',
            name='gender',
            field=models.CharField(choices=[('man', '男'), ('woman', '女')], max_length=5),
        ),
    ]
