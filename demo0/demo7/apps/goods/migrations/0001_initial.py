# Generated by Django 2.2.3 on 2019-07-15 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TypeInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Goodsinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('pic', models.ImageField(upload_to='df_goods')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('danwei', models.CharField(default='500g', max_length=20)),
                ('goodsclick', models.IntegerField(default=0)),
                ('goodsdetail', models.CharField(max_length=50)),
                ('goodscontent', models.TextField()),
                ('goodstype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.TypeInfo')),
            ],
        ),
    ]