# Generated by Django 2.2.6 on 2019-11-20 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OUC', '0002_auto_20191105_1314'),
    ]

    operations = [
        migrations.CreateModel(
            name='Swiper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='./static/upload_image/20191120')),
            ],
        ),
    ]
