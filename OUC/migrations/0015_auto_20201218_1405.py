# Generated by Django 2.2.6 on 2020-12-18 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OUC', '0014_student_lock_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='openid',
            field=models.CharField(db_index=True, max_length=50, unique=True, verbose_name='openid'),
        ),
    ]
