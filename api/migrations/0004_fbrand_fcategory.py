# Generated by Django 3.1.2 on 2021-02-11 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20210211_1710'),
    ]

    operations = [
        migrations.CreateModel(
            name='FBrand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fbrand', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='FCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fcategory', models.CharField(max_length=100)),
            ],
        ),
    ]
