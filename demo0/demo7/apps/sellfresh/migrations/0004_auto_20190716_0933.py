# Generated by Django 2.2.3 on 2019-07-16 01:33

import DjangoUeditor.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sellfresh', '0003_auto_20190715_2120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=DjangoUeditor.models.UEditorField(null=True),
        ),
    ]