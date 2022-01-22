# Generated by Django 2.2.6 on 2022-01-22 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OUC', '0061_auto_20211010_1442'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='class_duties',
            field=models.SmallIntegerField(default=0, verbose_name='职务(0学生 1班长 2支书 3 学习委员  10其它)'),
        ),
        migrations.AddField(
            model_name='student',
            name='extra',
            field=models.TextField(default='', verbose_name='其它信息'),
        ),
        migrations.AlterField(
            model_name='studentrank',
            name='profession',
            field=models.CharField(default='-', max_length=40, verbose_name='专业'),
        ),
        migrations.AlterField(
            model_name='studentrank',
            name='research',
            field=models.CharField(default='-', max_length=40, verbose_name='研究方向'),
        ),
        migrations.AlterIndexTogether(
            name='studentrank',
            index_together={('profession', 'research', 'can_join_rank')},
        ),
        migrations.AddIndex(
            model_name='studentinfo',
            index=models.Index(fields=['sno'], name='idx_sno'),
        ),
        migrations.AddIndex(
            model_name='subscribestudent',
            index=models.Index(fields=['status'], name='idx_status'),
        ),
    ]
