# Generated by Django 2.2.3 on 2019-07-16 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0003_typeinfo_pic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ads',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='ads')),
                ('title', models.CharField(max_length=20)),
                ('indexes', models.IntegerField()),
            ],
        ),
    ]